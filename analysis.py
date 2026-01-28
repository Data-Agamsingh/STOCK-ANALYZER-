def analyze_stock(data):
    print("ANALYSIS STARTED")

    # 🚨 Check if data downloaded
    if data is None or data.empty:
        return "Stock data could not be downloaded. Try another symbol.", data

    # Ensure Close column exists
    if "Close" not in data.columns:
        return "Invalid data format received.", data

    # Create moving averages
    data["MA_20"] = data["Close"].rolling(window=20).mean()
    data["MA_50"] = data["Close"].rolling(window=50).mean()
    
    # Calculate RSI (14-day default)
    delta = data["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data["RSI"] = 100 - (100 / (1 + rs))

    # Drop rows where indicators not available
    data = data.dropna()

    if data.empty:
        return "Not enough data to calculate indicators.", data

    # Extract single values
    latest_price = data["Close"].values[-1]
    last_ma20 = data["MA_20"].values[-1]
    last_ma50 = data["MA_50"].values[-1]
    last_rsi = data["RSI"].values[-1]

    result = ""

    # Price vs Moving Averages
    if latest_price > last_ma20:
        result += f"Price ABOVE 20-day MA ({last_ma20:.2f})\n"
    else:
        result += f"Price BELOW 20-day MA ({last_ma20:.2f})\n"

    if latest_price > last_ma50:
        result += f"Price ABOVE 50-day MA ({last_ma50:.2f})\n"
    else:
        result += f"Price BELOW 50-day MA ({last_ma50:.2f})\n"

    # RSI Analysis
    result += f"\nRSI: {last_rsi:.2f}\n"
    if last_rsi > 70:
        result += "⚠️ OVERBOUGHT (RSI > 70) - Possible sell signal\n"
    elif last_rsi < 30:
        result += "⚠️ OVERSOLD (RSI < 30) - Possible buy signal\n"
    else:
        result += "✅ NEUTRAL (RSI between 30-70)\n"

    return result, data