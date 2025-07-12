import streamlit as st
import pandas as pd
import joblib
import os
import sys

# ✅ Fix: Add parent folder to system path so 'utils' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.feature_extraction import extract_features

# ✅ Streamlit app UI
st.set_page_config(page_title="Smart Network IDS", layout="wide")
st.title("🔒 Smart Network Intrusion Detection System (IDS)")

uploaded_file = st.file_uploader("📤 Upload a network traffic CSV file", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        # Load trained model
        model_path = os.path.join("models", "ids_model.pkl")
        if not os.path.exists(model_path):
            st.error("❌ Model not found. Please train the model using `train_model.py` first.")
        else:
            model = joblib.load(model_path)

            # Extract features and predict
            X, _ = extract_features(df)
            preds = model.predict(X)

            # Add predictions to dataframe
            df['Prediction'] = preds
            df['Status'] = df['Prediction'].apply(lambda x: '🔴 Intrusion' if x == 1 else '🟢 Normal')

            # Show results
            st.subheader("📊 Prediction Results:")
            st.dataframe(df[['Status'] + list(df.columns.difference(['Prediction']))])

            st.success("✅ File processed successfully!")
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Upload a CSV file to begin detection.")
