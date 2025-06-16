# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 23:34:02 2025

@author: Aryan.singh
"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# SMTP Config (USE YOUR SMTP INFO HERE)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "aryansvce@gmail.com"   # Replace with your email
SENDER_PASSWORD = "your_app_password"   # Replace with app password (not your Gmail password!)

# Title
st.title("💪 Smart Health & BMI Assistant (With Email Report)")
st.subheader("Predict your Height, Calculate BMI & Get Personalized Health Advice with Email Report!")

# Load dataset
df = pd.read_csv('height-weight.csv')

# Graph
st.write("### 📈 Weight vs Height Trend")
plt.figure(figsize=(8,5))
sns.regplot(x='Weight', y='Height', data=df, scatter_kws={'alpha':0.3}, line_kws={"color":"red"})
st.pyplot(plt)

# Prepare ML model
X = df[['Weight']]
y = df['Height']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
regression = LinearRegression()
regression.fit(X_train_scaled, y_train)

# User Info
st.write("### 🔍 Enter Your Details:")
user_name = st.text_input("Enter your Name:")
user_email = st.text_input("Enter your Email:")

user_weight = st.number_input("Enter your Weight (kg):", min_value=1.0, step=0.5)
user_age = st.number_input("Enter your Age (years):", min_value=5, max_value=100, step=1)
gender = st.radio("Select your Gender:", ('Male', 'Female'))
activity_level = st.selectbox("Select your Activity Level:", ('Sedentary', 'Moderate', 'Active'))

# Prediction
if st.button("Predict Height, BMI & Get Recommendations + Email Report"):
    scaled_weight = scaler.transform([[user_weight]])
    predicted_height = regression.predict(scaled_weight)[0]

    height_in_meters = predicted_height / 100
    bmi = user_weight / (height_in_meters ** 2)

    # Results
    st.success(f"Predicted Height: {predicted_height:.2f} cm")
    st.success(f"Calculated BMI: {bmi:.2f}")

    # BMI category
    if bmi < 18.5:
        bmi_status = "Underweight"
        color = 'blue'
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal weight"
        color = 'green'
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight"
        color = 'orange'
    else:
        bmi_status = "Obesity"
        color = 'red'

    st.markdown(f"### 📝 **BMI Category: :{color}[{bmi_status}]**")

    # Calorie Intake Suggestion
    if bmi_status == "Underweight":
        calorie = "2500 - 2800 kcal/day"
    elif bmi_status == "Normal weight":
        calorie = "2000 - 2200 kcal/day"
    elif bmi_status == "Overweight":
        calorie = "1500 - 1800 kcal/day"
    else:
        calorie = "1200 - 1500 kcal/day (Consult dietitian)"

    # Activity Advice
    if activity_level == "Sedentary":
        activity_advice = "Try 20 mins walking or yoga daily."
    elif activity_level == "Moderate":
        activity_advice = "Maintain 30-45 mins cardio or strength workouts."
    else:
        activity_advice = "Super active! Keep up HIIT or sports."

    # Gender tip
    if gender == 'Male':
        gender_tip = "Include strength workouts. Ensure 7-8 hrs sleep."
    else:
        gender_tip = "Include calcium & iron-rich food. Yoga or Zumba for stress relief."

    # Age-based tip
    if user_age < 18:
        age_tip = "Growth phase! Milk, eggs, vitamins are essential."
    elif 18 <= user_age < 40:
        age_tip = "Stay active! Office workouts or cycling recommended."
    elif 40 <= user_age < 60:
        age_tip = "Include stretching, low-impact cardio, regular checkups."
    else:
        age_tip = "Regular doctor consultation & daily 15 mins walk."

    # Mental wellness
    wellness_tips = [
        "Practice 10 mins mindfulness meditation daily.",
        "Stay hydrated — 8 glasses of water a day!",
        "Ensure 7-9 hours of quality sleep.",
        "Limit screen time — digital detox once a week."
    ]
    mental_tip = random.choice(wellness_tips)

    # Log details
    log_content = f"""
    User: {user_name}
    Email: {user_email}
    Weight: {user_weight} kg
    Age: {user_age}
    Gender: {gender}
    Activity Level: {activity_level}

    Predicted Height: {predicted_height:.2f} cm
    BMI: {bmi:.2f} ({bmi_status})
    Suggested Calorie Intake: {calorie}
    Activity Advice: {activity_advice}
    Gender Tip: {gender_tip}
    Age Tip: {age_tip}
    Mental Wellness Tip: {mental_tip}
    """

    log_filename = f"{user_name}_health_report.txt"
    with open(log_filename, "w") as file:
        file.write(log_content)

    st.success("✅ Report Generated and saved!")

    # Send Email with Attachment
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = user_email
        msg['Subject'] = 'Your Health & BMI Report'

        body = "Hi {},\n\nPlease find attached your personalized Health & BMI Report.\n\nStay Healthy!\nAryan's Health Assistant".format(user_name)
        msg.attach(MIMEText(body, 'plain'))

        with open(log_filename, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=log_filename)
            part['Content-Disposition'] = f'attachment; filename="{log_filename}"'
            msg.attach(part)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        st.success(f"📧 Email sent successfully to {user_email}!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# Footer
st.write("----")
st.caption("Built with ❤️ by Aryan | Python, Streamlit, Seaborn, Scikit-Learn, SMTP Email")
