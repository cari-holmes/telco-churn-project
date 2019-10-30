import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from util import get_db_url
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    df.total_charges.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df = df.dropna()
    df['total_charges'] = df['total_charges'].astype(float)
    df['family'] = (df.partner == 'Yes') | (df.dependents == 'Yes')
    df['streaming_services'] = (df.streaming_movies == 'Yes') | (df.streaming_tv == 'Yes')
    df.drop(columns=['partner', 'dependents', 'streaming_tv', 'streaming_movies'], inplace=True)
    return df


def encode(train, test):
    encoder = LabelEncoder()
    train = train.drop(columns=['contract_type', 'internet_service_type','payment_type'])
    test = test.drop(columns=['contract_type', 'internet_service_type', 'payment_type'])
    encode_list = ['gender', 'phone_service','multiple_lines', 'online_security', 'online_backup','device_protection','tech_support', \
                'paperless_billing', 'churn', 'family', 'streaming_services']
    for c in encode_list:
        train[c] = encoder.fit_transform(train[c])
        test[c] = encoder.transform(test[c])
    return train, test

