import pandas as pd
import matplotlib.pyplot as plt
def get_categorical_variables(df):
    result = []
    for i in df.columns:
        if df.loc[:,i].nunique() < 20:
            result.append(i)
    return result



def get_numerical_variables(df):
    cols = df._get_numeric_data().columns
    res=list(cols)
    return list((x for x in res if x not in get_categorical_variables(df)))


def get_numerical_variables_percentile(df):
    final = pd.DataFrame(columns = ['variable name','mean','median','25th percentile','50th percentile','75th percentile'])
    final = df[get_numerical_variables(df)]
    return final.describe()


def get_categorical_variables_modes(df):
    x = df[get_categorical_variables(df)].mode()
    # return x.to_dict(orient='records')
    return x


def get_missing_values_count(df):
    return pd.DataFrame(len(df.index) - df.count())


def plot_histogram_with_numerical_values(df):
    df_sub = df.loc[:,cols]
    sub_cols = list(df_sub.columns)
    col_length = len(sub_cols)
    for i in range(0,col_length):
        plt.figure(figsize=(30,10))
        plt.subplot(col_length,1,i+1)
        plt.hist(df_sub.loc[:,sub_cols[i]], bins=10)
        plt.title(sub_cols[i])
        plt.xlabel("Value")
        plt.ylabel(sub_cols[i])
        plt.show()


def plot_facet_box(df):
    df_sub = df.loc[:,get_numerical_variables(df)]
    sub_cols = list(df_sub.columns)
    df_sub.groupby(sub_cols).agg('sum').unstack(1).plot(kind='bar',subplots=True)
    plt.show()
    
