# Vegetable Price Prediction App

This application predicts vegetable prices in the market using machine learning. The app is built with Streamlit and includes continuous integration using GitHub Actions.

## Features
- Interactive vegetable price prediction
- Historical price data visualization
- Machine learning-based price forecasting

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd vegetable-price-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Project Structure
- `app.py`: Main Streamlit application
- `model.py`: Machine learning model implementation
- `data/`: Directory for storing data
- `tests/`: Test files
- `.github/workflows/`: GitHub Actions workflow files

## Development
- The project uses Black for code formatting
- Flake8 for linting
- Pytest for testing

## License
MIT 