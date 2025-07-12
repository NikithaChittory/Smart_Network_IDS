# 🔒 Smart Network Intrusion Detection System (IDS)

A Machine Learning-based Intrusion Detection System (IDS) that analyzes network traffic and detects anomalies or attacks using a trained model. Includes a real-time dashboard built with Streamlit.

---

## 🚀 Features

- 🔍 Detects malicious activity using ML (Random Forest)
- 📊 Interactive dashboard for analysis (Streamlit)
- 📁 Simple upload-based detection
- 🧠 Preprocessing & feature extraction
- 💾 Trained model with NSL-KDD dataset

---

## 📂 Project Structure
Smart_Network_IDS/
├── dashboard/ # Streamlit dashboard app
├── data/ # Sample datasets (NSL-KDD & simulated)
├── models/ # Trained ML model (Random Forest)
├── notebooks/ # Jupyter notebook for EDA
├── scripts/ # Training & live monitor scripts
├── utils/ # Feature extraction functions
├── requirements.txt # Python dependencies
└── README.md # You are here


---

## 🛠️ Getting Started

### 🔹 1. Clone the Repo
git clone https://github.com/NikithaChittory/Smart_Network_IDS.git
cd Smart_Network_IDS


### 🔹 2. Create a Virtual Environment (Optional)
python -m venv venv
venv\Scripts\activate     # For Windows

### 🔹 3 Install Dependencies
pip install -r requirements.txt

### 🔹 4. Train the Model
python -m scripts.train_model

### 🔹 5. Run the Streamlit Dashboard
streamlit run dashboard/app.py
Then upload data/live_simulated.csv to test predictions.

<img width="1366" height="722" alt="image" src="https://github.com/user-attachments/assets/076c02e1-706a-42dd-9b1e-b1323aa25212" />

🤖 Tech Stack
Python
Scikit-learn
Streamlit
Pandas, NumPy
NSL-KDD Dataset

📬 Contact
Srinikitha Chittory
GitHub | LinkedIn (https://www.linkedin.com/in/srinikithachittory)
