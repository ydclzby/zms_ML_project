import pandas as pd

from preprocessing import get_original_data


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
    print(data_ma.iloc[20:].head()
          )  # Skip the first 20 rows and print the next 5 rows

    # For large dataframe, export to a CSV file
    # data_ma.to_csv('data_with_moving_averages.csv')


if __name__ == '__main__':
    main()
