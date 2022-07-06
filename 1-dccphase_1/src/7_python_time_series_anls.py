#--  --  --  -- Time Series Analysis in Python:
# Used for Data Scientist Training Path 
#FYI it's a compilation of how to work
#with different commands.

### --------------------------------------------------------
# # ------>>>>> A "Thin" Application of Time Series # 0
# Import pandas and plotting modules
import pandas as pd
import matplotlib.pyplot as plt
# Convert the date index to datetime
diet.index = pd.to_datetime(diet.index)


### --------------------------------------------------------
# # ------>>>>> A "Thin" Application of Time Series # 1
# Import pandas and plotting modules
# From previous step
diet.index = pd.to_datetime(diet.index)
# Plot the entire time series diet and show gridlines
diet.plot(grid=True)
plt.show()


### --------------------------------------------------------
# # ------>>>>> A "Thin" Application of Time Series # 2
# From previous step
diet.index = pd.to_datetime(diet.index)
# Slice the dataset to keep only 2012
diet2012 = diet['2012']
# Plot 2012 data
diet2012.plot(grid=True)
plt.show()


### --------------------------------------------------------
# # ------>>>>> Merging Time Series With Different Dates
# Import pandas
import pandas as pd
# Convert the stock index and bond index into sets
set_stock_dates = set(stocks.index)
set_bond_dates = set(bonds.index)
# Take the difference between the sets and print
print(set_stock_dates - set_bond_dates)
# Merge stocks and bonds DataFrames using join()
stocks_and_bonds = stocks.join(bonds, how='inner')


### --------------------------------------------------------
# # ------>>>>> Correlation of Stocks and Bonds
# Compute percent change using pct_change()
returns = stocks_and_bonds.pct_change()
# Compute correlation using corr()
correlation = returns['SP500'].corr(returns['US10Y'])
print("Correlation of stocks and interest rates: ", correlation)
# Make scatter plot
plt.scatter(returns['SP500'], returns['US10Y'])
plt.show()


### --------------------------------------------------------
# # ------>>>>> Flying Saucers Aren't Correlated to Flying Markets
# Compute correlation of levels
correlation1 = levels['DJI'].corr(levels['UFO'])
print("Correlation of levels: ", correlation1)
# Compute correlation of percent changes
changes = levels.pct_change()
correlation2 = changes['DJI'].corr(changes['UFO'])
print("Correlation of changes: ", correlation2)



### --------------------------------------------------------
# # ------>>>>>  Looking at a Regression's R-Squared
# Import the statsmodels module
import statsmodels.api as sm
# Compute correlation of x and y
correlation =  x.corr(y)
print("The correlation between x and y is %4.2f" %(correlation))
# Convert the Series x to a DataFrame and name the column x
dfx = pd.DataFrame(x, columns=['x'])
# Add a constant to the DataFrame dfx
dfx1 = sm.add_constant(dfx)
# Regress y on dfx1
result = sm.OLS(y, dfx1).fit()
# Print out the results and look at the relationship between R-squared and the correlation above
print(result.summary())


### --------------------------------------------------------
# # ------>>>>>  Match Correlation with Regression Output
# Here are four scatter plots, each showing a linear regression line and an R-squared:
# R/ Fig #3 supossed to be +0.9 of correlation but not in the options



### --------------------------------------------------------
# # ------>>>>>  A Popular Strategy Using Autocorrelation
# Convert the daily data to weekly data
MSFT = MSFT.resample(rule='w',how='last')
# Compute the percentage change of prices
returns = MSFT.pct_change()
# Compute and print the autocorrelation of returns
autocorrelation = returns['Adj Close'].autocorr()
print("The autocorrelation of weekly returns is %4.2f" %(autocorrelation))


### --------------------------------------------------------
# # ------>>>>>  Are Interest Rates Autocorrelated?
# Compute the daily change in interest rates 
daily_diff = daily_rates.diff()
# Compute and print the autocorrelation of daily changes
autocorrelation_daily = daily_diff['US10Y'].autocorr()
print("The autocorrelation of daily interest rate changes is %4.2f" %(autocorrelation_daily))
# Convert the daily data to annual data
yearly_rates = daily_rates.resample(rule='A', how='last')
# Repeat above for annual data
yearly_diff = yearly_rates.diff()
autocorrelation_yearly = yearly_diff['US10Y'].autocorr()
print("The autocorrelation of annual interest rate changes is %4.2f" %(autocorrelation_yearly))

