# flake8: noqa

# standard library
import os
import re
import sys
from functools import wraps
from pathlib import Path

# dependent packages
import tools
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
from jupyter_io import savefig_in_notebook
from tqdm import tqdm


# decorators
def dataarray_func(func):
    @wraps(func)
    def wrapped(da, *args, **kwargs):
        return xr.zeros_like(da) + func(da, *args, **kwargs)

    return wrapped


# special path objects
def _get_path_from(env_var: str, default: str = ".") -> Path:
    """Get a resolved path from an environment variable."""
    path = Path(os.environ.get(env_var, default)).resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


DATA = _get_path_from("DATA_PATH", "./data")
PRODUCTS = _get_path_from("PRODUCTS_PATH", "./products")
LDATA = _get_path_from("LDATA_PATH", "./large/data")
LPRODUCTS = _get_path_from("LPRODUCTS_PATH", "./large/products")
