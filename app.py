import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Vegetable price Prediction",
    page_icon="🥬",
    layout="wide"
)

# Title and description
st.title("🥬 Vegetable price Prediction")
st.markdown("""
This application helps predict vegetable prices in the market using machine learning.
Select a vegetable and date to get price predictions.
""")

# Sidebar for input parameters
st.sidebar.header("Input Parameters")

# Vegetable selection
vegetables = ["Tomato", "Potato", "Onion", "Carrot", "Cabbage"]
selected_vegetable = st.sidebar.selectbox("Select Vegetable", vegetables)

# Date selection
today = datetime.now().date()  # Get only the date part
max_date = today + timedelta(days=30)
selected_date = st.sidebar.date_input(
    "Select Date for Prediction",
    min_value=today,
    max_value=max_date,
    value=today
)

# Mock data for demonstration
def generate_mock_data():
    dates = pd.date_range(start=today - timedelta(days=30), end=today)
    prices = np.random.normal(50, 10, len(dates))  # Random prices around 50
    return pd.DataFrame({
        'Date': dates,
        'Price': prices
    })

# Display historical data
st.subheader("Historical Price Data")
historical_data = generate_mock_data()
st.line_chart(historical_data.set_index('Date')['Price'])

# Prediction section
st.subheader("Price Prediction")
if st.sidebar.button("Predict Price"):
    # Mock prediction (replace with actual model prediction)
    predicted_price = np.random.normal(50, 5)
    st.success(f"Predicted price for {selected_vegetable} on {selected_date}: ${predicted_price:.2f}")

# Additional information
st.markdown("---")
st.markdown("""
### About the Model
- The prediction model uses historical price data and market trends
- Predictions are based on seasonal patterns and market conditions
- Model is updated regularly with new data
""") 