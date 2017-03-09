import pandas as pd
import numpy as np

DATA_PATH = '5m_ms_10z13.rtab'

def load_data(fpath):
    data = pd.read_table(fpath)