### --------------------------------------------------------
# # ------>>>>>  Taxing Exercise: Compute the ACF
# Import the acf module and the plot_acf module from statsmodels
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
# Compute the acf array of HRB
acf_array = acf(HRB)
print(acf_array)
# Plot the acf function
plot_acf(HRB, alpha=1)
plt.show()

### --------------------------------------------------------
# # ------>>>>>  Are We Confident This Stock is Mean Reverting?
# Import the plot_acf module from statsmodels and sqrt from math
from statsmodels.graphics.tsaplots import plot_acf
from math import sqrt
# Compute and print the autocorrelation of MSFT weekly returns
autocorrelation = returns['Adj Close'].autocorr()
print("The autocorrelation of weekly MSFT returns is %4.2f" %(autocorrelation))
# Find the number of observations by taking the length of the returns DataFrame
nobs = len(returns)
# Compute the approximate confidence interval
conf = 1.96/sqrt(nobs)
print("The approximate confidence interval is +/- %4.2f" %(conf))
# Plot the autocorrelation function with 95% confidence intervals and 20 lags using plot_acf
plot_acf(returns, alpha=0.05, lags=20)
plt.show()

### --------------------------------------------------------
# # ------>>>>>  Can't Forecast White Noise
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
# Simulate wite noise returns
returns = np.random.normal(loc=0.02, scale=0.05, size=1000)
# Print out the mean and standard deviation of returns
mean = np.mean(returns)
std = np.std(returns)
print("The mean is %5.3f and the standard deviation is %5.3f" %(mean,std))
# Plot returns series
plt.plot(returns)
plt.show()
# Plot autocorrelation function of white noise returns
plot_acf(returns, lags=20)
plt.show()

### --------------------------------------------------------
# # ------>>>>>  Generate a Random Walk
# Generate 500 random steps with mean=0 and standard deviation=1
steps = np.random.normal(loc=0, scale=1, size=500)
# Set first element to 0 so that the first price will be the starting stock price
steps[0]=0
# Simulate stock prices, P with a starting price of 100
P = 100 + np.cumsum(steps)
# Plot the simulated stock prices
plt.plot(P)
plt.title("Simulated Random Walk")
plt.show()


### --------------------------------------------------------
# # ------>>>>>  Get the Drift
# Generate 500 random steps
steps = np.random.normal(loc=0.001, scale=0.01, size=500) + 1
# Set first element to 1
steps[0]=1
# Simulate the stock price, P, by taking the cumulative product
P = 100 * np.cumprod(steps)
# Plot the simulated stock prices
plt.plot(P)
plt.title("Simulated Random Walk with Drift")
plt.show()


### --------------------------------------------------------
# # ------>>>>>  Are Stock Prices a Random Walk?
# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller
# Run the ADF test on the price series and print out the results
results = adfuller(AMZN['Adj Close'])
print(results)
# Just print out the p-value
print('The p-value of the test on prices is: ' + str(results[1]))


### --------------------------------------------------------
# # ------>>>>>  How About Stock Returns?
# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller
# Create a DataFrame of AMZN returns
AMZN_ret = AMZN.pct_change()
# Eliminate the NaN in the first row of returns
AMZN_ret = AMZN_ret.dropna()
# Run the ADF test on the return series and print out the p-value
results = adfuller(AMZN_ret['Adj Close'])
print('The p-value of the test on returns is: ' + str(results[1]))


### --------------------------------------------------------
# # ------>>>>>  Is it Stationary?
# R/ A


### --------------------------------------------------------
# # ------>>>>>  Seasonal Adjustment During Tax Season
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
# Seasonally adjust quarterly earnings
HRBsa = HRB.diff(4)
# Print the first 10 rows of the seasonally adjusted series
print(HRBsa.head(10))
# Drop the NaN data in the first three three rows
HRBsa = HRBsa.dropna()
# Plot the autocorrelation function of the seasonally adjusted series
plot_acf(HRBsa)
plt.show()



### --------------------------------------------------------
# # ------>>>>>  Simulate AR(1) Time Series
# import the module for simulating data
from statsmodels.tsa.arima_process import ArmaProcess
# Plot 1: AR parameter = +0.9
plt.subplot(2,1,1)
ar1 = np.array([1, -0.9])
ma1 = np.array([1])
AR_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = AR_object1.generate_sample(nsample=1000)
plt.plot(simulated_data_1)
# Plot 2: AR parameter = -0.9
plt.subplot(2,1,2)
ar2 = np.array([1, 0.9])
ma2 = np.array([1])
AR_object2 = ArmaProcess(ar2, ma2)
simulated_data_2 = AR_object2.generate_sample(nsample=1000)
plt.plot(simulated_data_2)
plt.show()

