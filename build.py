import numpy as np
import pandas as pd
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline


# we check if the dataframe has been created successfully or not by using the head function,
# which shows the first 5 rows of the dataframe.
df = pd.read_csv("data/conversion_data.csv")
df.head(100)

# Check the info() of the df
# This provides a concise summary of your data frame
df.info()

# Question 1: Function that returns a list of the names of categorical variables

print "list of the names of categorical variables :"
def get_categorical_variables(df):
    return df[['country','new_user','source','converted']]

get_categorical_variables(df)
# Output: list of the names of categorical variables :
#        ['country', 'new_user', 'source', 'converted']

# Question 2: Function that returns the list of the names of numeric variables

print "The list of the names of numeric variables :"
def get_numerical_variables(df):
    numerical = df._get_numeric_data().columns
    return list(numerical)

# get_numerical_variables(df)
# Output: The list of the names of numeric variables :
#         ['age', 'total_pages_visited']

# Question 3: Function that returns, for numeric variables, mean, median, 25, 50, 75th percentile

def get_numerical_variables_percentile(df):
    final = df[get_numerical_variables(df)]

    return final.describe()

# get_numerical_variables_percentile(df)
# Output:                 count 	 mean 	   std 	       min 	  25% 	50%   75% 	max
#  age 	                316200.0   30.569858   8.271802    17.0   24.0 	30.0  36.0 	123.0
# total_pages_visited 	316200.0   4.872966    3.341104    1.0 	  2.0 	4.0   7.0 	29.0

# Question 4: For categorical variables, get modes

def get_categorical_variables_modes(df):

    modes = get_categorical_variables(df).mode()
    return modes

# get_categorical_variables_modes(df)
# Output:  	country  new_user  source  converted
#        0 	  US 	    1 	    Seo 	  0

# Question 5: For each column, list the count of missing values

print "Missing values per column:"
def get_missing_values_count(df):
    df1 = df.apply(lambda x: sum(x.isnull()), axis=0)
    return pd.DataFrame(df1)

# get_missing_values_count(df)
# Output:  	0
#        country 	            0
#         age 	                0
#       new_user 	            0
#        source 	            0
#       total_pages_visited 	0
#         converted 	        0

# Question 6: Plot histograms using different subplots of all the numerical values in a single plot

def plot_histogram_with_numerical_values(df):

    num_cols = get_numerical_variables(df)
    #num_cols = df.select_dtypes(exclude=['object','category']).columns

    plt.figure(figsize=(15,6))
    plt.subplot(121)
    plt.title(num_cols[0])
    sns.distplot(df[num_cols[0]], color='yellow', fit=norm, kde=False)
    plt.subplot(122)
    plt.title(num_cols[1])
    sns.distplot(df[num_cols[1]], color='yellow', fit=norm, kde=False)

# plot_histogram_with_numerical_values(df)

# Question 7: Plot facet box plots to check out the distribution according to the target variable

def plot_facet_box(df):
    plt.figure(figsize=(15,5))
    plt.subplot(221)
    sns.boxplot('converted','age',data=df)
    plt.subplot(222)
    sns.boxplot('converted','total_pages_visited',data=df)

# plot_facet_box(df)
