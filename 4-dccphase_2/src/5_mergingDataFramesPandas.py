# #--  --  --  -- Merging DataFrames with pandas
# # Used for Data Scientist Training Path 
# #FYI it's a compilation of how to work
# #with different commands.


# ### --------------------------------------------------------
# # # # ------>>>> Reading DataFrames from multiple files
# Import pandas
import pandas as pd
# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')
# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')
# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')
# Print the first five rows of gold
print(gold.head())


# ### --------------------------------------------------------
# # # # ------>>>> Reading DataFrames from multiple files in a loop
# Import pandas
import pandas as pd
# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']
# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))
# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())



# ### --------------------------------------------------------
# # # # ------>>>> Combining DataFrames from multiple data files
# Import pandas
import pandas as pd
# Make a copy of gold: medals
medals = gold.copy()
# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']
# Rename the columns of medals using new_labels
medals.columns = new_labels
# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']
# Print the head of medals
print(medals.head())


# ### --------------------------------------------------------
# # # # ------>>>> Sorting DataFrame with the Index & columns
# Import pandas
import pandas as pd
# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')
# Print the head of weather1
print(weather1.head())
# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()
# Print the head of weather2
print(weather2.head())
# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)
# Print the head of weather3
print(weather3.head())
# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')
# Print the head of weather4
print(weather4.head())



# ### --------------------------------------------------------
# # # # ------>>>> Reindexing DataFrame from a list
# Import pandas
import pandas as pd
# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)
# Print weather2
print(weather2)
# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()
# Print weather3
print(weather3)



# ### --------------------------------------------------------
# # # # ------>>>> Reindexing using another DataFrame Index
# Import pandas
import pandas as pd
# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)
# Print shape of common_names
print(common_names.shape)
# Drop rows with null counts: common_names
common_names = common_names.dropna()
# Print shape of new common_names
print(common_names.shape)



# ### --------------------------------------------------------
# # # # ------>>>>Adding unaligned DataFrames
# The DataFrames january and february, which have 
# been printed in the IPython Shell, represent the 
# sales a company made in the corresponding months.

# The Indexes in both DataFrames are called Company, 
# identifying which company bought that quantity of
#  units. The column Units is the number of units sold.

# If you were to add these two DataFrames by 
# executing the command total = january + february,
#  how many rows would the resulting DataFrame have?
#  Try this in the IPython Shell and find out for yourself.
total = january + february
total
# R/ 6 rows.



# ### --------------------------------------------------------
# # # # ------>>>> Broadcasting in arithmetic formulas
# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]
# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9
# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F', 'C')
# Print first 5 rows of temps_c
print(temps_c.head())



# ### --------------------------------------------------------
# # # # ------>>>> Computing percentage growth of GDP
import pandas as pd
# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv', parse_dates=True, index_col='DATE')
# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008':]
# Print the last 8 rows of post2008
print(post2008.tail(8))
# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()
# Print yearly
print(yearly)
# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 100
# Print yearly again
print(yearly)



# ### --------------------------------------------------------
# # # # ------>>>> Converting currency of stocks
# Import pandas
import pandas as pd
# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date')
# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')
# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]
# Print the head of dollars
print(dollars.head())
# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'],axis='rows')
# Print the head of pounds
print(pounds.head())



# ### --------------------------------------------------------
# # # # ------>>>> Appending Series with nonunique Indices
# The Series bronze and silver, which have been printed in 
# the IPython Shell, represent the 5 countries that won the 
# most bronze and silver Olympic medals respectively between 
# 1896 & 2008. The Indexes of both Series are called 
# Country and the values are the corresponding number 
# of medals won.

# If you were to run the command combined = bronze.append(silver), 
# how many rows would combined have? And how many rows would 
# combined.loc['United States'] return? Find out for yourself
#  by running these commands in the IPython Shell.
combined = bronze.append(silver)
# R/ combined has 10 rows and combined.loc['United States'] has 2 rows.



# ### --------------------------------------------------------
# # # # ------>>>> Appending pandas Series
# Import pandas
import pandas as pd
# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv', parse_dates=True, index_col='Date')
# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv', parse_dates=True, index_col='Date')
# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv', parse_dates=True, index_col='Date')
# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']
# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']
# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']
# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)
# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
# Compute & print total sales in quarter1
print(quarter1.sum())



# ### --------------------------------------------------------
# # # # ------>>>> Concatenating pandas Series along row axis
# Initialize empty list: units
units = []
# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])
# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')
# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])


# ### --------------------------------------------------------
# # # # ------>>>> Appending DataFrames with ignore_index
# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981
# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index=True)
# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)
# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name'] == 'Morgan'])


