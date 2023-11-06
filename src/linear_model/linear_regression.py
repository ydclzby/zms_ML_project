from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Linear_model(object):
    def __init__(self, X_train, y_train):
        self._X_train = X_train
        self._y_train = y_train
        self._regr = LinearRegression().fit(X_train, y_train)
        
    def predict(self, X_test, y_test):
        self._pred = self._regr.predict(X_test)
        
    def plot(self):
        plt.plot(len)