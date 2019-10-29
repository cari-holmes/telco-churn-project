import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from util import get_db_url

def clean_data(df):
    df.total_charges.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df = df.dropna()
    df['total_charges'] = df['total_charges'].astype(float)
    return df