# ### --------------------------------------------------------
# # # # ------>>>> Concatenating pandas DataFrames along column axis
# Create a list of weather_max and weather_mean
weather_list = [weather_max, weather_mean]
# Concatenate weather_list horizontally
weather = pd.concat(weather_list, axis=1)
# Print weather
print(weather)



# ### --------------------------------------------------------
# # # # ------>>>> Reading multiple files to build a DataFrame
#Initialize an empyy list: medals
medals =[]
for medal in medal_types:
    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    # Create list of column names: columns
    columns = ['Country', medal]
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)
    # Append medal_df to medals
    medals.append(medal_df)
# Concatenate medals horizontally: medals_df
medals_df = pd.concat(medals, axis='columns')
# Print medals_df
print(medals_df)



# ### --------------------------------------------------------
# # # # ------>>>> Concatenating vertically to get MultiIndexed rows
for medal in medal_types:
    file_name = "%s_top5.csv" % medal
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    # Append medal_df to medals
    medals.append(medal_df) 
# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])
# Print medals in entirety
print(medals)



# ### --------------------------------------------------------
# # # # ------>>>> Slicing MultiIndexed DataFrames
# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)
# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])
# Print data about silver medals
print(medals_sorted.loc['silver'])
# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice
# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'], :])



# ### --------------------------------------------------------
# # # # ------>>>> Concatenating horizontally to get MultiIndexed columns
# Concatenate dataframes: february
february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])
# Print february.info()
print(february.info())
# Assign pd.IndexSlice: idx
idx = pd.IndexSlice
# Create the slice: slice_2_8
slice_2_8 = february.loc['2015-2-2':'2015-2-8', idx[:, 'Company']]
# Print slice_2_8
print(slice_2_8)



# ### --------------------------------------------------------
# # # # ------>>>> Concatenating DataFrames from a dict
# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]
# Create an empty dictionary: month_dict
month_dict = {}
for month_name, month_data in month_list:
    # Group month_data: month_dict[month_name]
    month_dict[month_name] =  month_data.groupby('Company').sum()
# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)
# Print sales
print(sales)
# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])



# ### --------------------------------------------------------
# # # # ------>>>> Concatenating DataFrames with inner join
# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]
# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys=['bronze', 'silver', 'gold'], axis=1, join='inner')
# Print medals
print(medals)


# ### --------------------------------------------------------
# # # # ------>>>> Resampling & concatenating DataFrames with inner join
# Resample and tidy china: china_annual
china_annual = china.resample('A').last().pct_change(10).dropna()
# Resample and tidy us: us_annual
us_annual = us.resample('A').last().pct_change(10).dropna()
# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual, us_annual], join='inner', axis=1)
# Resample gdp and print
print(gdp.resample('10A').last())



# ### --------------------------------------------------------
# # # # ------>>>>Merging company DataFrames 
# Suppose your company has 
# operations in several 
# different cities under 
# several different managers. 
# The DataFrames revenue and 
# managers contain partial 
# information related to the 
# company. That is, the rows of 
# the city columns don't quite 
# match in revenue and 
# managers (the Mendocino 
# branch has no revenue yet 
# since it just opened and the 
# manager of Springfield branch 
# recently left the company). 

# The DataFrames have been 
# printed in the IPython Shell. 
# If you were to run the 
# command combined = pd.merge(
# revenue, managers, 
# on='city'), how many rows 
# would combined have?
combined = pd.merge(revenue, managers, on='city')
# R/ 2 rows

# ### --------------------------------------------------------
# # # # ------>>>> Merging on a specific column
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on='city')
# Print merge_by_city
print(merge_by_city)
# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on='branch_id')
# Print merge_by_id
print(merge_by_id)



# ### --------------------------------------------------------
# # # # ------>>>> Merging on columns with non-matching labels
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, left_on='city', right_on='branch')
# Print combined
print(combined)



# ### --------------------------------------------------------
# # # # ------>>>> Merging on multiple columns
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']
# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']
# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])
# Print combined
print(combined)



# ### --------------------------------------------------------
# # # # ------>>>> Joining by Index
# The DataFrames revenue and 
# managers are displayed in the 
# IPython Shell. Here, they are 
# indexed by 'branch_id'. 

# Choose the function call 
# below that will join the 
# DataFrames on their indexes 
# and return 5 rows with index 
# labels [10, 20, 30, 31, 47]. 
# Explore each of them in the 
# IPython Shell to get a better 
# understanding of their 
# functionality.
revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer')


# ### --------------------------------------------------------
# # # # ------>>>>Choosing a joining strategy 
# Suppose you have two 
# DataFrames: students (with 
# columns 'StudentID', 
# 'LastName', 'FirstName', and 
# 'Major') and midterm_results (
# with columns 'StudentID', 
# 'Q1', 'Q2', and 'Q3' for 
# their scores on midterm 
# questions). 

