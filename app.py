# Burnout Prediction Streamlit App Template
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page Configuration
st.set_page_config(
    page_title="Student Burnout Predictor",
    layout="centered"
)

#custom css
st.markdown("""
<style>

/* ================= BUTTON ================= */

div.stButton > button {
    background-color: #4EA8FF !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 600 !important;
    font-size: 18px !important;
}

div.stButton > button:hover {
    background-color: #3399FF !important;
    color: white !important;
}

/* ================= SLIDER ACTIVE TRACK ================= */

.stSlider div[data-baseweb="slider"] > div > div > div {
    background-color: #4EA8FF !important;
}

/* ================= SLIDER HANDLE ================= */

.stSlider div[role="slider"] {
    background-color: #4EA8FF !important;
    border-color: #4EA8FF !important;
}

/* ================= SLIDER VALUE TEXT ================= */

.stSlider div[data-testid="stThumbValue"] {
    color: #4EA8FF !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# Load Model
model = joblib.load('burnout_model.pkl')

#adding image
st.image(
    os.path.join(os.getcwd(), 'static', 'stress lens poster.png')
)

# Title Section
st.title("Student Burnout Prediction System")
st.markdown(
    "This application predicts burnout risk based on academic, emotional, and lifestyle factors."
)

st.divider()

# Sidebar
st.sidebar.header("About Project")
st.sidebar.divider()
st.sidebar.write("""
Stress Lens is a machine learning based burnout prediction system designed to analyze academic, emotional, and lifestyle factors that may contribute to student burnout.

----- Created by Bindhu 🖤 -----
""")

# Input Section
st.header("Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    study_hours_per_day = st.slider("Study Hours Per Day", 0, 10, 5)
    exam_pressure = st.slider("Exam Pressure", 0, 10, 5)
    stress_level = st.slider("Stress Level", 0, 10, 5)
    anxiety_score = st.slider("Anxiety Score", 0, 10, 5)
    depression_score = st.slider("Depression Score", 0, 10, 5)

with col2:
    sleep_hours = st.slider("Sleep Hours", 0, 10, 5)
    physical_activity = st.slider("Physical Activity", 0, 10, 5)
    social_support = st.slider("Social Support", 0, 10, 5)
    financial_stress = st.slider("Financial Stress", 0, 10, 5)
    family_expectation = st.slider("Family Expectation", 0, 10, 5)

# Create Input DataFrame
input_data = pd.DataFrame({
    'study_hours_per_day': [study_hours_per_day],
    'exam_pressure': [exam_pressure],
    'stress_level': [stress_level],
    'anxiety_score': [anxiety_score],
    'depression_score': [depression_score],
    'sleep_hours': [sleep_hours],
    'physical_activity': [physical_activity],
    'social_support': [social_support],
    'financial_stress': [financial_stress],
    'family_expectation': [family_expectation]
})

st.divider()

# Prediction Section
if st.button("Predict Burnout"):

    # Create Input Array
    user_data = np.array([[ 
        study_hours_per_day,
        exam_pressure,
        stress_level,
        anxiety_score,
        depression_score,
        sleep_hours,
        physical_activity,
        social_support,
        financial_stress,
        family_expectation
    ]])

    prediction = model.predict(user_data)[0]

    # Layout for Chart + Suggestions
    result_col1,spacer, result_col2 = st.columns([1,0.2, 1])

    # Burnout Levels
    if prediction == 0:
        burnout_label = "Low Burnout"

        suggestions = [
            "Maintain a healthy sleep schedule",
            "Continue balancing academics and personal life",
            "Stay physically active",
            "Take regular study breaks"
        ]

    elif prediction == 1:
        burnout_label = "Moderate Burnout"

        suggestions = [
            "Reduce excessive study pressure",
            "Practice stress management techniques",
            "Increase relaxation time",
            "Talk to friends or mentors when stressed"
        ]

    else:
        burnout_label = "High Burnout"

        suggestions = [
            "Prioritize mental health and rest",
            "Seek emotional or academic support",
            "Reduce workload if possible",
            "Consult a counselor or mental health professional"
        ]


    # burnout Chart
    with result_col1:
        if prediction == 0:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(
                os.path.join(os.getcwd(), 'static', 'low burnout.png')
                )
        elif prediction == 1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(
                os.path.join(os.getcwd(), 'static', 'moderate burnout.png')
                )
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(
                os.path.join(os.getcwd(), 'static', 'high burnout.png')
                )

    # Suggestions Section
    with result_col2:

        st.subheader("**Suggestions**")
        for tip in suggestions:
            st.write(f"✔️ {tip}")

st.divider()

# Footer
st.caption("Remember: burnout is not a weakness. Taking breaks, seeking support, and prioritizing mental well being are important steps toward maintaining a healthier and more balanced student life.")
