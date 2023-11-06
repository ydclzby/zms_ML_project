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
    moving_averages = data.rolling(window=window_size,min_periods = 1, center = True).mean()
    return moving_averages

def export_data(stock_name,start_date,end_date,window_size):
    # Get the original data
    data = get_original_data(stock_name, start_date, end_date)

    # Calculate the moving average with a specific window size, e.g., 20 days
    data_ma = calculate_moving_average(data, window_size)
    
    file_path_before_rolling = "../data/" + stock_name + "_" + start_date[:4] + "_before.csv"   
    file_path_after_rolling = "../data/" + stock_name + "_" + start_date[:4] + "_after.csv"   
    data.to_csv(file_path_before_rolling,index = True)
    data_ma.to_csv(file_path_after_rolling,index = True)

    # Print the first few rows of the original data
    print("Original Data:")
    print(data.head(10))  # .head() prints the first 5 rows by default

    # Print the first few rows of the data with moving averages, skipping the initial NaN values
    print("\nData with Moving Averages (starting from row 21):")
    print(data_ma.head(10))  # Skip the first 20 rows and print the next 5 rows

    # For large dataframe, export to a CSV file
    # data_ma.to_csv('data_with_moving_averages.csv')
    plot(data,data_ma)

def plot(data,data_ma):
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
    plt.savefig('../data/plot.png')



def main():
    stock_name = 'AAPL'  # Example stock ticker
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    window_size = 5
    export_data(stock_name,start_date,end_date,window_size)
    #print(start_date[:4])
if __name__ == '__main__':
    main()