import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-container h1 {
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
    }
    
    .header-container p {
        font-size: 1.1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.95;
    }
    
    .input-section {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    .section-title {
        color: #667eea;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    .result-container {
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .result-high-risk {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        color: white;
    }
    
    .result-low-risk {
        background: linear-gradient(135deg, #51cf66 0%, #40c057 100%);
        color: white;
    }
    
    .result-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .result-description {
        font-size: 1rem;
        opacity: 0.95;
        margin-top: 1rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 8px;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }
    
    .info-box {
        background: #f0f3ff;
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    
    .sidebar-section {
        background: #f8f9ff;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load saved model, scaler, and expected columns
@st.cache_resource
def load_model():
    try:
        model = joblib.load("knn_heart.pkl")
        scaler = joblib.load("scaler.pkl")
        expected_columns = joblib.load("columns.pkl")
        return model, scaler, expected_columns
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None, None

# Header
st.markdown("""
    <div class="header-container">
        <h1>❤️ Heart Disease Predictor</h1>
        
    </div>
""", unsafe_allow_html=True)

# Information alert
st.info("💡 **Disclaimer**: This tool is for educational purposes only. Please consult with a healthcare professional for accurate diagnosis and treatment.")

# Load model
model, scaler, expected_columns = load_model()

if model is None:
    st.stop()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="input-section">
            <h2 class="section-title">📋 Your Health Information</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for different categories
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Basic Info", "💓 Heart Metrics", "🩺 ECG Data", "🏃 Activity"])
    
    with tab1:
        col_a, col_b = st.columns(2)
        with col_a:
            age = st.slider("Age (years)", 18, 100, 45, help="Your current age")
        with col_b:
            sex = st.selectbox("Sex", ["Male", "Female"])
    
    with tab2:
        col_c, col_d = st.columns(2)
        with col_c:
            resting_bp = st.number_input(
                "Resting Blood Pressure (mm Hg)",
                min_value=80,
                max_value=200,
                value=120,
                help="Normal: <120, Elevated: 120-129"
            )
        with col_d:
            cholesterol = st.number_input(
                "Total Cholesterol (mg/dL)",
                min_value=100,
                max_value=600,
                value=200,
                help="Desirable: <200, Borderline: 200-239, High: ≥240"
            )
        
        fasting_bs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dL",
            [("No", 0), ("Yes", 1)],
            format_func=lambda x: x[0],
            help="1 = True (>120 mg/dL), 0 = False (≤120 mg/dL)"
        )
        fasting_bs = fasting_bs[1]
    
    with tab3:
        resting_ecg = st.selectbox(
            "Resting ECG Result",
            ["Normal", "ST", "LVH"],
            help="Normal: Normal ECG, ST: ST-T wave abnormality, LVH: Left ventricular hypertrophy"
        )
        
        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "TA", "ASY"],
            help="ATA: Atypical Angina, NAP: Non-anginal Pain, TA: Typical Angina, ASY: Asymptomatic"
        )
    
    with tab4:
        col_e, col_f = st.columns(2)
        with col_e:
            max_hr = st.slider(
                "Max Heart Rate Achieved (bpm)",
                min_value=60,
                max_value=220,
                value=150,
                help="Maximum heart rate during exercise"
            )
        with col_f:
            exercise_angina = st.selectbox(
                "Exercise-Induced Angina",
                [("No", "N"), ("Yes", "Y")],
                format_func=lambda x: x[0],
                help="Angina induced by exercise"
            )
            exercise_angina = exercise_angina[1]
        
        col_g, col_h = st.columns(2)
        with col_g:
            oldpeak = st.slider(
                "Oldpeak (ST Depression)",
                min_value=0.0,
                max_value=6.0,
                value=1.0,
                step=0.1,
                help="ST depression induced by exercise"
            )
        with col_h:
            st_slope = st.selectbox(
                "ST Slope",
                ["Up", "Flat", "Down"],
                help="Slope of ST segment: Up/Flat/Down"
            )

# Sidebar for summary
with col2:
    st.markdown("""
        <div class="sidebar-section">
            <h3 style="color: #667eea; margin-top: 0;">📊 Input Summary</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.metric("Age", f"{age} yrs")
    st.metric("Sex", sex)
    st.metric("Resting BP", f"{resting_bp} mm Hg")
    st.metric("Max HR", f"{max_hr} bpm")
    st.metric("Cholesterol", f"{cholesterol} mg/dL")

# Prediction button
st.markdown("<br>", unsafe_allow_html=True)
col_pred1, col_pred2, col_pred3 = st.columns([1, 2, 1])

with col_pred2:
    predict_button = st.button("🔍 Analyze Heart Health", use_container_width=True)

# When Predict is clicked
if predict_button:
    # Create a raw input dictionary
    sex_code = sex[0]  # "M" or "F"
    
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex_code: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }
    
    # Create input dataframe
    input_df = pd.DataFrame([raw_input])
    
    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    # Reorder columns
    input_df = input_df[expected_columns]
    
    # Scale the input
    scaled_input = scaler.fit_transform(input_df)
    
    # Make prediction
    prediction = model.predict(scaled_input)[0]
    
    # Get prediction probability if available
    if hasattr(model, 'predict_proba'):
        probability = model.predict_proba(scaled_input)[0]
        risk_score = probability[1] * 100
    else:
        risk_score = 75 if prediction == 1 else 25
    
    # Display result with better styling
    st.markdown("<br>", unsafe_allow_html=True)
    
    if prediction == 1:
        st.markdown(f"""
            <div class="result-container result-high-risk">
                <div class="result-title">⚠️ HIGH RISK</div>
                <p style="font-size: 1.2rem;">Risk Score: {risk_score:.1f}%</p>
                <div class="result-description">
                    Based on your health metrics, there is a higher likelihood of heart disease.<br>
                    <strong>Please consult with a healthcare professional immediately.</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="result-container result-low-risk">
                <div class="result-title">✅ LOW RISK</div>
                <p style="font-size: 1.2rem;">Risk Score: {risk_score:.1f}%</p>
                <div class="result-description">
                    Based on your health metrics, your heart disease risk appears to be low.<br>
                    <strong>Continue maintaining a healthy lifestyle and regular check-ups.</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Additional health recommendations
    st.markdown("<br>", unsafe_allow_html=True)
    
    

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #888; padding: 1rem; border-top: 1px solid #ddd; margin-top: 2rem;">
        <p style="margin: 0;"><small>❤️ Heart Disease Predictor | THE DATA SCIENTIST ABHISHEK | Version 2.0</small></p>
        <p style="margin: 0.5rem 0 0 0;"><small>⚠️ Educational purposes only.</small></p>
    </div>
""", unsafe_allow_html=True)