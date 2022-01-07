# taniguchi-2021-analysis
Analysis repository for Taniguchi et al. 2021, AJ, 162, 111

## How to use

This repository contains Jupyter notebooks (`notes/*`) and a Python package (`taniguchi_2021_analysis`).
It does **not** contain any observed datasets; please contact the corresponding author to get them.
Users can rerun the notebooks by a Jupyter notebook environment and dependencies described in `pyproject.toml`.
The following describes how to setup a standalone environment by VS Code and Docker.

1. Install [VS Code] and [Docker Desktop], and launch them
1. Install the [Remote Containers] extension to VS Code
1. Clone this repository
1. Put datasets (*.nc) in `./data`
1. Open the repository by VS Code
1. Choose `Reopen in Container` from the [Command Palette]

## Data

Data | LMT ID | Description
--- | --- | ---
xffts_20191126051026_086889_01.nc | 86889 | XFFTS spectra of a hot-load measurement for LMT ID 86890.
xffts_20191126051059_086890_01.nc | 86890 | XFFTS spectra of a CO(4-3) observation of PJ020941.3.
xffts_20191126055343_086895_01.nc | 86895 | XFFTS spectra of a hot-load measurement for LMT ID 86896.
xffts_20191126055417_086896_01.nc | 86896 | XFFTS spectra of a CO(5-4) observation of PJ020941.3.
lmttpm_20191126_086889_00_01.nc | 86889 | LMT telescope log.
lmttpm_20191126_086890_00_01.nc | 86890 | LMT telescope log.
lmttpm_20191126_086895_00_01.nc | 86895 | LMT telescope log.
lmttpm_20191126_086896_00_01.nc | 86896 | LMT telescope log.

## Notes

Note | Description
--- | ---
[2020-02-26](notes/2020-02-26) | Data analysis using an initial algorithm (GoDec + modification).
[2020-04-27](notes/2020-04-27) | Making figures for the paper (figures 1-3).
[2020-05-07](notes/2020-05-07) | Making figures for the paper (figures 4-11).
[2021-05-24](notes/2021-05-24) | Inspection of the LMT log (on-off separation and transition time).

[Command Palette]: https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette
[Docker Desktop]: https://www.docker.com/products/docker-desktop
[Remote Containers]: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
[VS Code]: https://code.visualstudio.com
