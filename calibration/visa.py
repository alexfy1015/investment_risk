import yfinance as yf

# Download S&P 500 index data (ticker: ^GSPC)
sp500 = yf.download('^GSPC', start='2000-01-01', end='2025-01-01')

# Save to CSV
sp500.to_csv('sp500_data.csv')

print("S&P 500 data downloaded and saved to sp500_data.csv")