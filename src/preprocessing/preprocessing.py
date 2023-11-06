import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_original_data(stock_name,start_date,end_date):
    data = yf.download(stock_name, start=start_date, end=end_date)
    #data = data.set_index(pd.Index(range(1,len(data)+1)))
    #data['Date'] = pd.to_datetime(data['Date'])
    data["Difference"] = data["Open"] - data["Close"] #difference between Open and Close
    data["Price percentage change"] = data["Difference"] / data["Open"] * 100
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
    
    file_path_before_rolling = "../../data/" + stock_name + "_" + start_date[:4] + "_before.csv"   
    file_path_after_rolling = "../../data/" + stock_name + "_" + start_date[:4] + "_after.csv"   
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
    fig, axes = plt.subplots(2,2,figsize = (20,20))
    #plot Close value for both data
    axes[0][0].set_xlabel("Date")
    axes[0][0].set_ylabel("Stock Price")
    axes[0][0].set_title("Close")
    axes[0][0].plot(data.index, data.loc[:,"Close"], color = "red", label = "raw")
    axes[0][0].plot(data_ma.index, data_ma.loc[:,"Close"], color = "blue", label = "moving_avg")
    axes[0][0].legend(loc="upper left")

    #plot Volume
    axes[0][1].set_xlabel("Date")
    axes[0][1].set_ylabel("Volume Change")
    axes[0][1].set_title("Volume Change")
    axes[0][1].plot(data.index, data.loc[:,"Volume_change"], color = "black", label = "raw")
    axes[0][1].legend(loc="upper left")

    #plot price percentage change
    axes[1][0].set_xlabel("Volume Difference")
    axes[1][0].set_ylabel("Price Percent Change")
    axes[1][0].set_title("Price Percent Change")
    axes[1][0].scatter(data.loc[:,"Volume_change"], data.loc[:,"Price percentage change"], marker = "o", color = "black", label = "raw")

    #plot price
    axes[1][1].set_xlabel("Volume Difference")
    axes[1][1].set_ylabel("Price Change")
    axes[1][1].set_title("Price Change")
    axes[1][1].scatter(data.loc[:,"Volume_change"]**2, data.loc[:,"Difference"]**2, marker = "o", color = "r", label = "raw")
    
    plt.show()
    plt.savefig('../../data/plot.png')



def main():
    stock_name = 'AAPL'  # Example stock ticker
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    window_size = 5
    export_data(stock_name,start_date,end_date,window_size)
    #print(start_date[:4])

if __name__ == '__main__':
    main()