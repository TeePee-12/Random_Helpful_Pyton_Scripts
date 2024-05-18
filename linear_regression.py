# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:54:10 2021

@author: Thomas Phelan

Performs linear regression calculations on a set of data
All input happens in the last cell.
Run last cell cell only
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#%%
def makedf(Filename, sigfigs=7):
    """
    Builds the dataframe, rounding off numbers to desired sig figs

    """
    if Filename[-3:] == 'txt':
        df = (pd.read_csv(Filename, delimiter = "\t"))
    elif Filename[-3:] == 'csv':
        df = (pd.read_csv(Filename))
    else:
        assert Filename[-3:] == 'csv' or Filename[-3:] == 'txt', 'Only Accepts .TXT or .CSV'
    for i in (range(len(df.columns))):
        for j in (range(len(df))):
            df.iat[j,i] = round(df.iat[j,i], sigfigs)
    return(df)    

#%%
def linreg(Filename, df, a, b):
    '''
    Calculates Linear regression mathematically then verifies with scipy

    '''
    x = np.array(df[a]) 
    y = np.array(df[b])
    n = np.size(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_mean,y_mean 
    Sxy = np.sum(x*y)- n*x_mean*y_mean
    Sxx = np.sum(x*x)-n*x_mean*x_mean  
    b1 = Sxy/Sxx
    b0 = y_mean-b1*x_mean
    print('===============================================')
    print('Mathematical results for plotting')
    print('slope is', b1)
    print('Y intercept is', b0)
    print('===============================================')
        
    #SciPy verification
    x = x.reshape(-1,1)
    y = y.reshape(-1,1)
    regression_model = LinearRegression()  
    regression_model.fit(x, y)
    y_predicted = regression_model.predict(x) 
    mse=mean_squared_error(y,y_predicted)
    rmse = np.sqrt(mean_squared_error(y, y_predicted))
    r2 = r2_score(y, y_predicted)
    print('===============================================')
    print('Scipy Verification of data:')
    print('Slope:' ,regression_model.coef_)
    print('Intercept:', regression_model.intercept_)
    print('MSE:',mse)
    print('Root mean squared error: ', rmse)
    print('R2 score: ', r2)
    print('===============================================')
    print()
    return(x, y, b0, b1)

#%%
def makeplot(x, y, b0, b1, title, xlabel, ylabel):
    '''
    Makes a scatter plot of datapoints with a linear regression
    '''
    plt.scatter(x, y, color='gray')
    plt.plot(x, y , linestyle='--')
    plt.title(title, fontsize=10)
    plt.xlabel(xlabel,fontsize=8)
    plt.ylabel(ylabel,fontsize=8)
    
    #plt.xlim(0)
    #plt.ylim(0,b0)
    
    plt.grid()
    
    plt.savefig(title+".png")
    plt.show()

#%%
def doit(Filename, a, b, title, xlabel, ylabel):
    df = makedf(Filename)
    x, y, b0, b1 = linreg(Filename,df, a, b)
    makeplot(x, y, b0, b1, title, xlabel, ylabel)

#%%
'''INPUT DATA HERE'''
#Filename is where your data is stored in the working directory
Filename = 'lab2_vin_vs_vout.csv'

#a Is the index or name label of the data column to be read on the x axis
a = 'Vin'

#b Is the index or name label of the data column to be read on the y axis
b = 'Vout'

#Title, xlabel, ylael will be printed on the plot
title = 'Linear operation, and saturation of TL071 Op Amp with Vcc = 5V and Gain = 3'
xlabel = 'Vin (Volts)'
ylabel = 'Vout (Volts)'

'''END USER INPUT, NOW RUN THIS CELL'''

doit(Filename, a, b, title, xlabel, ylabel)    
