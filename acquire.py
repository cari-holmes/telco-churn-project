import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from util import get_db_url
from prepare import clean_data



def get_data_from_sql():
    query='''
    SELECT * FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id);
    '''

    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df

def acquire_telco():
    df = get_data_from_sql()
    df = clean_data(df)
    return df

