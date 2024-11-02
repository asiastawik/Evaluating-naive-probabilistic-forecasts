#first 190 days for betas
#make forecasts for last 8 days

import pandas as pd
import numpy as np

df = pd.read_csv('us_consumption.csv', sep='\t')

# Assumed model specification:
# Consumption = beta_0 + beta_1 * Income + beta_2 * Production

Y = df[['Consumption']].values
X1 = df[['Income', 'Production', 'Savings']].values #X1 and X2 and X3
X0 = np.ones(np.shape(Y))
X = np.concatenate((X0, X1), axis=1)  # Here we put explanatory variables for our model

X_in_sample = X[:-8]  # we'll use all data except the last observation for betas estimation
Y_in_sample = Y[:-8]

# This is our 'future' values of the explanatory variables - we'll use them for our estimation
# of Consumption value
X_future = X[-8:]

# This is real value of Consumption that we want to forecast
Y_future = Y[-8:]

arr1 = np.linalg.inv(np.dot(X_in_sample.T, X_in_sample)) #jak liczymy forecast i error to musimy dać X_in_sample, Y_in_sample
betas = np.dot(arr1, np.dot(X_in_sample.T, Y_in_sample))  #X.T is X transposed, X^(-1) is np.linalg.inv(X), X*Y is np.dot(X,Y) - matrix multiplication

# we estimated the parameters of the model, namely beta_0, beta_1 and beta_2
print(betas)
# we now know that our model looks like this:
# Consumption = 0.507022 + 0.184151 * Income + 0.193907 * Production
# Now we want to forecast the next value of Consumption (Y_future)
# We just have to put values from X_future to the equation above:

forecast = np.dot(X_future, betas)  # this is our forecast of Consumption
error = (forecast - Y_future) ** 2  # We compare this to real Consumption and calc. the error
print(len(forecast))
print(forecast)