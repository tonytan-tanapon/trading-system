from ib_insync import *
import pandas as pd
import time

def load_signals():
    signals = pd.read_csv('data/trading_signals.csv', parse_dates=['Date'])
    return signals

def execute_trade(signal, contract, action, quantity):
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)

    order = MarketOrder(action, quantity)
    trade = ib.placeOrder(contract, order)
    
    while not trade.isDone():
        ib.sleep(1)
    
    ib.disconnect()

if __name__ == '__main__':
    signals = load_signals()
    contract = Stock('AAPL', 'SMART', 'USD')
    
    for index, row in signals.iterrows():
        if row['positions'] == 1.0:
            print(f"Buy signal on {row['Date']}")
            execute_trade(row, contract, 'BUY', 100)
        elif row['positions'] == -1.0:
            print(f"Sell signal on {row['Date']}")
            execute_trade(row, contract, 'SELL', 100)
        time.sleep(1)  # Sleep to avoid rate limit issues