### --------------------------------------------------------
# # ------>>>>> Compare the ACF for Several AR Time Series
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
# Plot 1: AR parameter = +0.9
plot_acf(simulated_data_1, alpha=1, lags=20)
plt.show()
# Plot 2: AR parameter = -0.9
plot_acf(simulated_data_2, alpha=1, lags=20)
plt.show()
# Plot 3: AR parameter = +0.3
plot_acf(simulated_data_3, alpha=1, lags=20)
plt.show()



### --------------------------------------------------------
# # ------>>>>> Match AR Model with ACF
#-> autoregression parameter - ar parameter
# Which figure corresponds to an AR(1) model with an AR parameter of -0.5?
# R/ D



### --------------------------------------------------------
# # ------>>>>> Estimating an AR Model
# You will estimate the AR(1) parameter, phi , of one of
# the simulated series that you generated in the earlier 
# exercise. Since the parameters are known for a simulated
# series, it is a good way to understand the estimation 
# routines before applying it to real data.
# For simulated_data_1 with a true  of 0.9, you will print out 
# the estimate of phi. In addition, you will also print out the entire 
# output that is produced when you fit a time series, so you can get
# an idea of what other tests and summary statistics are available in 
# statsmodels.
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA
# Fit an AR(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(1,0))
res = mod.fit()
# Print out summary information on the fit
print(res.summary())
# Print out the estimate for the constant and for phi
print("When the true phi=0.9, the estimate of phi (and the constant) are:")
print(res.params)


### --------------------------------------------------------
# # ------>>>>> Forecasting with an AR Model
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA
# Forecast the first AR(1) model
mod = ARMA(simulated_data_1, order=(1,0))
res = mod.fit()
res.plot_predict(start=990, end=1010)
plt.show()



### --------------------------------------------------------
# # ------>>>>> Let's Forecast Interest Rates
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA
# Forecast interest rates using an AR(1) model
mod = ARMA(interest_rate_data, order=(1,0))
res = mod.fit()
# Plot the original series and the forecasted series
res.plot_predict(start=0, end='2022')
plt.legend(fontsize=8)
plt.show()



### --------------------------------------------------------
# # ------>>>>> Compare AR Model with Random Walk
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
# Plot the interest rate series and the simulated random walk series side-by-side
fig, axes = plt.subplots(2,1)
# Plot the autocorrelation of the interest rate series in the top plot
fig = plot_acf(interest_rate_data, alpha=1, lags=12, ax=axes[0])
# Plot the autocorrelation of the simulated random walk series in the bottom plot
fig = plot_acf(simulated_data, alpha=1, lags=12, ax=axes[1])
# Label axes
axes[0].set_title("Interest Rate Data")
axes[1].set_title("Simulated Random Walk Data")
plt.show()



### --------------------------------------------------------
# Import the modules for simulating data and for plotting the PACF
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_pacf
# Simulate AR(1) with phi=+0.6
ma = np.array([1])
ar = np.array([1, -0.6])
AR_object = ArmaProcess(ar, ma)
simulated_data_1 = AR_object.generate_sample(nsample=5000)
# Plot PACF for AR(1)
plot_pacf(simulated_data_1, lags=20)
plt.show()
# Simulate AR(2) with phi1=+0.6, phi2=+0.3
ma = np.array([1])
ar = np.array([1, -0.6, -0.3])
AR_object = ArmaProcess(ar, ma)
simulated_data_2 = AR_object.generate_sample(nsample=5000)
# Plot PACF for AR(2)
plot_pacf(simulated_data_2, lags=20)
plt.show()



### --------------------------------------------------------
# # ------>>>>> Estimate Order of Model: Information Criteria
# Import the module for estimating an ARMA model
from statsmodels.tsa.arima_model import ARMA
# Fit the data to an AR(p) for p = 0,...,6 , and save the BIC
BIC = np.zeros(7)
for p in range(7):
    mod = ARMA(simulated_data_2, order=(p,0))
    res = mod.fit()
# Save BIC for AR(p)    
    BIC[p] = res.bic   
# Plot the BIC as a function of p
plt.plot(range(1,7), BIC[1:7], marker='o')
plt.xlabel('Order of AR Model')
plt.ylabel('Bayesian Information Criterion')
plt.show()



