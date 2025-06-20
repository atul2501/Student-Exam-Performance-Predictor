# 🎓 Student Exam Performance Predictor

A full-fledged machine learning project that predicts a student's math score based on several demographic and performance inputs. Built using Streamlit for UI and a custom ML pipeline for preprocessing and prediction.

---

## 🚀 Features

* Predicts math scores from demographic and academic info.
* Streamlit web app for user-friendly prediction interface.
* Trained model with proper preprocessing.
* Clean and modular code with logging and artifacts.

---

## 📁 Project Structure

```
Student-Exam-Performance-Predictor/
├── app.py                          # Streamlit frontend
├── setup.py                        # Project packaging
├── requirements.txt                # Dependencies
├── artifacts/                      # Trained model, preprocessor, datasets
├── logs/                           # Timestamped logs
├── .streamlit/config.toml          # Streamlit config
├── .ebextensions/                  # Elastic Beanstalk configs
├── notebook/                       # Jupyter notebooks for EDA & training
├── src/                            # ML pipeline code
├── catboost_info/                  # Additional training info
├── .gitignore                      # Git ignores
└── README.md                       # Project documentation
```

---

## 📘 Code Overview

### `app.py`

* Loads the `PredictPipeline` and `CustomData` from `src.pipeline.predict_pipeline`
* Collects user inputs via Streamlit form
* Predicts math score using the trained model
* Displays result to the user

### `CustomData`

A wrapper for user input. It collects the data and converts it into a DataFrame that matches training data format.

### `PredictPipeline`

Loads the `model.pkl` and `preprocessor.pkl`, applies transformation, and performs prediction.

---

## 🔍 How Prediction Works

1. User fills out form with inputs like gender, reading score, etc.
2. Input is wrapped with `CustomData()` and converted to DataFrame.
3. `PredictPipeline.predict()`:

   * Loads pre-trained model and preprocessor.
   * Applies preprocessing to the data.
   * Returns the predicted math score.

Example:

| Feature            | Value      |
| ------------------ | ---------- |
| Gender             | Female     |
| Ethnicity          | Group C    |
| Parental Education | Bachelor’s |
| Reading Score      | 85         |
| Writing Score      | 88         |

🔮 **Prediction**: Math Score ≈ 78.42

---

## 🧪 Running Locally

```bash
git clone https://github.com/atul2501/Student-Exam-Performance-Predictor.git
cd Student-Exam-Performance-Predictor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Dataset Source

* [Kaggle: Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)

---

## 👨‍💻 Author

**Atul Yadav**

* [LinkedIn](https://www.linkedin.com/in/atul-yadav-112063294/)
* [Medium Article](https://medium.com/@yatul247/build-a-professional-movie-recommender-system-using-python-streamlit-tmdb-api-f16ec17758b5)

---

## ✅ What’s Next

* Add model training UI
* Deploy on cloud (AWS Elastic Beanstalk planned)
* Expand to multi-output prediction (e.g., reading/writing scores)
