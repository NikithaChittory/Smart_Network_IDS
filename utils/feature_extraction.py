
import pandas as pd
import numpy as np

def extract_features(df):
    # Basic feature selection and transformation
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if 'label' in df.columns:
        numeric_cols.remove('label')

    X = df[numeric_cols]
    y = df['label'] if 'label' in df.columns else None
    return X, y
