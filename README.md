# ❤️ Heart Disease Prediction Model

A machine learning web application that predicts the risk of heart disease using patient health metrics. Built with **Streamlit** and **K-Nearest Neighbors (KNN)** algorithm.

## ✨ Features

- 🎯 AI-Powered Prediction using KNN algorithm
- 🎨 Beautiful modern Streamlit UI with gradient design
- 📊 Risk assessment with percentage scores
- 📋 Organized input forms with tabs
- 💡 Personalized health recommendations
- 🔍 Debug mode for model validation
- ⚡ Real-time predictions

## 🚀 Installation

### Requirements
- Python 3.8 or higher
- pip package manager

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install streamlit pandas scikit-learn joblib numpy
```

### Step 4: Run the App
```bash
streamlit run heart_disease_predictor.py
```

The app will open at `http://localhost:8501`

## 💻 Usage

### Running the Application
```bash
streamlit run heart_disease_predictor.py
```

### Using the App
1. **Enter Health Information** - Fill in 4 tabs of health metrics
2. **View Summary** - See all entered values on the right sidebar
3. **Get Prediction** - Click "Analyze Heart Health" button
4. **Review Results** - See risk assessment with recommendations

## 🧠 Model Details

### Algorithm
- **Type:** K-Nearest Neighbors (KNN)
- **K Value:** 5
- **Distance Metric:** Euclidean
- **Preprocessing:** StandardScaler normalization

### Features Used

| Feature | Type | Description |
|---------|------|-------------|
| Age | Numeric | Patient age in years |
| Sex | Categorical | Male/Female |
| Chest Pain Type | Categorical | ASY, ATA, NAP, TA |
| Resting BP | Numeric | Resting blood pressure (mm Hg) |
| Cholesterol | Numeric | Serum cholesterol (mg/dL) |
| Fasting BS | Binary | Fasting blood sugar > 120 mg/dL |
| Resting ECG | Categorical | Normal, ST, LVH |
| Max HR | Numeric | Maximum heart rate achieved |
| Exercise Angina | Categorical | Yes/No |
| Oldpeak | Numeric | ST depression |
| ST Slope | Categorical | Up, Flat, Down |

### Performance
- **Accuracy:** ~85%
- **Precision:** ~82%
- **Recall:** ~80%
- **F1-Score:** ~81%


## ⚠️ Disclaimer

**IMPORTANT:** This application is for **educational purposes only**.

**This tool is NOT a medical diagnostic device and should NOT be used for:**
- Self-diagnosis
- Treatment decisions
- Medical advice

**Always:**
- ✅ Consult with healthcare professionals
- ✅ Get proper medical examination
- ✅ Seek immediate help for chest pain or heart symptoms

**The developers assume NO LIABILITY** for medical decisions made based on this tool.

## 📦 Requirements

```
streamlit==1.28.1
pandas==2.1.0
scikit-learn==1.3.1
joblib==1.3.2
numpy==1.24.3
```

Install with:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing
**⭐ If this project helps you, please give it a star! ⭐**

