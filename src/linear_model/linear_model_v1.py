from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


sys.path.append("../preprocessing")
import preprocessing

def linear_train(X_train, y_train, X_test, y_test):
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return y_pred, mse


def polynomial_transform(x, d, include_bias=False):
    # Start with an array of ones (for bias term) or an empty array
    z = np.ones((len(x), 1)) if include_bias else np.empty((len(x), 0))

    # Iterate through polynomial degrees
    for i in range(1, d + 1):
        new_column = x ** i
        z = np.column_stack((z, new_column))

    return z

def regression_transform(x, y,x_test, y_test, d, include_bias):
    x_transformed = polynomial_transform(x,d,include_bias)
    x_test_transformed = polynomial_transform(x_test,d,include_bias)
    regr = LinearRegression()
    regr.fit(x_transformed, y)
    
    y_pred = regr.predict(x_test_transformed)

    mse = mean_squared_error(y_test, y_pred)

    plt.figure(figsize=(5, 4))
    plt.title(f'degree {d}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_test, y_test, c='b', label='Actual')
    plt.plot(x_test,y_pred, c='r', label='predict')
    plt.legend(loc='upper left')
    plt.savefig("../../data/degree_" +str(d) + ".png")
    print(f"degree{d} \t MSE = {mse}")


def main():
    stock_name = 'AAPL'
    data_2020 = preprocessing.get_original_data(stock_name, '2020-01-01', '2020-12-31')
    data_2021 = preprocessing.get_original_data(stock_name, '2021-01-01', '2021-12-31')
    data_2020_processed = preprocessing.calculate_moving_average(data_2020, 5)
    data_2021_processed = preprocessing.calculate_moving_average(data_2021, 5)
    y_train = np.array(data_2020_processed.loc[:, "Difference"])
    X_train = np.array(range(0,len(y_train)))
    y_test = np.array(data_2021_processed.loc[:, "Difference"])
    X_test = np.array(range(len(y_train), len(y_train)+len(y_test)))
    for i in range(1, 100):
        regression_transform(X_train, y_train,X_test, y_test, i, False)

    
if __name__ == '__main__':
    main()
        
    