### --------------------------------------------------------
# # ------>>>>> Simulate MA(1) Time Series
# import the module for simulating data
from statsmodels.tsa.arima_process import ArmaProcess
# Plot 1: MA parameter = -0.9
plt.subplot(2,1,1)
ar1 = np.array([1])
ma1 = np.array([1, -0.9])
MA_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = MA_object1.generate_sample(nsample=1000)
plt.plot(simulated_data_1)
# Plot 2: MA parameter = +0.9
plt.subplot(2,1,2)
ar2 = np.array([1])
ma2 = np.array([1, 0.9])
MA_object2 = ArmaProcess(ar2, ma2)
simulated_data_2 = MA_object2.generate_sample(nsample=1000)
plt.plot(simulated_data_2)
# show
plt.show()



### --------------------------------------------------------
# # ------>>>>> Compute the ACF for Several MA Time Series - ex#0
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
# Plot 1: MA parameter = -0.9
plot_acf(simulated_data_1, lags=20)
plt.show()



### --------------------------------------------------------
# # ------>>>>> Compute the ACF for Several MA Time Series - ex#1
# Plot 2: MA parameter = 0.9
plot_acf(simulated_data_2, lags=20)
plt.show()


### --------------------------------------------------------
# # ------>>>>> Compute the ACF for Several MA Time Series - ex#2
# Plot 3: MA parameter = -0.3
plot_acf(simulated_data_3, lags=20)
plt.show()


### --------------------------------------------------------
# # ------>>>>> Match ACF with MA Model
# Here are four Autocorrelation plots:
# Which figure corresponds to an MA(1) model with an MA parameter of -0.5
# R/ D


### --------------------------------------------------------
# # ------>>>>> Estimating an MA Model
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA
# Fit an MA(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(0,1))
res = mod.fit()
# Print out summary information on the fit
print(res.summary())
# Print out the estimate for the constant and for theta
print("When the true theta=-0.9, the estimate of theta (and the constant) are:")
print(res.params)


### --------------------------------------------------------
# # ------>>>>> Forecasting with MA Model
# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA
# Forecast the first MA(1) model
mod = ARMA(simulated_data_1, order=(0,1))
res = mod.fit()
res.plot_predict(start=990, end=1010)
plt.show()



### --------------------------------------------------------
# # ------>>>>> High Frequency Stock Prices
# import datetime module
import datetime
# Change the first date to zero
intraday.iloc[0,0] = 0
# Change the column headers to 'DATE' and 'CLOSE'
intraday.columns = ['DATE','CLOSE']
# Examine the data types for each column
print(intraday.dtypes)
# Convert DATE column to numeric
intraday['DATE'] = pd.to_numeric(intraday['DATE'])
# Make the `DATE` column the new index
intraday = intraday.set_index('DATE')


### --------------------------------------------------------
# # ------>>>>> More Data Cleaning: Missing Data - ex#0
# Notice that some rows are missing
print("If there were no missing rows, there would be 391 rows of minute data")
print("The actual length of the DataFrame is:", len(intraday))


### --------------------------------------------------------
# # ------>>>>> More Data Cleaning: Missing Data - ex#1
# Everything
set_everything = set(range(391))
# The intraday index as a set
set_intraday = set(intraday.index)
# Calculate the difference
set_missing = set_everything - set_intraday
# Print the difference
print("Missing rows: ", set_missing)


### --------------------------------------------------------
# # ------>>>>> More Data Cleaning: Missing Data - ex#2
# Fill in the missing rows
intraday = intraday.reindex(range(391), method='ffill')


### --------------------------------------------------------
# # ------>>>>> More Data Cleaning: Missing Data - ex#3
# From previous step
intraday = intraday.reindex(range(391), method='ffill')
# Change the index to the intraday times
intraday.index = pd.date_range(start='2017-09-01 9:30', end='2017-09-01 16:00', freq='1min')
# Plot the intraday time series
intraday.plot(grid=True)
plt.show()


### --------------------------------------------------------
# # ------>>>>> Applying an MA Model
# Import plot_acf and ARMA modules from statsmodels
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_model import ARMA
# Compute returns from prices and drop the NaN
returns = intraday.pct_change()
returns = returns.dropna()
# Plot ACF of returns with lags up to 60 minutes
plot_acf(returns, lags=60)
plt.show()
# Fit the data to an MA(1) model
mod = ARMA(returns, order=(0,1))
res = mod.fit()
print(res.params)


