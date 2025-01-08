# Backtesting a Simple Trading Strategy

## Overview

The **Backtesting Simple Trading Strategy** is a Python application for analyzing and visualizing a simple moving average-based trading strategy. It allows users to backtest stock market data, generate buy/sell signals, and visualize the strategy’s performance on historical data.

## Features

- **Data Loading**: Processes historical stock price data from a CSV file.
- **Moving Average Calculation**: Computes short-term and long-term moving averages for strategy generation.
- **Signal Generation**: Identifies buy and sell signals based on moving average crossovers.
- **Visualization**: Plots stock prices, moving averages, and buy/sell signals for clear strategy interpretation.

## Requirements

Ensure you have Python 3.x installed along with the following libraries:

- `pandas`: For data manipulation and processing.
- `numpy`: For numerical calculations.
- `matplotlib`: For plotting and visualization.

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BacktestingSimpleTradingStrategy.git
   cd BacktestingSimpleTradingStrategy
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your historical stock data in CSV format with the name `historical_stock_data.csv`. The CSV should follow this structure:
   ```
   Date,Open,High,Low,Close,Volume
   2025-01-01,100,110,95,105,100000
   ```

4. Run the tool:
   ```bash
   python main.py
   ```

## How It Works

- The script reads the `historical_stock_data.csv` file.
- It calculates short-term (20-day) and long-term (50-day) moving averages.
- Buy signals are generated when the short-term moving average crosses above the long-term average.
- Sell signals are generated when the short-term moving average crosses below the long-term average.
- The strategy and signals are visualized on a graph for interpretation.

## Example Output

Upon running the script, you will see a plot like this:

- Stock prices with overlaid moving averages.
- Green triangles (`^`) indicating buy signals.
- Red triangles (`v`) indicating sell signals.

## File Structure

```
BacktestingSimpleTradingStrategy/
│
├── main.py                     # Main script for backtesting the strategy
├── historical_stock_data.csv   # Sample stock price data file
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```
--- 

By: Adithya Sai Srinivas
