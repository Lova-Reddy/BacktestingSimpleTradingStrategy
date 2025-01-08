import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Historical Stock Data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

# Calculate Moving Averages
def calculate_moving_averages(data, short_window=20, long_window=50):
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    return data

# Defining Trading Strategy
def generate_signals(data):
    data['Signal'] = 0
    data['Signal'][short_window:] = np.where(
        data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0
    )
    data['Position'] = data['Signal'].diff()
    return data

# Plot Results
def plot_strategy(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Stock Price', alpha=0.5)
    plt.plot(data.index, data['Short_MA'], label='Short MA (20 Days)', alpha=0.75)
    plt.plot(data.index, data['Long_MA'], label='Long MA (50 Days)', alpha=0.75)
    plt.scatter(data.index[data['Position'] == 1], data['Close'][data['Position'] == 1], 
                label='Buy Signal', marker='^', color='green', alpha=1)
    plt.scatter(data.index[data['Position'] == -1], data['Close'][data['Position'] == -1], 
                label='Sell Signal', marker='v', color='red', alpha=1)
    plt.title('Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid()
    plt.show()

# Main Execution
if __name__ == "__main__":
    file_path = "historical_stock_data.csv"  # CSV file
    data = load_data(file_path)
    short_window = 20
    long_window = 50
    
    data = calculate_moving_averages(data, short_window, long_window)
    data = generate_signals(data)
    
    plot_strategy(data)
