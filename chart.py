import matplotlib.pyplot as plt

print("CHART FILE LOADED")

def plot_stock(data, symbol):
    print("Plot function reached")
    
    # Create figure with 2 subplots (Price + RSI)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Plot 1: Price and Moving Averages
    ax1.plot(data.index, data["Close"], label="Close Price", linewidth=2)
    ax1.plot(data.index, data["MA_20"], label="20-day MA", linestyle="--")
    ax1.plot(data.index, data["MA_50"], label="50-day MA", linestyle="--")
    ax1.set_ylabel("Price ($)")
    ax1.set_title(f"{symbol} - Stock Analysis")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: RSI
    ax2.plot(data.index, data["RSI"], label="RSI", color="purple", linewidth=2)
    ax2.axhline(y=70, color='r', linestyle='--', label="Overbought (70)")
    ax2.axhline(y=30, color='g', linestyle='--', label="Oversold (30)")
    ax2.fill_between(data.index, 30, 70, alpha=0.1)
    ax2.set_ylabel("RSI")
    ax2.set_xlabel("Date")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.show()
    
    print("Chart displayed!")