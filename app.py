import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="PeoplePulse Analytics",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background-color: #F4F6FC;
}

header {
    background-color: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #20264B;
}

.subtitle {
    color: #777E9B;
    font-size: 16px;
    margin-bottom: 25px;
}

.metric-card {
    background: white;
    padding: 24px;
    border-radius: 15px;
    border-left: 5px solid #7667E8;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.metric-title {
    color: #777E9B;
    font-size: 15px;
}

.metric-value {
    color: #20264B;
    font-size: 30px;
    font-weight: bold;
    margin-top: 8px;
}

.section-title {
    color: #20264B;
    font-size: 23px;
    font-weight: 700;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# Load Dataset
df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)


# Sidebar
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

# Apply Filters
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

# Header

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


# Calculate KPIs
total_employees = len(filtered_df)

attrition_count = (
    filtered_df["Attrition"] == "Yes"
).sum()

attrition_rate = (
    (attrition_count / total_employees) * 100
    if total_employees > 0 else 0
)

retained_employees = total_employees - attrition_count

# KPI Cards

st.markdown(
    '<div class="section-title">Workforce Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background:#E8E5FF; padding:22px; border-radius:15px;">
        <p style="color:#5146B8;">👥 Total Employees</p>
        <h2 style="color:#5146B8;">{total_employees:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background:#FFE8ED; padding:22px; border-radius:15px;">
        <p style="color:#D94F72;">📉 Employees Left</p>
        <h2 style="color:#D94F72;">{attrition_count:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background:#DDF7F1; padding:22px; border-radius:15px;">
        <p style="color:#168C78;">📈 Attrition Rate</p>
        <h2 style="color:#168C78;">{attrition_rate:.2f}%</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="background:#FFF1D9; padding:22px; border-radius:15px;">
        <p style="color:#C18422;">✅ Employees Stayed</p>
        <h2 style="color:#C18422;">{retained_employees:,}</h2>
    </div>
    """, unsafe_allow_html=True)

# Department Analysis
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
    color_discrete_sequence=["#7667E8", "#20BFA9", "#F28C9F"],
    title="Employee Attrition by Department"
)

st.plotly_chart(fig, use_container_width=True)


# Gender and Overtime Analysis

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

# Business Insights

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
    highest_department = department_attrition.loc[department_attrition["Employees"].idxmax(), "Department"]
    st.warning(f"🏢 Highest attrition count: {highest_department}")

# Employee Data Table

st.markdown(
    '<div class="section-title">👥 Employee Records</div>',
    unsafe_allow_html=True
)
search = st.text_input("🔍 Search Employee")

if search:
    filtered_df = filtered_df[
        filtered_df.astype(str).apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )
    ]

# Select Columns

all_columns = filtered_df.columns.tolist()

selected_columns = st.multiselect(
    "Choose Columns to Display",
    ["All"] + all_columns,
    default=[
        "EmployeeNumber",
        "Age",
        "Department",
        "Gender",
        "JobRole",
        "Attrition",
        "MonthlyIncome",
        "OverTime"
    ]
)

if "All" in selected_columns:
    selected_columns = all_columns

st.caption(f"Total Records Found: {len(filtered_df)}")

st.dataframe(
    filtered_df[selected_columns],
    use_container_width=True,
    hide_index=True,
    height=450
)

# Download Employee Data

csv = filtered_df[selected_columns].to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Employee Data",
    data=csv,
    file_name="PeoplePulse_Employee_Data.csv",
    mime="text/csv"
)