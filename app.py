import streamlit as st
import pandas as pd
import dill
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Set page config
st.set_page_config(page_title="Student Exam Performance", layout="centered")

# Title
st.title("🎓 Student Exam Performance Predictor")

st.markdown("Predict the **Math Score** based on student details:")

# Sidebar info
with st.sidebar:
    st.header("ℹ️ App Info")
    st.write("""
    - Predict student's math score.
    - Based on gender, race, education, lunch, preparation, reading & writing scores.
    """)

# Form
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    ethnicity = st.selectbox("Race or Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])
    parental_education = st.selectbox(
        "Parental Level of Education",
        ["Associate's degree", "Bachelor's degree", "High school", "Master's degree", "Some college", "Some high school"]
    )
    lunch = st.selectbox("Lunch Type", ["Free/Reduced", "Standard"])
    test_prep = st.selectbox("Test Preparation Course", ["None", "Completed"])
    
    reading_score = st.number_input("Reading Score (out of 100)", min_value=0, max_value=100, step=1)
    writing_score = st.number_input("Writing Score (out of 100)", min_value=0, max_value=100, step=1)

    submit = st.form_submit_button("🔍 Predict Math Score")

# Prediction
if submit:
    try:
        # Format input to CustomData
        data = CustomData(
            gender=gender.lower(),
            race_ethnicity=ethnicity.lower(),
            parental_level_of_education=parental_education.lower(),
            lunch=lunch.lower(),
            test_preparation_course=test_prep.lower(),
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        st.success(f"📊 Predicted Math Score: **{round(result[0], 2)}** / 100")

    except Exception as e:
        st.error(f"❌ Prediction Failed. Error: {e}")
