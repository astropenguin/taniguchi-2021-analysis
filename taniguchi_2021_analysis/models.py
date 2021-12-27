__all__ = [
    "calibrate_intensity",
    "despike_outliers",
    "bin_channels",
    "estimate_baseline",
]


# dependent packages
import numpy as np
import xarray as xr
from sklearn.linear_model import LinearRegression
from tqdm import tqdm


# main functions
def calibrate_intensity(P_sci, P_cal, T_amb=273, progress=True):
    """Calibrate intensity by chopper wheel calibration."""
    P_on = P_sci[P_sci.scantype == "ON"]
    P_off = P_sci[P_sci.scantype == "REF"]
    P_r = P_cal[P_cal.scanid == 0].mean("t")

    T_cal = xr.zeros_like(P_on)
    T_sys = xr.zeros_like(P_on)

    for on_id in tqdm(np.unique(P_on.scanid), disable=not progress):
        # ON array of single scan
        P_on_ = P_on[P_on.scanid == on_id]

        # OFF arrays between ON array
        P_off_lead = P_off[P_off.scanid == on_id - 1]
        P_off_trail = P_off[P_off.scanid == on_id + 1]
        P_off_ = xr.concat([P_off_lead, P_off_trail], "t").mean("t")

        # calibrate intensity and calculate Tsys
        T_cal_ = T_amb * (P_on_ - P_off_) / (P_r - P_off_)
        T_cal[T_cal.scanid == on_id] = T_cal_

        T_sys_ = T_amb / (P_r / P_off_ - 1)
        T_sys[T_sys.scanid == on_id] = T_sys_

    T_cal.coords["T_sys"] = T_sys
    return T_cal


def despike_outliers(T_cal, threshold=100):
    """Detect outliers and replace them by noise."""
    where = (np.abs(T_cal) > threshold) | np.isnan(T_cal)
    std = T_cal.values[~where].std()
    noise = np.random.normal(scale=std, size=int(where.sum()))

    T_cal_new = T_cal.copy()
    T_cal_new.values[where] = noise
    return T_cal_new


def bin_channels(T_cal, size=2):
    """Bin channels by given size."""
    shape = T_cal.shape[0], int(T_cal.shape[1] / size), size

    # compute binned values
    T_cal_bin = T_cal.values.reshape(shape).mean(2)
    T_cal_bin = xr.DataArray(T_cal_bin, dims=T_cal.dims)

    # set binned frequency
    ch_bin = T_cal.ch.values.reshape(shape[1:]).mean(1)
    T_cal_bin["ch"] = "ch", ch_bin

    # set binned T_sys (if any)
    if "T_sys" in T_cal.coords:
        T_sys_bin = T_cal.T_sys.values.reshape(shape).mean(2)
        T_cal_bin["T_sys"] = ("t", "ch"), T_sys_bin

    # set other t-shaped coords
    for key, coord in T_cal.coords.items():
        if coord.dims == ("t",):
            T_cal_bin[key] = coord

    return T_cal_bin


def estimate_baseline(T_cal, order=1, weight=1.0):
    """Estimate polynomial baseline of each sample."""
    freq = T_cal.ch - T_cal.ch.mean()
    n_freq, n_poly = len(freq), order + 1

    # make design matrix
    X = np.zeros([n_freq, n_poly])

    for i in range(n_poly):
        poly = freq ** i
        X[:, i] = poly / np.linalg.norm(poly)

    y = T_cal.values.T

    # estimate coeffs by solving linear regression problem
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y, sample_weight=weight)

    # estimate baseline
    T_base = xr.zeros_like(T_cal) + model.coef_ @ X.T

    for i in range(n_poly):
        T_base.coords[f"basis_{i}"] = "ch", X[:, i]
        T_base.coords[f"coeff_{i}"] = "t", model.coef_[:, i]

    return T_base
