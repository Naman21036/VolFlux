import yfinance as yf
import pandas as pd

assets = {
    "SP500": "SPY",
    "BTC": "BTC-USD"
}

for name, ticker in assets.items():
    df = yf.download(ticker, start="2014-01-01", interval="1d")
    
    df = df[['Open','High','Low','Close','Volume']]
    
    df.to_csv(f"data/{name}_raw.csv")

    print(f"{name} data saved")