from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir+"../preprocessing")
import preprocessing

def linear_train(X_train, y_train, X_test, y_test):
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return y_pred, mse

    

