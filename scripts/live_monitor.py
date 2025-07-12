
import pandas as pd
import joblib
from utils.feature_extraction import extract_features

model = joblib.load('models/ids_model.pkl')

df = pd.read_csv('data/live_simulated.csv')
X, _ = extract_features(df)

predictions = model.predict(X)

for i, pred in enumerate(predictions):
    status = 'Intrusion' if pred == 1 else 'Normal'
    print(f'Packet {i+1}: {status}')
