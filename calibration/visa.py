import yfinance as yf
import pandas as pd

def download_data(ticker, start_date, end_date, data_dir='data', data_name='data'):
    raw = yf.download(ticker, start=start_date, end=end_date)
    raw.to_csv(f'{data_dir}/raw_data_{data_name}.csv')
    df = raw.reset_index().iloc[:,[0, 1]]
    df.columns = ['date', 'close_price']
    df.to_csv(f'{data_dir}/close_price_data_{data_name}.csv', index=False)
    return df

df_sp500 = download_data('^GSPC', '2000-01-01', '2025-01-01', data_name='sp500')
df_visa = download_data('V', '2000-01-01', '2025-01-01', data_name='visa')

# merge

# compute log return

# perform regression analysis

# statistical testing
