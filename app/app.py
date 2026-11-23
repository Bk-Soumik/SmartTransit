
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SmartTransit",
    page_icon="🚍",
    layout="wide"
)

# Main heading
st.title("🚍 SmartTransit")

st.markdown(
    "### Smart Public Transport Crowd Prediction System"
)

st.write(
    "Monitor and predict passenger crowd levels "
    "across Kolkata's public transport network."
)

st.divider()

# Sidebar
st.sidebar.title("SmartTransit")
st.sidebar.write("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Crowd Prediction",
        "Transport Analysis",
        "About Project"
    ]
)

# Dashboard
if page == "Dashboard":

    st.header("City Transport Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Transport Modes", "3")

    with col2:
        st.metric("City", "Kolkata")

    with col3:
        st.metric("System Status", "Development")

    st.subheader("Available Transport Modes")

    transport = st.selectbox(
        "Select Transport Mode",
        ["Bus", "Suburban Train", "Metro"]
    )

    st.info(f"You selected: {transport}")

# Crowd Prediction
elif page == "Crowd Prediction":

    st.header("Passenger Crowd Prediction")

    st.write(
        "This section will predict passenger crowd "
        "levels using our trained machine learning model."
    )

# Transport Analysis
elif page == "Transport Analysis":

    st.header("Transport Analysis")

    st.write(
        "This section will display passenger trends, "
        "peak hours and transport comparisons."
    )

# About Project
elif page == "About Project":

    st.header("About SmartTransit")

    st.write(
        """
        SmartTransit is a city-wide public transport
        crowd prediction system for Kolkata.

        It focuses on:
        - Bus services
        - Suburban trains
        - Metro services

        The objective is to help passengers identify
        less crowded travel times.
        """
    )
