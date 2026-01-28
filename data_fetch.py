import yfinance as yf

def fetch_stock_data(symbol):
    print("Downloading stock data...")

    data = yf.download(symbol, period="6mo", progress=False)

    return data