# You want to combine the 
# DataFrames into a single 
# DataFrame grades, and be able 
# to easily spot which students 
# wrote the midterm and which 
# didn't (their midterm 
# question scores 'Q1', 'Q2', & 
# 'Q3' should be filled with 
# NaN values). 

# You also want to drop rows 
# from midterm_results in which 
# the StudentID is not found in 
# students. 

# Which of the following 
# strategies gives the desired 
# result?
grades = pd.merge(students, midterm_results, how='left')
# R/A left join: grades = pd.merge(students, midterm_results, how='left')


# ### --------------------------------------------------------
# # # # ------>>>> Left & right merging on multiple columns
# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, how='right', on=['city', 'state'])
# Print revenue_and_sales
print(revenue_and_sales)
# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, how='left', left_on=['city', 'state'], right_on=['branch', 'state'])
# Print sales_and_managers
print(sales_and_managers)


# ### --------------------------------------------------------
# # # # ------>>>> Merging DataFrames with outer join
# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers, revenue_and_sales)
# Print merge_default
print(merge_default)
# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers, revenue_and_sales, how='outer')
# Print merge_outer
print(merge_outer)
# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales, on=['city', 'state'], how='outer')
# Print merge_outer_on
print(merge_outer_on)



# ### --------------------------------------------------------
# # # # ------>>>> Using merge_ordered()
# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin, houston)
# Print tx_weather
print(tx_weather)
# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'])
# Print tx_weather_suff
print(tx_weather_suff)
# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'], fill_method='ffill')
# Print tx_weather_ffill
print(tx_weather_ffill)



# ### --------------------------------------------------------
# # # # ------>>>> Using merge_asof()
# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')
# Print the tail of merged
print(merged.tail())
# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()
# Print yearly
print(yearly)
# print yearly.corr()
print(yearly.corr())



# ### --------------------------------------------------------
# # # # ------>>>> Loading Olympic edition DataFrame
#Import pandas
import pandas as pd
# Create file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'
# Load DataFrame from file_path: editions
editions =  pd.read_csv(file_path, sep='\t')
# Extract the relevant columns: editions
editions =  editions[['Edition', 'Grand Total', 'City', 'Country']]
# Print editions DataFrame
print(editions)


# ### --------------------------------------------------------
# # # # ------>>>> Loading IOC codes DataFrame
# Import pandas
import pandas as pd
# Create the file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'
# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)
# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]
# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())



# ### --------------------------------------------------------
# # # # ------>>>> Building medals DataFrame
# Import pandas
import pandas as pd
# Create empty dictionary: medals_dict
medals_dict = {}
for year in editions['Edition']:
    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)  
    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)    
    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]
    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict, ignore_index=True)
# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())


# ### --------------------------------------------------------
# # # # ------>>>> Counting medals by country/edition in a pivot table
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(aggfunc='count', index='Edition', values='Athlete', columns='NOC')
# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())


# ### --------------------------------------------------------
# # # # ------>>>> Computing fraction of medals per Olympic edition
# Set Index of editions: totals
totals = editions.set_index('Edition')
# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']
# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis='rows')
# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())



# ### --------------------------------------------------------
# # # # ------>>>> Computing percentage change in fraction of medals won
# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()
# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change() * 100
# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()
# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())



# ### --------------------------------------------------------
# # # # ------>>>> Building hosts DataFrame
# Import pandas
import pandas as pd
# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, ioc_codes, how='left')
# Extract relevant columns and set index: hosts
hosts =  hosts[['Edition','NOC']].set_index('Edition')
# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'
# Reset Index of hosts: hosts
hosts = hosts.reset_index()
# Print hosts
print(hosts)



# ### --------------------------------------------------------
# # # # ------>>>> Reshaping for analysis
# Import pandas
import pandas as pd
# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')
# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)
# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped.loc[reshaped.NOC == 'CHN']
# Print last 5 rows of chn with .tail()
print(chn.tail())



# ### --------------------------------------------------------
# # # # ------>>>> Merging to compute influence
# Import pandas
import pandas as pd
# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts, how='inner')
# Print first 5 rows of merged
print(merged.head())
# Set Index of merged and sort it: influence
influence =  merged.set_index('Edition').sort_index()
# Print first 5 rows of influence
print(influence.head())



# ### --------------------------------------------------------
# # # # ------>>>> Plotting influence of host country
# Import pyplot
import matplotlib.pyplot as plt
# Extract influence['Change']: change
change = influence['Change']
# Make bar plot of change: ax
ax = change.plot(kind='bar')
# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])
# Display the plot
plt.show()




