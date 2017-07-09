import numpy as np
import pandas as pd
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/conversion_data.csv")

def get_categorical_variables(df):
    return df[['country','new_user','source','converted']]

def get_numerical_variables(df):
    numerical = df._get_numeric_data().columns
    return list(numerical)

def get_numerical_variables_percentile(df):
    final = df[get_numerical_variables(df)]
    return final.describe()

def get_categorical_variables_modes(df):
    modes = get_categorical_variables(df).mode()
    return modes

def get_missing_values_count(df):
    df1 = df.apply(lambda x: sum(x.isnull()), axis=0)
    return pd.DataFrame(df1)


def plot_histogram_with_numerical_values(df):
    num_cols = get_numerical_variables(df)
    plt.figure(figsize=(15,6))
    plt.subplot(121)
    plt.title(num_cols[0])
    sns.distplot(df[num_cols[0]], color='yellow', fit=norm, kde=False)
    plt.subplot(122)
    plt.title(num_cols[1])
    sns.distplot(df[num_cols[1]], color='yellow', fit=norm, kde=False)
    plt.subplot(211)
    plt.title(num_cols[2])
    sns.distplot(df[num_cols[2]], color='yellow', fit=norm, kde=False)
    plt.subplot(212)
    plt.title(num_cols[3])
    sns.distplot(df[num_cols[3]], color='yellow', fit=norm, kde=False)
    plt.tight_layout()
    plt.show()

def plot_facet_box(df):
    plt.figure(figsize=(10,10))
    plt.subplot(221)
    plt.title('Age')
    sns.boxplot('converted','age',data=df)
    plt.subplot(222)
    plt.title('Total Pages Visited')
    sns.boxplot('converted','total_pages_visited',data=df)
    plt.tight_layout()
    plt.show()
