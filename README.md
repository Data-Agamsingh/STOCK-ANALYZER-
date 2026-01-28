import sys
import os

for module in ['analysis', 'data_fetch', 'chart']:
    if module in sys.modules:
        del sys.modules[module]

sys.path.append(os.path.dirname(__file__))

from data_fetch import fetch_stock_data
from analysis import analyze_stock
from chart import plot_stock

print("Stock Market Project Analyzer Started")

symbol = input("Enter stock symbol (example: AAPL or TCS.NS): ")

# Fetch OF THE DATA YES !!!
data = fetch_stock_data(symbol)

#  CHECK IF DATA DOWNLOADED
if data is None or data.empty:
    print("\n❌ Could not download stock data.")
    print("Possible reasons:")
    print("• Wrong stock symbol")
    print("• Internet issue")
    print("• Yahoo Finance temporary block")
    exit()

# Analyze
analysis_result, data = analyze_stock(data)

print("\n📊 Stock Analysis Result:")
print(analysis_result)

print("\n📈 Data Preview:")
print(data.head())

#  Plot Graph
plot_stock(data, symbol)
