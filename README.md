# ML_LinearRegression

# AI-Powered BMI & Health Assistant 🤖💪

A Machine Learning and Streamlit-powered web app that predicts height based on weight, calculates BMI, provides personalized health, diet, and exercise recommendations, logs user activity, and emails a detailed report to the user.

---

## 🌟 Features

- Predicts **Height** using a Linear Regression model (Scikit-Learn)
- Calculates **BMI (Body Mass Index)**
- Personalized **diet and exercise suggestions** based on:
  - BMI Category
  - Age
  - Gender
  - Activity Level
- Generates a **detailed health report** (.txt)
- Automatically **emails the report to the user** (via SMTP)
- Logs all user inputs and model suggestions
- **Clean Streamlit UI**
- Data Visualization using **Seaborn & Matplotlib**

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit app
├── height-weight.csv     # Dataset used for training
├── requirements.txt      # All required Python libraries
├── README.md             # Project Documentation
├── /logs                # Folder to store user logs (generated dynamically)
```
---

## 🔧 Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/Aryansvce/ML_LinearRegression.git
cd BMI-Health-Assistant
```

2. **Create Virtual Environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run Streamlit App:**
```bash
streamlit run app.py
```

---

## 📦 Requirements (`requirements.txt`)

```
streamlit
pandas
scikit-learn
matplotlib
seaborn
smtplib
email
```

---

## 📬 Email Functionality Notes:

- Uses **SMTP (Gmail)** to send reports.
- Configure these in `app.py`:
```python
SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASSWORD = "your_app_password"
```
- Enable **App Password** in Gmail.

---

## 📊 Sample Output

| Weight (kg) | Predicted Height (cm) | BMI  | BMI Category | Suggested Calorie Intake |
|-------------|-----------------------|------|-------------|-------------------------|
| 70          | 172.34                | 23.1 | Normal      | 2000-2200 kcal/day       |

---

## 🙏 Acknowledgements

- **Dataset:** Public Height-Weight CSV
- **Tutorial Inspiration:** @Krish Naik (YouTube)
- **Tech:** Python, Scikit-Learn, Streamlit, Seaborn, Matplotlib, SMTP Email

---

## 🤝 Connect with Me

- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/aryanhpe/)
- **GitHub:** [GitHub](https://github.com/Aryansvce/ML_LinearRegression.git)
- **Developer:** [Aryan Singh]

---



