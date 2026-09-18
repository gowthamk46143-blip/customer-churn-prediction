import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Page settings
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# Load data and model
df = pd.read_csv("data/Telco-Customer-Churn.csv")
model = joblib.load("churn_model.pkl")

# Title
st.title("📊 Customer Churn Analytics & Prediction")
st.caption("Analyze customer behavior and predict churn using Machine Learning")

# Sidebar
st.sidebar.header("Dashboard Filters")

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Internet Service",
    options=df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

filtered_df = df[
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter))
]

# KPI calculations
total_customers = len(filtered_df)
churned_customers = (filtered_df["Churn"] == "Yes").sum()

if total_customers > 0:
    churn_rate = (churned_customers / total_customers) * 100
else:
    churn_rate = 0

avg_monthly = filtered_df["MonthlyCharges"].mean()

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Customers", total_customers)
col2.metric("⚠️ Churned", churned_customers)
col3.metric("📉 Churn Rate", f"{churn_rate:.2f}%")
col4.metric("💰 Avg Monthly Charges", f"${avg_monthly:.2f}")

st.divider()

# Churn distribution
st.subheader("📌 Churn Distribution")

col1, col2 = st.columns(2)

with col1:
    churn_counts = filtered_df["Churn"].value_counts()
    st.bar_chart(churn_counts)

with col2:
    fig, ax = plt.subplots()

    sns.countplot(
        data=filtered_df,
        x="Churn",
        ax=ax
    )

    ax.set_title("Customer Churn Count")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Customers")

    st.pyplot(fig)

# Monthly charges
st.subheader("💰 Monthly Charges vs Churn")

fig, ax = plt.subplots()

sns.boxplot(
    data=filtered_df,
    x="Churn",
    y="MonthlyCharges",
    ax=ax
)

ax.set_xlabel("Churn")
ax.set_ylabel("Monthly Charges")

st.pyplot(fig)

# Tenure analysis
st.subheader("📅 Customer Tenure Analysis")

fig, ax = plt.subplots()

sns.histplot(
    data=filtered_df,
    x="tenure",
    hue="Churn",
    bins=30,
    kde=True,
    ax=ax
)

ax.set_xlabel("Tenure (Months)")
ax.set_ylabel("Number of Customers")

st.pyplot(fig)

# Contract analysis
st.subheader("📄 Contract Type")

contract_counts = filtered_df["Contract"].value_counts()

st.bar_chart(contract_counts)

# Customer table
st.subheader("👥 Customer Data")

st.dataframe(
    filtered_df.head(50),
    use_container_width=True
)

st.divider()

# Prediction section
st.header("🔮 Customer Churn Prediction")

st.write("Enter customer details to predict churn probability.")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

with col2:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

# Prediction
if st.button("🔍 Predict Churn"):

    customer = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    customer = pd.get_dummies(
        customer,
        drop_first=True,
        dtype=int
    )

    customer = customer.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0][1]

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:
            st.error("⚠️ Customer is likely to Churn")
        else:
            st.success("✅ Customer is likely to Stay")

    with col2:
        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )

# Footer
st.divider()

st.caption(
    "Built with Python • Pandas • Scikit-learn • Streamlit"
)