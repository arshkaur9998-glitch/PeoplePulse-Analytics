# 📊 PeoplePulse Analytics

### An Interactive HR Analytics and Employee Attrition Prediction System

PeoplePulse Analytics is a Python-based HR analytics project developed using Streamlit. It analyses employee data, identifies workforce trends, visualizes attrition patterns, and estimates employee attrition risk using Machine Learning.

## 🌐 Live Demo

[Open PeoplePulse Analytics Dashboard](https://peoplepulse-analytics-zi4hficzyey4to7fjfwk3e.streamlit.app/)

## 💻 Source Code

[GitHub Repository](https://github.com/arshkaur9998-glitch/PeoplePulse-Analytics)

---

## 🎯 Project Objectives

- Explore employee data and check data quality.
- Analyse employee attrition and retention patterns.
- Compare attrition across different employee categories.
- Develop an interactive HR analytics dashboard.
- Predict employee attrition risk using Machine Learning.
- Provide useful workforce insights to support HR decision-making.

---

## 📂 Dataset

The project uses the IBM HR Employee Attrition dataset.

- **Dataset File:** `WA_Fn-UseC_-HR-Employee-Attrition.csv`
- **Total Records:** 1,470
- **Total Columns:** 35
- **Missing Values:** 0

---

## 📈 Key Performance Indicators (KPIs)

| Metric | Value |
|---|---:|
| Total Employees | 1,470 |
| Employees Who Left | 237 |
| Employees Who Stayed | 1,233 |
| Retention Rate | 83.88% |
| Attrition Rate | 16.12% |

These metrics represent historical employee data.

---

## ✨ Dashboard Features

1. **Workforce Overview:** Displays important HR metrics through KPI cards.
2. **Interactive Filters:** Filter employee records by Department, Gender and Overtime.
3. **Department Analysis:** Visualizes employee attrition across departments.
4. **Gender-wise Analysis:** Compares attrition across gender categories.
5. **Overtime Analysis:** Examines attrition among employees working overtime.
6. **Business Insights:** Highlights important findings from employee data.
7. **Ask PeoplePulse:** Provides answers to supported questions about the HR dataset.
8. **Dark and Light Mode:** Allows users to switch dashboard themes.
9. **Employee Records:** Search and explore employee information.
10. **CSV Download:** Export filtered employee records.

---

## 🤖 Machine Learning Module

PeoplePulse Analytics includes an Employee Attrition Prediction module developed using the Random Forest Classification algorithm.

### Machine Learning Workflow

- Data Preprocessing
- Categorical Feature Encoding using One-Hot Encoding
- Train-Test Split
- Random Forest Classifier
- Class Imbalance Handling
- Decision Threshold Tuning
- Model Evaluation
- Employee Attrition Risk Prediction

### Prediction Features

- Select an employee using Employee ID.
- View employee details such as Age, Department and Job Role.
- Estimate attrition probability.
- Classify estimated risk into Low, Medium and High categories.
- Display the model's attrition prediction.

### Model Performance

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 81.29% |
| Attrition Recall | 38% |
| Selected Threshold | 0.34 |

The model provides estimated predictions based on historical employee information. Predictions are not guarantees of future employee decisions.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive charts |
| Streamlit | Dashboard development |
| Scikit-learn | Machine Learning |
| Joblib | Saving and loading the trained model |
| MySQL | Database connectivity and SQL practice |
| Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
PeoplePulse_Analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── attrition_model.pkl
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   └── 02_SQL_Connection.ipynb
│
├── src/
│   └── train_model.py
│
├── reports/
│
└── visuals/
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/arshkaur9998-glitch/PeoplePulse-Analytics.git
```

### 2. Navigate to the Project Folder

```bash
cd PeoplePulse-Analytics
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

### 5. Train the Machine Learning Model

```bash
python src/train_model.py
```

The trained model is saved in the `models` directory.

---

## 🔮 Future Improvements

- Improve Machine Learning model performance.
- Add more HR analytics metrics.
- Enhance employee risk analysis.
- Expand HR data assistant capabilities.
- Introduce automated HR report generation.

---

## ⚠️ Important Notes

- The dashboard analyses historical employee data.
- Machine Learning predictions are estimates and not guaranteed outcomes.
- MySQL connection testing was performed locally.
- Database credentials and API keys should never be uploaded to a public repository.
- This project is developed for academic and educational purposes.

---

## 👩‍💻 Author

**Arshpreet Kaur**

B.Tech Computer Science and Engineering

**Project:** PeoplePulse Analytics – Minor Project Part 2