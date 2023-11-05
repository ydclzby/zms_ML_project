import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_original_data(stock_name,start_date,end_date):
    data = yf.download(stock_name, start=start_date, end=end_date)
    #data = data.set_index(pd.Index(range(1,len(data)+1)))
    #data['Date'] = pd.to_datetime(data['Date'])
    data["Difference"] = data["Open"] - data["Close"] #difference between Open and Close
    data["Volume_change"] = data["Volume"].diff() #difference between Volumes
    return data

def calculate_moving_average(data, window_size):
    # Assuming data is a pandas DataFrame with the financial data.
    moving_averages = data.rolling(window=window_size).mean()
    return moving_averages

def main():
    stock_name = 'AAPL'  # Example stock ticker
    start_date = '2020-01-01'
    end_date = '2020-12-31'

    # Get the original data
    data = get_original_data(stock_name, start_date, end_date)

    # Calculate the moving average with a specific window size, e.g., 20 days
    window_size = 20
    data_ma = calculate_moving_average(data, window_size)

    # Print the first few rows of the original data
    print("Original Data:")
    print(data.head())  # .head() prints the first 5 rows by default

    # Print the first few rows of the data with moving averages, skipping the initial NaN values
    print("\nData with Moving Averages (starting from row 21):")
    print(data_ma.iloc[20:].head())  # Skip the first 20 rows and print the next 5 rows

    # For large dataframe, export to a CSV file
    # data_ma.to_csv('data_with_moving_averages.csv')

    fig, (ax1, ax2) = plt.subplots(1,2,figsize = (20,8))
    #plot Close value for both data
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Stock Price")
    ax1.set_title("Close")
    ax1.plot(data.index, data.loc[:,"Close"], color = "red", label = "raw")
    ax1.plot(data_ma.index, data_ma.loc[:,"Close"], color = "blue", label = "moving_avg")
    ax1.legend(loc="upper left")

    #plot Volume
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Volume")
    ax2.set_title("Volume")
    ax2.plot(data.index, data.loc[:,"Volume"], color = "black", label = "raw")
    ax2.legend(loc="upper left")

    plt.show()
    plt.savefig('plot.png')

if __name__ == '__main__':
    main()