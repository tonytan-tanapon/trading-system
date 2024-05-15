import pandas as pd

def load_data():
    # Load your dataset here
    data = pd.read_csv('data/sample_data.csv', parse_dates=['Date'])
    return data

def preprocess_data(data):
    # Preprocess your data here
    # Example: Feature engineering, handling missing values, etc.
    data['PriceChange'] = data['Close'].pct_change()
    data = data.dropna()
    return data

if __name__ == '__main__':
    data = load_data()
    processed_data = preprocess_data(data)
    processed_data.to_csv('data/processed_data.csv', index=False)
