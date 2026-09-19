import streamlit as st
import pandas as pd
import altair as alt
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# THEME
# =========================================================

st.markdown("""
<style>

:root {
    --blue: #2388ED;
    --blue-dark: #1672D4;
    --blue-light: #EAF4FF;
    --amber: #F5B83D;
    --amber-light: #FFF3D6;
    --red: #E5484D;
    --green: #2E9B67;
}

/* ==============================
   PAGE
   ============================== */

.stApp {
    background: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ==============================
   HEADER
   ============================== */

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #172033;
    letter-spacing: -1px;
    margin-bottom: 3px;
}

.subtitle {
    font-size: 15px;
    color: #687386;
    margin-bottom: 25px;
}

/* ==============================
   SIDEBAR
   ============================== */

section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #E7ECF2;
}

section[data-testid="stSidebar"] * {
    color: #263244;
}

.sidebar-title {
    font-size: 20px;
    font-weight: 800;
    color: #172033;
}

.sidebar-subtitle {
    font-size: 13px;
    color: #7A8494;
    margin-bottom: 15px;
}

/* ==============================
   KPI CARDS
   ============================== */

.metric-card {
    background: #FFFFFF;
    border: 1px solid #E7ECF2;
    border-radius: 14px;
    padding: 20px;
    min-height: 115px;
    box-shadow: 0 3px 12px rgba(25, 45, 70, 0.05);
}

.metric-label {
    color: #718096;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 8px;
}

.metric-value {
    color: #172033;
    font-size: 28px;
    font-weight: 800;
}

/* ==============================
   SECTION TITLES
   ============================== */

.section-title {
    font-size: 22px;
    font-weight: 750;
    color: #172033;
    margin-top: 18px;
    margin-bottom: 15px;
}

/* ==============================
   CHART CARDS
   ============================== */

.chart-card {
    background: #FFFFFF;
    border: 1px solid #E7ECF2;
    border-radius: 14px;
    padding: 12px;
    box-shadow: 0 3px 12px rgba(25, 45, 70, 0.04);
}

/* ==============================
   BUTTON
   ============================== */

.stButton > button {
    width: 100%;
    background: var(--blue);
    color: white;
    border: none;
    border-radius: 9px;
    padding: 12px 18px;
    font-size: 15px;
    font-weight: 750;
}

.stButton > button:hover {
    background: var(--blue-dark);
    color: white;
}

/* ==============================
   PREDICTION CARD
   ============================== */

.prediction-card {
    background: #FFFFFF;
    border: 1px solid #E7ECF2;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 16px rgba(25, 45, 70, 0.05);
}

/* ==============================
   FILTER AREA
   ============================== */

.filter-header {
    background: var(--amber-light);
    border-radius: 10px;
    padding: 10px 12px;
    font-weight: 700;
    color: #624500;
    margin-bottom: 8px;
}

/* ==============================
   DARK MODE
   ============================== */

@media (prefers-color-scheme: dark) {

    .stApp {
        background: #101827;
    }

    .main-title {
        color: #FFFFFF;
    }

    .subtitle {
        color: #9AA5B5;
    }

    .section-title {
        color: #FFFFFF;
    }

    section[data-testid="stSidebar"] {
        background: #151D2B;
        border-right: 1px solid #273244;
    }

    section[data-testid="stSidebar"] * {
        color: #E7ECF2;
    }

    .sidebar-title {
        color: #FFFFFF;
    }

    .sidebar-subtitle {
        color: #9AA5B5;
    }

    .metric-card,
    .chart-card,
    .prediction-card {
        background: #172033;
        border-color: #273244;
        box-shadow: none;
    }

    .metric-label {
        color: #9AA5B5;
    }

    .metric-value {
        color: #FFFFFF;
    }

    .filter-header {
        color: #FFE5A8;
        background: #3A2D12;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA + MODEL
# =========================================================

df = pd.read_csv(
    "data/Telco-Customer-Churn.csv"
)

model = joblib.load(
    "churn_model.pkl"
)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">Customer Churn Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Turn customer data into retention insights'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    '<div class="sidebar-title">📊 Customer Churn<br>Intelligence</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-subtitle">'
    'Predict. Retain. Grow.'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.markdown("---")

st.sidebar.markdown("### 🧭 Navigation")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Customer Insights",
        "Prediction",
        "Data Explorer",
        "About"
    ],
    label_visibility="collapsed"
)

# =========================================================
# DASHBOARD CONTROLS
# =========================================================

st.sidebar.markdown("---")

st.sidebar.markdown(
    '<div class="sidebar-title">🎛️ Dashboard Controls</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-subtitle">'
    'Filter customer segments'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# CURRENCY
# =========================================================

st.sidebar.markdown("### 💱 Display Currency")

currency = st.sidebar.selectbox(
    "Currency",
    [
        "INR (₹)",
        "USD ($)"
    ],
    label_visibility="collapsed"
)

USD_TO_INR = 90.0

# =========================================================
# TENURE
# =========================================================

st.sidebar.markdown("### 📅 Tenure Range")

tenure_range = st.sidebar.slider(
    "Tenure",
    0,
    72,
    (0, 72)
)

# =========================================================
# CONTRACT
# =========================================================

st.sidebar.markdown("### 📄 Contract Type")

contract_filter = st.sidebar.multiselect(
    "Contract",
    sorted(df["Contract"].unique()),
    default=sorted(df["Contract"].unique()),
    label_visibility="collapsed"
)

# =========================================================
# INTERNET
# =========================================================

st.sidebar.markdown("### 🌐 Internet Service")

internet_filter = st.sidebar.multiselect(
    "Internet",
    sorted(df["InternetService"].unique()),
    default=sorted(df["InternetService"].unique()),
    label_visibility="collapsed"
)

# =========================================================
# PAYMENT
# =========================================================

st.sidebar.markdown("### 💳 Payment Method")

payment_filter = st.multiselect(
    "Payment",
    sorted(df["PaymentMethod"].unique()),
    default=sorted(df["PaymentMethod"].unique()),
    label_visibility="collapsed"
)

# =========================================================
# GENDER
# =========================================================

st.sidebar.markdown("### 👤 Gender")

gender_filter = st.sidebar.selectbox(
    "Gender",
    ["All", "Male", "Female"],
    label_visibility="collapsed"
)

# =========================================================
# SENIOR CITIZEN
# =========================================================

st.sidebar.markdown("### 👴 Senior Citizen")

senior_filter = st.sidebar.selectbox(
    "Senior Citizen",
    ["All", "Yes", "No"],
    label_visibility="collapsed"
)

# =========================================================
# PARTNER
# =========================================================

st.sidebar.markdown("### 🤝 Partner")

partner_filter = st.sidebar.selectbox(
    "Partner",
    ["All", "Yes", "No"],
    label_visibility="collapsed"
)

# =========================================================
# DEPENDENTS
# =========================================================

st.sidebar.markdown("### 👨‍👩‍👧 Dependents")

dependents_filter = st.sidebar.selectbox(
    "Dependents",
    ["All", "Yes", "No"],
    label_visibility="collapsed"
)

# =========================================================
# PAPERLESS
# =========================================================

st.sidebar.markdown("### 🧾 Paperless Billing")

paperless_filter = st.sidebar.selectbox(
    "Paperless",
    ["All", "Yes", "No"],
    label_visibility="collapsed"
)

# =========================================================
# RESET
# =========================================================

st.sidebar.markdown("---")

if st.sidebar.button(
    "↻ Reset Filters",
    use_container_width=True
):
    st.rerun()

# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["tenure"].between(
        tenure_range[0],
        tenure_range[1]
    )
]

if contract_filter:
    filtered_df = filtered_df[
        filtered_df["Contract"].isin(contract_filter)
    ]

if internet_filter:
    filtered_df = filtered_df[
        filtered_df["InternetService"].isin(
            internet_filter
        )
    ]

if payment_filter:
    filtered_df = filtered_df[
        filtered_df["PaymentMethod"].isin(
            payment_filter
        )
    ]

if gender_filter != "All":
    filtered_df = filtered_df[
        filtered_df["gender"] == gender_filter
    ]

if senior_filter != "All":

    senior_value = (
        1 if senior_filter == "Yes"
        else 0
    )

    filtered_df = filtered_df[
        filtered_df["SeniorCitizen"] == senior_value
    ]

if partner_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Partner"] == partner_filter
    ]

if dependents_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Dependents"] == dependents_filter
    ]

if paperless_filter != "All":
    filtered_df = filtered_df[
        filtered_df["PaperlessBilling"] == paperless_filter
    ]

# =========================================================
# ABOUT PAGE
# =========================================================

if page == "About":

    st.markdown(
        '<div class="section-title">ℹ️ About This Project</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Customer Churn Intelligence is a Machine Learning "
        "analytics application built using the IBM Telco "
        "Customer Churn dataset."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Dataset", "IBM Telco")

    with col2:
        st.metric("Model", "Random Forest")

    with col3:
        st.metric("Platform", "Streamlit")

    st.write("### 🎯 Project Objectives")

    st.write(
        """
        • Analyze customer churn patterns  
        • Understand customer behavior  
        • Identify high-risk customers  
        • Predict churn probability  
        • Support customer retention decisions
        """
    )

    st.write("### 🛠️ Technology")

    st.write(
        "Python • Pandas • Scikit-learn • "
        "Altair • Streamlit • Joblib"
    )

    st.stop()

# =========================================================
# KPI VALUES
# =========================================================

total_customers = len(filtered_df)

churned_customers = (
    filtered_df["Churn"] == "Yes"
).sum()

churn_rate = (
    churned_customers /
    total_customers * 100
    if total_customers > 0
    else 0
)

avg_monthly = filtered_df[
    "MonthlyCharges"
].mean()

if pd.isna(avg_monthly):
    avg_monthly = 0

# =========================================================
# DASHBOARD PAGE
# =========================================================

if page == "Dashboard":

    # =====================================================
    # KPI SECTION
    # =====================================================

    st.markdown(
        '<div class="section-title">📈 Business Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">
                    👥 Total Customers
                </div>
                <div class="metric-value">
                    {total_customers:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">
                    ⚠️ Churned Customers
                </div>
                <div class="metric-value">
                    {churned_customers:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">
                    📉 Churn Rate
                </div>
                <div class="metric-value">
                    {churn_rate:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        if currency == "INR (₹)":

            display_charge = (
                avg_monthly *
                USD_TO_INR
            )

            symbol = "₹"

        else:

            display_charge = avg_monthly
            symbol = "$"

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">
                    💰 Avg Monthly Charges
                </div>
                <div class="metric-value">
                    {symbol}{display_charge:,.2f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.divider()

    # =====================================================
    # CHURN CHARTS
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Customer Churn Overview</div>',
        unsafe_allow_html=True
    )

    if filtered_df.empty:

        st.warning(
            "No customers match the selected filters."
        )

    else:

        left_chart, right_chart = st.columns(2)

        # -------------------------------------------------
        # CHURN COUNT
        # -------------------------------------------------

        with left_chart:

            churn_data = (
                filtered_df["Churn"]
                .value_counts()
                .reset_index()
            )

            churn_data.columns = [
                "Churn",
                "Customers"
            ]

            chart = (
                alt.Chart(churn_data)
                .mark_bar(
                    color="#2388ED",
                    cornerRadiusTopLeft=6,
                    cornerRadiusTopRight=6
                )
                .encode(
                    x=alt.X(
                        "Churn:N",
                        title="Churn"
                    ),
                    y=alt.Y(
                        "Customers:Q",
                        title="Customers"
                    ),
                    tooltip=[
                        "Churn",
                        "Customers"
                    ]
                )
                .properties(
                    title="Customer Churn Distribution",
                    height=320
                )
            )

            st.altair_chart(
                chart,
                use_container_width=True
            )

        # -------------------------------------------------
        # DONUT — BLUE ONLY
        # -------------------------------------------------

        with right_chart:

            churn_percentage = (
                filtered_df["Churn"]
                .value_counts(normalize=True)
                .mul(100)
                .round(2)
                .reset_index()
            )

            churn_percentage.columns = [
                "Churn",
                "Percentage"
            ]

            donut = (
                alt.Chart(churn_percentage)
                .mark_arc(
                    innerRadius=65
                )
                .encode(
                    theta="Percentage:Q",
                    color=alt.Color(
                        "Churn:N",
                        scale=alt.Scale(
                            domain=["No", "Yes"],
                            range=[
                                "#62B0FF",
                                "#1672D4"
                            ]
                        ),
                        legend=alt.Legend(
                            title=None
                        )
                    ),
                    tooltip=[
                        "Churn",
                        alt.Tooltip(
                            "Percentage:Q",
                            format=".2f"
                        )
                    ]
                )
                .properties(
                    title="Churn Rate Breakdown",
                    height=320
                )
            )

            st.altair_chart(
                donut,
                use_container_width=True
            )

    # =====================================================
    # CUSTOMER BEHAVIOR
    # =====================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '💰 Customer Behavior Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # MONTHLY CHARGES
    # -----------------------------------------------------

    if not filtered_df.empty:

        charges_df = filtered_df[
            ["Churn", "MonthlyCharges"]
        ].copy()

        if currency == "INR (₹)":

            charges_df["DisplayCharges"] = (
                charges_df["MonthlyCharges"] *
                USD_TO_INR
            )

            charge_title = "Monthly Charges (₹)"

        else:

            charges_df["DisplayCharges"] = (
                charges_df["MonthlyCharges"]
            )

            charge_title = "Monthly Charges ($)"

        charge_chart = (
            alt.Chart(charges_df)
            .mark_boxplot(
                extent="min-max"
            )
            .encode(
                x=alt.X(
                    "Churn:N",
                    title="Churn"
                ),
                y=alt.Y(
                    "DisplayCharges:Q",
                    title=charge_title
                ),
                color=alt.value(
                    "#2388ED"
                )
            )
            .properties(
                title="Monthly Charges vs Churn",
                height=340
            )
        )

        st.altair_chart(
            charge_chart,
            use_container_width=True
        )

        # -------------------------------------------------
        # TENURE
        # -------------------------------------------------

        tenure_chart = (
            alt.Chart(filtered_df)
            .mark_bar(
                color="#2388ED"
            )
            .encode(
                x=alt.X(
                    "tenure:Q",
                    bin=alt.Bin(
                        maxbins=30
                    ),
                    title="Tenure (Months)"
                ),
                y=alt.Y(
                    "count():Q",
                    title="Customers"
                ),
                tooltip=[
                    alt.Tooltip(
                        "count():Q",
                        title="Customers"
                    )
                ]
            )
            .properties(
                title="Customer Tenure Distribution",
                height=340
            )
        )

        st.altair_chart(
            tenure_chart,
            use_container_width=True
        )

        # -------------------------------------------------
        # CONTRACT
        # -------------------------------------------------

        contract_data = (
            filtered_df["Contract"]
            .value_counts()
            .reset_index()
        )

        contract_data.columns = [
            "Contract",
            "Customers"
        ]

        contract_chart = (
            alt.Chart(contract_data)
            .mark_bar(
                color="#2388ED",
                cornerRadiusTopLeft=6,
                cornerRadiusTopRight=6
            )
            .encode(
                x=alt.X(
                    "Contract:N",
                    title="Contract Type",
                    sort="-y"
                ),
                y=alt.Y(
                    "Customers:Q",
                    title="Customers"
                ),
                tooltip=[
                    "Contract",
                    "Customers"
                ]
            )
            .properties(
                title="Customers by Contract Type",
                height=340
            )
        )

        st.altair_chart(
            contract_chart,
            use_container_width=True
        )

# =========================================================
# CUSTOMER INSIGHTS
# =========================================================

if page == "Customer Insights":

    st.markdown(
        '<div class="section-title">'
        '🔎 Customer Insights'
        '</div>',
        unsafe_allow_html=True
    )

    if filtered_df.empty:

        st.warning(
            "No customers match the current filters."
        )

    else:

        insight1, insight2, insight3 = st.columns(3)

        # Month-to-month churn
        month_df = filtered_df[
            filtered_df["Contract"]
            == "Month-to-month"
        ]

        month_churn = (
            month_df["Churn"] == "Yes"
        ).mean() * 100 if len(month_df) else 0

        with insight1:
            st.metric(
                "Month-to-Month Churn",
                f"{month_churn:.1f}%"
            )

        # Fiber churn
        fiber_df = filtered_df[
            filtered_df["InternetService"]
            == "Fiber optic"
        ]

        fiber_churn = (
            fiber_df["Churn"] == "Yes"
        ).mean() * 100 if len(fiber_df) else 0

        with insight2:
            st.metric(
                "Fiber Optic Churn",
                f"{fiber_churn:.1f}%"
            )

        # Electronic check churn
        electronic_df = filtered_df[
            filtered_df["PaymentMethod"]
            == "Electronic check"
        ]

        electronic_churn = (
            electronic_df["Churn"] == "Yes"
        ).mean() * 100 if len(electronic_df) else 0

        with insight3:
            st.metric(
                "Electronic Check Churn",
                f"{electronic_churn:.1f}%"
            )

        st.divider()

        st.write("### 📌 Key Customer Segments")

        segment_data = (
            filtered_df.groupby(
                "Contract"
            )["Churn"]
            .apply(
                lambda x:
                (x == "Yes").mean() * 100
            )
            .reset_index()
        )

        segment_data.columns = [
            "Contract",
            "ChurnRate"
        ]

        segment_chart = (
            alt.Chart(segment_data)
            .mark_bar(
                color="#2388ED"
            )
            .encode(
                x=alt.X(
                    "Contract:N",
                    title="Contract"
                ),
                y=alt.Y(
                    "ChurnRate:Q",
                    title="Churn Rate (%)"
                ),
                tooltip=[
                    "Contract",
                    alt.Tooltip(
                        "ChurnRate:Q",
                        format=".2f"
                    )
                ]
            )
            .properties(
                height=380
            )
        )

        st.altair_chart(
            segment_chart,
            use_container_width=True
        )

# =========================================================
# DATA EXPLORER
# =========================================================

if page == "Data Explorer":

    st.markdown(
        '<div class="section-title">'
        '🗂️ Customer Data Explorer'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        f"Showing {len(filtered_df):,} filtered customers."
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=550
    )

# =========================================================
# PREDICTION PAGE
# =========================================================

if page == "Prediction":

    st.markdown(
        '<div class="section-title">'
        '🔮 Customer Churn Prediction'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter customer details to predict churn probability."
    )

    # -----------------------------------------------------
    # CUSTOMER NAME
    # -----------------------------------------------------

    customer_name = st.text_input(
        "👤 Customer Name",
        placeholder="Example: Arun Kumar"
    )

    st.caption(
        "Customer name is used only for displaying the result."
    )

    left, right = st.columns(2)

    # -----------------------------------------------------
    # CUSTOMER INFORMATION
    # -----------------------------------------------------

    with left:

        st.markdown("#### 👤 Customer Information")

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
            0,
            100,
            12
        )

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            [
                "Yes",
                "No",
                "No phone service"
            ]
        )

        internet_service = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        online_security = st.selectbox(
            "Online Security",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        online_backup = st.selectbox(
            "Online Backup",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

    # -----------------------------------------------------
    # SERVICE & BILLING
    # -----------------------------------------------------

    with right:

        st.markdown(
            "#### ⚙️ Service & Billing Details"
        )

        device_protection = st.selectbox(
            "Device Protection",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        tech_support = st.selectbox(
            "Tech Support",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
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

        if currency == "INR (₹)":

            monthly_display = st.number_input(
                "Monthly Charges (₹)",
                min_value=0.0,
                value=6300.0
            )

            total_display = st.number_input(
                "Total Charges (₹)",
                min_value=0.0,
                value=75600.0
            )

            monthly_charges = (
                monthly_display /
                USD_TO_INR
            )

            total_charges = (
                total_display /
                USD_TO_INR
            )

        else:

            monthly_charges = st.number_input(
                "Monthly Charges ($)",
                min_value=0.0,
                value=70.0
            )

            total_charges = st.number_input(
                "Total Charges ($)",
                min_value=0.0,
                value=840.0
            )

    # -----------------------------------------------------
    # PREDICT
    # -----------------------------------------------------

    st.write("")

    if st.button(
        "🔍 Predict Churn",
        use_container_width=True
    ):

        customer = pd.DataFrame({

            "gender": [gender],
            "SeniorCitizen": [senior],
            "Partner": [partner],
            "Dependents": [dependents],
            "tenure": [tenure],
            "PhoneService": [phone_service],
            "MultipleLines": [multiple_lines],
            "InternetService": [internet_service],
            "OnlineSecurity": [online_security],
            "OnlineBackup": [online_backup],
            "DeviceProtection": [device_protection],
            "TechSupport": [tech_support],
            "StreamingTV": [streaming_tv],
            "StreamingMovies": [streaming_movies],
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

        prediction = model.predict(
            customer
        )[0]

        probability = model.predict_proba(
            customer
        )[0][1]

        display_name = (
            customer_name.strip()
            if customer_name.strip()
            else "Customer"
        )

        st.write("")

        st.markdown(
            '<div class="prediction-card">',
            unsafe_allow_html=True
        )

        result1, result2 = st.columns(2)

        with result1:

            if prediction == 1:

                st.error(
                    f"⚠️ {display_name} is likely to CHURN"
                )

            else:

                st.success(
                    f"✅ {display_name} is likely to STAY"
                )

        with result2:

            st.metric(
                "Churn Probability",
                f"{probability * 100:.2f}%"
            )

        st.write("### Churn Risk")

        st.progress(
            float(probability)
        )

        if probability >= 0.70:

            st.error(
                "🔴 HIGH RISK — High predicted churn probability."
            )

        elif probability >= 0.40:

            st.warning(
                "🟠 MEDIUM RISK — Moderate predicted churn probability."
            )

        else:

            st.success(
                "🟢 LOW RISK — Lower predicted churn probability."
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#7A8494;
        padding:20px;
        font-size:13px;
    ">
        <b>Customer Churn Intelligence</b>
        &nbsp; | &nbsp;
        Built with Python, Streamlit & Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)