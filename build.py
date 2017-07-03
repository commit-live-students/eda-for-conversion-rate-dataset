import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import pandas as pd

def get_categorical_variables(df):
    df['new_user'] = df['new_user'].astype('category')
    df['converted'] = df['converted'].astype('category')
    cat_cols = df.select_dtypes(include=['object','category']).columns
    return cat_cols


def get_numerical_variables(df):
    df['new_user'] = df['new_user'].astype('category')
    df['converted'] = df['converted'].astype('category')
    num_cols = df.select_dtypes(exclude=['object','category']).columns
    return num_cols

def get_numerical_variables_percentile(df):
    df['new_user'] = df['new_user'].astype('category')
    df['converted'] = df['converted'].astype('category')
    num_cols = df.select_dtypes(exclude=['object','category']).columns
    return df[num_cols].describe()


def get_categorical_variables_modes(df):
    df['new_user'] = df['new_user'].astype('category')
    df['converted'] = df['converted'].astype('category')
    cat_cols = df.select_dtypes(include=['object','category']).columns
    return df[cat_cols].mode()


def get_missing_values_count(df):
    return pd.isnull(df).sum().reset_index()

def plot_histogram_with_numerical_values(df):
    df['new_user'] = df['new_user'].astype('category')
    df['converted'] = df['converted'].astype('category')
    num_cols = df.select_dtypes(exclude=['object','category']).columns
    plt.subplot(121)
    plt.title(num_cols[0])
    sns.distplot(df[num_cols[0]], color='yellow', fit=norm, kde=False)
    plt.subplot(122)
    plt.title(num_cols[1])
    sns.distplot(df[num_cols[1]], color='yellow', fit=norm, kde=False)

def plot_facet_box(df):
    plt.subplot(121)
    sns.boxplot('converted','age',data=df)
    plt.subplot(122)
    sns.boxplot('converted','total_pages_visited',data=df)
