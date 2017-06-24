import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_categorical_variables(df):

    return df.iloc[:,[0, 2, 3, 5]]


def get_numerical_variables(df):

    return pd.DataFrame._get_numeric_data(df)


def get_numerical_variables_percentile(df):

    df = get_numerical_variables(df)
    res_df = df.describe()
    res_df = res_df.transpose()
    variable_name = list(res_df.index)
    res_df['variable name'] = variable_name
    return res_df


def get_categorical_variables_modes(df):

    df = get_categorical_variables(df)
    dic = {'converted':0, 'country':'', 'new_user':0, 'source':''}
    for col in df.mode().columns:
        dic[col] = df.mode()[col][0]
    return pd.DataFrame(dic.items(), columns=['var_name', 'mode'])


def get_missing_values_count(df):

    ans_df = pd.DataFrame(df[df.isnull()].count(), columns=['missing_value_count'])
    ans_df.index.name = 'var_name'
    return ans_df


def plot_histogram_with_numerical_values(df):

    fig, axes = plt.subplots(2, 2)

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


def plot_facet_box(df):

    for col in list_of_cols:
        plt.boxplot(df[col], 1)
        plt.title(col)
        plt.show()
