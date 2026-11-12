import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="PeoplePulse Analytics",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# ==========================================
# DARK / LIGHT MODE
# ==========================================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

st.sidebar.markdown("## 🎨 Appearance")

theme = st.sidebar.radio(
    "Select Theme",
    ["Light", "Dark"],
    horizontal=True,
    key="theme"
)

if theme == "Dark":
    bg = "#0E1424"
    card = "#192238"
    text = "#F1F5F9"
    muted = "#AAB4C8"
    border = "#2B3852"
    plot_template = "plotly_dark"

else:
    bg = "#F4F6FC"
    card = "#FFFFFF"
    text = "#20264B"
    muted = "#777E9B"
    border = "#E5E7EB"
    plot_template = "plotly_white"


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(f"""
<style>

.stApp {{
    background-color: {bg};
    color: {text};
}}

header {{
    background-color: transparent;
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

.metric-card {{
    background: {card};
    padding: 24px;
    border-radius: 15px;
    border-left: 5px solid #7667E8;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}}

.section-title {{
    color: {text};
    font-size: 23px;
    font-weight: 700;
    margin-top: 30px;
}}

.stTextInput label,
.stSelectbox label,
.stMultiSelect label {{
    color: {text} !important;
}}

.ask-box {{
    background: {card};
    padding: 22px;
    border-radius: 15px;
    border: 1px solid {border};
    margin-top: 12px;
}}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("## 📊 PeoplePulse")
st.sidebar.caption("Employee Analytics Platform")

st.sidebar.divider()

st.sidebar.subheader("Dashboard Filters")
st.sidebar.caption("Customize your workforce analysis")


if "department" not in st.session_state:
    st.session_state.department = "All"

if "gender" not in st.session_state:
    st.session_state.gender = "All"

if "overtime" not in st.session_state:
    st.session_state.overtime = "All"


def reset_filters():
    st.session_state.department = "All"
    st.session_state.gender = "All"
    st.session_state.overtime = "All"


department = st.sidebar.selectbox(
    "🏢 Select Department",
    ["All"] + sorted(df["Department"].unique()),
    key="department"
)

gender = st.sidebar.selectbox(
    "👤 Select Gender",
    ["All"] + sorted(df["Gender"].unique()),
    key="gender"
)

overtime = st.sidebar.selectbox(
    "⏰ Select Overtime",
    ["All"] + sorted(df["OverTime"].unique()),
    key="overtime"
)

st.sidebar.button(
    "🔄 Reset Filters",
    on_click=reset_filters
)


# ==========================================
# APPLY FILTERS
# ==========================================

filtered_df = df.copy()

if department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == department
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender
    ]

if overtime != "All":
    filtered_df = filtered_df[
        filtered_df["OverTime"] == overtime
    ]

analysis_df = filtered_df.copy()


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div style="
    background: linear-gradient(90deg, #5146B8, #7667E8);
    padding: 30px;
    border-radius: 15px;
    color: white;
    margin-bottom: 25px;
">
    <h1 style="color:white;">📊 PeoplePulse Analytics</h1>
    <p style="color:white; font-size:17px;">
        Employee Attrition & Workforce Insights
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()


# ==========================================
# CALCULATE KPIs
# ==========================================

total_employees = len(filtered_df)

attrition_count = (
    filtered_df["Attrition"] == "Yes"
).sum()

attrition_rate = (
    (attrition_count / total_employees) * 100
    if total_employees > 0 else 0
)

retained_employees = total_employees - attrition_count


# ==========================================
# KPI CARDS
# ==========================================

st.markdown(
    '<div class="section-title">Workforce Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

kpi_data = [
    ("👥 Total Employees", total_employees, "#7667E8"),
    ("📉 Employees Left", attrition_count, "#D94F72"),
    ("📈 Attrition Rate", f"{attrition_rate:.2f}%", "#168C78"),
    ("✅ Employees Stayed", retained_employees, "#C18422")
]

for col, (title, value, accent) in zip(
    [col1, col2, col3, col4],
    kpi_data
):
    with col:
        st.markdown(f"""
        <div style="
            background:{card};
            padding:22px;
            border-radius:15px;
            border-left:5px solid {accent};
            box-shadow:0 4px 15px rgba(0,0,0,0.07);
        ">
            <p style="color:{muted};">{title}</p>
            <h2 style="color:{text};">{value}</h2>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# DEPARTMENT ANALYSIS
# ==========================================

st.markdown(
    '<div class="section-title">Department Analysis</div>',
    unsafe_allow_html=True
)

department_attrition = (
    filtered_df[filtered_df["Attrition"] == "Yes"]
    .groupby("Department")
    .size()
    .reset_index(name="Employees")
)

fig = px.bar(
    department_attrition,
    x="Department",
    y="Employees",
    color="Department",
    color_discrete_sequence=[
        "#7667E8",
        "#20BFA9",
        "#F28C9F"
    ],
    title="Employee Attrition by Department",
    template=plot_template
)

st.plotly_chart(fig, width="stretch")


# ==========================================
# GENDER AND OVERTIME ANALYSIS
# ==========================================

st.markdown(
    '<div class="section-title">Employee Attrition Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Gender-wise Attrition")

    gender_attrition = (
        filtered_df[filtered_df["Attrition"] == "Yes"]
        .groupby("Gender")
        .size()
    )

    st.bar_chart(gender_attrition)

with col2:

    st.subheader("Overtime-wise Attrition")

    overtime_attrition = (
        filtered_df[filtered_df["Attrition"] == "Yes"]
        .groupby("OverTime")
        .size()
    )

    st.bar_chart(overtime_attrition)


# ==========================================
# BUSINESS INSIGHTS
# ==========================================

st.markdown(
    '<div class="section-title">💡 Business Insights</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.info(f"👥 {attrition_count} employees left the company.")

with col2:
    st.success(f"📊 Current Attrition Rate: {attrition_rate:.2f}%")

if not department_attrition.empty:

    highest_department = department_attrition.loc[
        department_attrition["Employees"].idxmax(),
        "Department"
    ]

    st.warning(
        f"🏢 Highest attrition count: {highest_department}"
    )


# ==========================================
# ASK PEOPLEPULSE
# ==========================================

st.markdown(
    '<div class="section-title">🤖 Ask PeoplePulse</div>',
    unsafe_allow_html=True
)

st.caption(
    "Ask questions about your employee dataset in simple English."
)

st.markdown(f"""
<div class="ask-box">
    <h4 style="color:{text};">
        Your HR Data Assistant
    </h4>
    <p style="color:{muted};">
        Explore workforce information using simple questions.
    </p>
</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "Ask your question",
    placeholder="Example: Which department has the highest attrition?"
)

if st.button("🔍 Get Answer"):

    q = question.lower().strip()

    if not q:
        st.warning("Please enter a question.")

    elif len(analysis_df) == 0:
        st.warning("No employee records found.")

    else:

        answer = None

        if "total employee" in q or "how many employee" in q:

            answer = f"Total employees: {len(analysis_df)}"

        elif (
            "employee left" in q
            or "employees left" in q
            or "how many left" in q
            or "attrition count" in q
        ):

            left = (
                analysis_df["Attrition"] == "Yes"
            ).sum()

            answer = f"Total employees who left: {left}"

        elif "attrition rate" in q:

            left = (
                analysis_df["Attrition"] == "Yes"
            ).sum()

            rate = left / len(analysis_df) * 100

            answer = f"Current attrition rate: {rate:.2f}%"

        elif "retention rate" in q:

            stayed = (
                analysis_df["Attrition"] == "No"
            ).sum()

            rate = stayed / len(analysis_df) * 100

            answer = f"Current retention rate: {rate:.2f}%"

        elif "department" in q:

            dept_data = (
                analysis_df[
                    analysis_df["Attrition"] == "Yes"
                ]
                .groupby("Department")
                .size()
            )

            if not dept_data.empty:

                highest = dept_data.idxmax()

                answer = (
                    f"{highest} has the highest attrition count "
                    f"with {dept_data.max()} employees leaving."
                )

            else:
                answer = "No attrition records found."

        elif "overtime" in q:

            overtime_data = (
                analysis_df[
                    analysis_df["Attrition"] == "Yes"
                ]
                .groupby("OverTime")
                .size()
            )

            answer = (
                "Employees who left by overtime category:\n"
                + overtime_data.to_string()
            )

        elif "gender" in q:

            gender_data = (
                analysis_df[
                    analysis_df["Attrition"] == "Yes"
                ]
                .groupby("Gender")
                .size()
            )

            answer = (
                "Gender-wise employees who left:\n"
                + gender_data.to_string()
            )

        elif "average age" in q or "mean age" in q:

            answer = (
                f"Average employee age: "
                f"{analysis_df['Age'].mean():.2f} years"
            )

        elif (
            "average salary" in q
            or "average income" in q
            or "monthly income" in q
        ):

            answer = (
                f"Average monthly income: "
                f"{analysis_df['MonthlyIncome'].mean():,.2f}"
            )

        else:

            answer = (
                "I couldn't understand that question yet. "
                "Please try one of the suggested questions."
            )

        st.success("PeoplePulse Answer")
        st.write(answer)


with st.expander("💬 Try these questions"):

    st.markdown("""
    - How many employees are there?
    - How many employees left?
    - What is the attrition rate?
    - What is the retention rate?
    - Which department has the highest attrition?
    - What is the overtime attrition count?
    - What is the gender-wise attrition?
    - What is the average age?
    - What is the average salary?
    """)


# ==========================================
# EMPLOYEE RECORDS
# ==========================================

st.markdown(
    '<div class="section-title">👥 Employee Records</div>',
    unsafe_allow_html=True
)

search = st.text_input("🔍 Search Employee")

if search:

    filtered_df = filtered_df[
        filtered_df.astype(str).apply(
            lambda row: row.str.contains(
                search,
                case=False
            ).any(),
            axis=1
        )
    ]


# ==========================================
# SELECT COLUMNS
# ==========================================

all_columns = filtered_df.columns.tolist()

default_columns = [
    "EmployeeNumber",
    "Age",
    "Department",
    "Gender",
    "JobRole",
    "Attrition",
    "MonthlyIncome",
    "OverTime"
]

selected_columns = st.multiselect(
    "Choose Columns to Display",
    ["All"] + all_columns,
    default=default_columns
)

if "All" in selected_columns:
    selected_columns = all_columns

st.caption(f"Total Records Found: {len(filtered_df)}")

st.dataframe(
    filtered_df[selected_columns],
    width="stretch",
    hide_index=True,
    height=450
)


# ==========================================
# DOWNLOAD EMPLOYEE DATA
# ==========================================

csv = filtered_df[selected_columns].to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Employee Data",
    data=csv,
    file_name="PeoplePulse_Employee_Data.csv",
    mime="text/csv",
    width="stretch"
)


# ==========================================
# EMPLOYEE ATTRITION PREDICTION
# ==========================================

st.divider()

st.markdown(
    '<div class="section-title">🔮 Employee Attrition Prediction</div>',
    unsafe_allow_html=True
)

st.caption(
    "Estimate employee attrition risk using the trained Machine Learning model."
)


@st.cache_resource
def load_attrition_model():

    return joblib.load(
        "models/attrition_model.pkl"
    )


try:

    model_data = load_attrition_model()

    model = model_data["model"]
    threshold = model_data["threshold"]

    st.markdown(f"""
    <div class="ask-box">
        <h4 style="color:{text};">
            Machine Learning Prediction
        </h4>
        <p style="color:{muted};">
            Select an employee ID to estimate their attrition probability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    selected_id = st.selectbox(
        "Select Employee ID",
        df["EmployeeNumber"].tolist()
    )

    employee = df[
        df["EmployeeNumber"] == selected_id
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Employee Age",
            employee["Age"]
        )

    with col2:
        st.metric(
            "Department",
            employee["Department"]
        )

    with col3:
        st.metric(
            "Job Role",
            employee["JobRole"]
        )

    if st.button("🔍 Predict Attrition Risk"):

        input_data = employee.drop(
            labels=[
                "Attrition",
                "EmployeeNumber",
                "EmployeeCount",
                "Over18",
                "StandardHours"
            ]
        ).to_frame().T

        probability = model.predict_proba(
            input_data
        )[0][1]

        predicted_class = (
            probability >= threshold
        )

        risk_percentage = probability * 100

        st.subheader("Prediction Result")

        st.metric(
            "Estimated Attrition Probability",
            f"{risk_percentage:.2f}%"
        )

        if risk_percentage >= 50:

            st.error("🔴 High Risk")

        elif risk_percentage >= 25:

            st.warning("🟡 Medium Risk")

        else:

            st.success("🟢 Low Risk")

        if predicted_class:

            st.info(
                "Model Prediction: Attrition risk flagged."
            )

        else:

            st.info(
                "Model Prediction: Attrition risk not flagged."
            )

        st.progress(
            float(probability)
        )

        st.caption(
            "This is an estimated prediction based on historical "
            "data. It does not guarantee an employee's future decision."
        )

except Exception as e:

    st.error(
        f"Unable to load prediction model: {e}"
    )