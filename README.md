# PeoplePulse Analytics

### Employee Attrition Analysis Dashboard

PeoplePulse Analytics is an interactive HR data analytics project built with Python and Streamlit. It explores employee attrition patterns and presents workforce metrics through an interactive dashboard.

## Live Demo

[Open Live Dashboard](https://peoplepulse-analytics-zi4hficzyey4to7fjfwk3e.streamlit.app/)

## Source Code

[GitHub Repository](https://github.com/arshkaur9998-glitch/PeoplePulse-Analytics)

## Project Objectives

- Explore employee data and check data quality.
- Analyse employee attrition and retention.
- Compare attrition across different employee categories.
- Present results through an interactive dashboard.
- Allow users to filter, search and export employee records.

## Dataset

- File: `WA_Fn-UseC_-HR-Employee-Attrition.csv`
- Total Records: 1,470
- Total Columns: 35
- Missing Values: 0

## Key Metrics

| Metric | Value |
|---|---:|
| Total Employees | 1,470 |
| Employees Who Left | 237 |
| Employees Who Stayed | 1,233 |
| Retention Rate | 83.88% |
| Attrition Rate | 16.12% |

These are descriptive results from the dataset, not predictions or proof of cause and effect.

## Dashboard Features

- Workforce overview KPI cards.
- Department, Gender and OverTime filters.
- Interactive Plotly charts.
- Employee records table with search.
- Selectable table columns.
- CSV download functionality.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- MySQL
- Git and GitHub

## Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/arshkaur9998-glitch/PeoplePulse-Analytics.git
cd PeoplePulse-Analytics
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the dashboard**

```bash
python -m streamlit run app.py
```

## Project Structure

```text
PeoplePulse_Analytics/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── raw/
├── notebooks/
├── reports/
├── src/
└── visuals/
```

## Future Improvements

- Add more HR metrics and dashboard explanations.
- Integrate a securely hosted database.
- Explore a validated predictive analytics model.
- Improve documentation and automated testing.

## Important Notes

- The dashboard reads the CSV dataset from the project repository.
- MySQL connection testing was performed locally.
- Never upload database passwords or API keys to a public repository.
- This project is intended for learning and descriptive analysis.

## Author

**Arshpreet Kaur**