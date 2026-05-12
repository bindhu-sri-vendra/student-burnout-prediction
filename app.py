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
st.sidebar.write("""
Stress Lens is a machine learning based burnout prediction system designed to analyze academic, emotional, and lifestyle factors that may contribute to student burnout.
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
    sleep_hours = st.slider("Sleep Hours", 0, 12, 6)
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
    result_col1, result_col2 = st.columns([1, 1])

    # Burnout Levels
    if prediction == 0:
        burnout_label = "Low Burnout"
        burnout_value = 25

        suggestions = [
            "Maintain a healthy sleep schedule",
            "Continue balancing academics and personal life",
            "Stay physically active",
            "Take regular study breaks"
        ]

    elif prediction == 1:
        burnout_label = "Moderate Burnout"
        burnout_value = 60

        suggestions = [
            "Reduce excessive study pressure",
            "Practice stress management techniques",
            "Increase relaxation time",
            "Talk to friends or mentors when stressed"
        ]

    else:
        burnout_label = "High Burnout"
        burnout_value = 90

        suggestions = [
            "Prioritize mental health and rest",
            "Seek emotional or academic support",
            "Reduce workload if possible",
            "Consult a counselor or mental health professional"
        ]

    # Donut Chart
    with result_col1:

        st.subheader("Burnout Analysis")

        chart_html = f"""
        <div style="display:flex; justify-content:center; align-items:center; margin-top:20px;">
            <div style="
                width:220px;
                height:220px;
                border-radius:50%;
                background: conic-gradient(
                    #FF5A5F {burnout_value}%,
                    #EAEAEA {burnout_value}%
                );
                display:flex;
                justify-content:center;
                align-items:center;
                box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
            ">
                <div style="
                    width:140px;
                    height:140px;
                    background:white;
                    border-radius:50%;
                    display:flex;
                    flex-direction:column;
                    justify-content:center;
                    align-items:center;
                    font-weight:bold;
                    font-size:22px;
                ">
                    {burnout_value}%
                </div>
            </div>
        </div>
        """

        st.markdown(chart_html, unsafe_allow_html=True)
        st.markdown(f"### {burnout_label}")

    # Suggestions Section
    with result_col2:

        st.subheader("Suggestions")

        for tip in suggestions:
            st.write(f"✅ {tip}")

st.divider()

# Footer
st.caption("Remember: burnout is not a weakness. Taking breaks, seeking support, and prioritizing mental well being are important steps toward maintaining a healthier and more balanced student life.")
