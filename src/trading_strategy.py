import pandas as pd
import numpy as np

def load_data():
    data = pd.read_csv('data/processed_data.csv', parse_dates=['Date'])
    return data

def moving_average_strategy(data, short_window=40, long_window=100):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

if __name__ == '__main__':
    data = load_data()
    signals = moving_average_strategy(data)
    signals.to_csv('data/trading_signals.csv', index=False)
