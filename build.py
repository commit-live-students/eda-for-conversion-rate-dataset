import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import operator
import matplotlib.pyplot as plt

df = pd.read_csv('data/conversion_data.csv')

def get_categorical_variables(df):
    return df[['country','source','new_user','converted']]


def get_numerical_variables(df):
    return df._get_numeric_data()


def get_numerical_variables_percentile(df):
    df_temp = get_numerical_variables(df)
    return df_temp.describe().T


def get_categorical_variables_modes(df):
    dic = {'converted':0, 'country':'', 'new_user':0, 'source':''}
    for col in df.mode().columns:
        dic[col] = df.mode()[col][0]
    return pd.DataFrame(dic.items(), columns=['var_name', 'mode'])

def get_missing_values_count(df):
    my_missing_value = pd.DataFrame(df.isnull().sum(), columns=['missing_value_count'])
    my_missing_value.index.name = 'var_name'
    return my_missing_value


def plot_histogram_with_numerical_values(df):
    fig, axes = plt.subplots(2, 2)
    df1 = get_numerical_variables(df)
    list_of_cols = df1.columns
    axes[0,0].hist(df[list_of_cols[0]])
    axes[0,0].set_title(list_of_cols[0])
    axes[0,1].hist(df[list_of_cols[1]])
    axes[0,1].set_title(list_of_cols[1])
    axes[1,0].hist(df[list_of_cols[2]])
    axes[1,0].set_title(list_of_cols[2])
    axes[1,1].hist(df[list_of_cols[3]])
    axes[1,1].set_title(list_of_cols[3])
    plt.tight_layout()
    plt.show()
    pass


def plot_facet_box(df):
    def plot_facet_box(df):
        list_of_cols = df.columns
        for col in list_of_cols:
            plt.boxplot(df[col], 1)
            plt.title(col)
            plt.show()
    pass
