# Health Evaluation App

## Overview
The *Health Evaluation App* is a machine learning-based web application designed to evaluate a person’s health and predict the likelihood of heart disease. By analyzing key health parameters, the application offers predictions to help users better understand their health status. The project is built using Python, Django, and machine learning techniques, and includes a user-friendly interface for input and output.

---

## Features
- *Heart Disease Prediction*: Predicts whether a person is likely to have heart disease based on provided health metrics.
- *Optimized Machine Learning Model*: Uses a Support Vector Machine (SVM) classifier trained on a balanced dataset for improved accuracy.
- *Data Preprocessing*: Automatically encodes categorical variables and scales numerical inputs for accurate predictions.
- *Web Interface*: User-friendly web forms built with Django for seamless interaction.
- *AI Doctor*: Auser friendly chatbot that is designed to give responses and answer health related quries along with seamless coverage that wprk as an all rounder.
- *Extensible Design*: Can be expanded to include additional features such as other health evaluations or advanced visualization tools.

---

## Input Features
The prediction model is trained on the following health parameters:
1. *Age*: Age of the person.
2. *Sex*: Male or Female (encoded numerically).
3. *Chest Pain Type*: Different types of chest pain experienced (encoded as categorical data).
4. *Fasting Blood Sugar*: Blood sugar level > 120 mg/dl (binary: 0 or 1).
5. *Resting ECG*: Results of resting electrocardiographic tests (encoded as categorical data).
6. *Maximum Heart Rate*: Maximum heart rate achieved during exercise.
7. *Exercise-Induced Angina*: Angina induced by exercise (binary: 0 or 1).
8. *Oldpeak*: ST depression induced by exercise relative to rest.
9. *ST Slope*: Slope of the peak exercise ST segment (encoded as categorical data).

---

## Tools and Technologies
- *Python*: For building the machine learning model.
- *Django*: Backend framework for the web application.
- *scikit-learn*: Used for model development and preprocessing.
- *pandas & numpy*: Data handling and analysis.
- *Matplotlib & Seaborn*: Data visualization during the analysis phase.
- *Joblib*: For saving and loading the machine learning model.
- *HTML*: A structure to create webframework.
- *CSS*: For styling the webpages.
- *JavaScript*: For a well structured integrating web interface.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Django framework
- Required Python libraries: pandas, numpy, scikit-learn, joblib, matplotlib, seaborn

### Steps
1. *Clone the Repository*:
   bash
   git clone https://github.com/your-username/health-evaluation-project.git
   cd health-evaluation-project
   

2. *Install Dependencies*:
   bash
   pip install -r requirements.txt
   

3. *Run Migrations*:
   bash
   python manage.py makemigrations
   python manage.py migrate
   

4. *Start the Development Server*:
   bash
   python manage.py runserver
   

5. *Access the Application*:
   Open your browser and navigate to http://127.0.0.1:8000/.

---

## How It Works

1. *Input Parameters*: Users provide inputs like age, chest pain type, and maximum heart rate via a web form.
2. *Preprocessing*: The application scales and encodes the input features to match the training dataset format.
3. *Prediction*: The preprocessed inputs are passed to the trained SVM model to predict whether the user is likely to have heart disease.
4. *Result Display*: The application displays the result as either "Heart Disease" or "No Heart Disease."

---

## Dataset
The project uses the *Heart Failure Prediction Dataset* from Kaggle. The dataset contains 918 samples with health-related attributes, such as age, sex, and blood sugar levels, and is balanced to ensure accurate predictions.

---

## Model Development
1. *Feature Selection*: Selected the top 9 features contributing the most to heart disease prediction based on correlation analysis.
2. *Data Preprocessing*:
   - Encoded categorical variables (e.g., Sex, ChestPainType).
   - Scaled numerical features using StandardScaler.
3. *Model Training*:
   - Split the dataset into training and test sets (80% training, 20% testing).
   - Trained an SVM model on the preprocessed data.
   - Achieved an accuracy of *~85%* on the test set.
4. *Model Saving*: Saved the trained model and scaler using joblib for future predictions.

---

## Example Usage
### Predict Heart Disease
python
import joblib
import pandas as pd

# Load the model and scaler
svm_model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')

# Example input
custom_input = [[45, 1, 2, 0, 1, 145, 0, 1.3, 1]]  # Replace with your own values
columns = ['Age', 'Sex', 'ChestPainType', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

# Preprocess input
custom_input_df = pd.DataFrame(custom_input, columns=columns)
custom_input_scaled = scaler.transform(custom_input_df)

# Predict
prediction = svm_model.predict(custom_input_scaled)
print("Prediction:", "No Heart Disease" if prediction[0] == 0 else "Heart Disease")


---

## Future Enhancements
1. Add advanced visualizations for health evaluation metrics.
2. Extend the application to include other disease prediction models.
3. Incorporate real-time data using wearable devices or health APIs.
4. Implement a chatbot for personalized health advice.

---

## Acknowledgments
- Kaggle for providing the *Heart Failure Prediction Dataset*.
- Open-source Python libraries: scikit-learn, pandas, matplotlib, and Django.

---

## License
This project is licensed under the Apache License 2.0. Feel free to use and modify it for personal or commercial purposes.

---

## Contact
For any questions or suggestions, feel free to reach out:

- *Email*: azkayasir09@gmail.com
- *GitHub*: [(https://github.com/azkayasir09/Health_Evaluation_App.git)]

---
