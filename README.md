# Network Anomaly Detection System

A Machine Learning project that detects whether network traffic is **Normal or an Attack**
using the **NSL-KDD dataset**, deployed with an interactive **Streamlit web app**.

---

# Live App:  
https://network-anomaly-detection-xzfgahvtf5apm45nkyvtv3.streamlit.app/


## Features
- Binary classification: Normal vs Attack
- 4 ML models compared: Random Forest, SVM, KNN, Isolation Forest
- **98% accuracy** achieved with Random Forest
- PCA visualization of high-dimensional data
- ROC Curve and AUC score evaluation
- Feature importance analysis (top 10 features)
- Interactive Streamlit UI for real-time prediction

---

## Tech Stack
| Category | Tools |
|----------|-------|
| Language | Python |
| ML Models | Scikit-learn (RF, SVM, KNN, IsolationForest) |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Serialization | Pickle |

---

## Model Results

| Model | Accuracy |
|-------|----------|
| Random Forest | **~98%** |
| SVM | ~97% |
| KNN | ~96% |
| Isolation Forest | Unsupervised |

---

## Project Structure
```
network-anomaly-detection/
├── Network_anomaly_detection.ipynb  # Full ML pipeline
├── app.py                           # Streamlit web app
├── model.pkl                        # Trained model (Random Forest)
├── scaler.pkl                       # Fitted StandardScaler
├── requirements.txt                 # Dependencies
└── README.md
```

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/PAWAN0836/network-anomaly-detection.git
cd network-anomaly-detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## Dataset
- **NSL-KDD** — improved version of KDD Cup 1999 dataset
- 41 features per network connection record
- Binary label: normal / attack

---

## Author
**Bairi Pawan Kumar** | B.Tech CSE | C.V. Raman Global University

## Connect With Me

- GitHub: https://github.com/PAWAN0836
- LinkedIn: [https://linkedin.com/in/YOUR-LINKEDIN](https://www.linkedin.com/in/bairi-paawan-kumar-26bb4628b/)
