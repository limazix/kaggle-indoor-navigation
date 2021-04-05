# %%
%reload_ext autoreload
%autoreload 2

import os
import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('..')

import pandas as pd
import numpy as np

import tools
import importlib
importlib.reload(tools)

from tools.data import DataLoader
# %%
DATA_ROOT_DIR=os.path.abspath(os.path.join('..', 'data'))
DATA_TRAIN_DIR='{}/train'.format(DATA_ROOT_DIR)
DATA_TEST_DIR='{}/test'.format(DATA_ROOT_DIR)

print(DATA_TRAIN_DIR)
# %%
train_loader = DataLoader(data_dir=DATA_TRAIN_DIR)
print(train_loader.data_dir)
# %%