### --------------------------------------------------------
# # ------>>>>> Equivalence of AR(1) and MA(infinity)
# import the modules for simulating data and plotting the ACF
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf
# Build a list MA parameters
ma = [0.8**i for i in range(30)]
# Simulate the MA(30) model
ar = np.array([1])
AR_object = ArmaProcess(ar, ma)
simulated_data = AR_object.generate_sample(nsample=5000)
# Plot the ACF
plot_acf(simulated_data, lags=30)
plt.show()



### --------------------------------------------------------
# # ------>>>>> A Dog on a Leash? (Part 1)
# Plot the prices separately
plt.subplot(2,1,1)
plt.plot(7.25*HO, label='Heating Oil')
plt.plot(NG, label='Natural Gas')
plt.legend(loc='best', fontsize='small')
# Plot the spread
plt.subplot(2,1,2)
plt.plot(7.25*HO-NG, label='Spread')
plt.legend(loc='best', fontsize='small')
plt.axhline(y=0, linestyle='--', color='k')
plt.show()


### --------------------------------------------------------
# # ------>>>>> A Dog on a Leash? (Part 2)
# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller
# Compute the ADF for HO and NG
result_HO = adfuller(HO['Close'])
print("The p-value for the ADF test on HO is ", result_HO[1])
result_NG = adfuller(NG['Close'])
print("The p-value for the ADF test on NG is ", result_NG[1])
# Compute the ADF of the spread
result_spread = adfuller(7.25 * HO['Close'] - NG['Close'])
print("The p-value for the ADF test on the spread is ", result_spread[1])


### --------------------------------------------------------
# # ------>>>>> Are Bitcoin and Ethereum Cointegrated?
# Import the statsmodels module for regression and the adfuller function
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
# Regress BTC on ETH
ETH = sm.add_constant(ETH)
result = sm.OLS(BTC,ETH).fit()
# Compute ADF
b = result.params[1]
adf_stats = adfuller(BTC['Price'] - b*ETH['Price'])
print("The p-value for the ADF test is ", adf_stats[1])
# The data suggests that Bitcoin and Ethereum are cointegrated



### --------------------------------------------------------
# # ------>>>>> Is Temperature a Random Walk (with Drift)?
# Import the adfuller function from the statsmodels module
from statsmodels.tsa.stattools import adfuller
# Convert the index to a datetime object
temp_NY.index = pd.to_datetime(temp_NY.index, format='%Y')
# Plot average temperatures
temp_NY.plot()
plt.show()
# Compute and print ADF p-value
result = adfuller(temp_NY['TAVG'])
print("The p-value for the ADF test is ", result[1]) 


### --------------------------------------------------------
# # ------>>>>>  Getting "Warmed" Up: Look at Autocorrelations
# Import the modules for plotting the sample ACF and PACF
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# Take first difference of the temperature Series
chg_temp = temp_NY.diff()
chg_temp = chg_temp.dropna()
# Plot the ACF and PACF on the same page
fig, axes = plt.subplots(2,1)
# Plot the ACF
plot_acf(chg_temp, lags=20, ax=axes[0])
# Plot the PACF
plot_pacf(chg_temp, lags=20, ax=axes[1])
plt.show()


### --------------------------------------------------------
# # ------>>>>> Which ARMA Model is Best?
# Import the module for estimating an ARMA model
from statsmodels.tsa.arima_model import ARMA
# Fit the data to an AR(1) model and print AIC:
mod_ar1 = ARMA(chg_temp, order=(1,0))
res_ar1 = mod_ar1.fit()
print("The AIC for an AR(1) is: ", res_ar1.aic)
# Fit the data to an AR(2) model and print AIC:
mod_ar2 = ARMA(chg_temp, order=(2,0))
res_ar2 = mod_ar2.fit()
print("The AIC for an AR(2) is: ", res_ar2.aic)
# Fit the data to an ARMA(1,1) model and print AIC:
mod_arma11 = ARMA(chg_temp, order=(0,1))
res_arma11 = mod_arma11.fit()
print("The AIC for an ARMA(1,1) is: ", res_arma11.aic)



### --------------------------------------------------------
# # ------>>>>> Don't Throw Out That Winter Coat Yet
# Import the ARIMA module from statsmodels
from statsmodels.tsa.arima_model import ARIMA
# Forecast temperatures using an ARIMA(1,1,1) model
mod = ARIMA(temp_NY, order=(1,1,1))
res = mod.fit()
# Plot the original series and the forecasted series
res.plot_predict(start='1872-01-01', end='2046-01-01')
plt.show()



