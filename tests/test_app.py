import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import generate_mock_data

def test_generate_mock_data():
    """Test the mock data generation function"""
    today = datetime.now().date()  # Get only the date part
    data = generate_mock_data()
    
    # Check if data is a DataFrame
    assert isinstance(data, pd.DataFrame)
    
    # Check if DataFrame has correct columns
    assert 'Date' in data.columns
    assert 'Price' in data.columns
    
    # Check if data has correct length
    assert len(data) == 31  # 30 days of historical data
    
    # Convert dates to date objects for comparison
    data_dates = pd.to_datetime(data['Date']).dt.date
    
    # Check if dates are within correct range
    assert data_dates.min() >= today - timedelta(days=30)
    assert data_dates.max() <= today
    
    # Check if prices are reasonable
    assert data['Price'].min() > 0
    assert data['Price'].max() < 100  # Assuming prices won't exceed 100 