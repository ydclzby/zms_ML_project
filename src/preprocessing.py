import yfinance as yf
import pandas as pd

def get_original_data(stock_name,start_date,end_date):
    data = yf.download(stock_name, start=start_date, end=end_date)
    data = data.set_index(pd.Index(range(1,len(data)+1)))
    data["Difference"] = data["High"] - data["Low"] #difference between High and Low
    data["Volume_change"] = data["Volume"].diff() #difference between Volumes
    return data