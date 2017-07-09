import pandas as pd
df = pd.read_csv('data/conversion_data.csv')

def get_categorical_variables(df):
    df['converted'] = df['converted'].astype('category')
    df['new_user'] = df['new_user'].astype('category')
    return df.select_dtypes(include=['category','object']).columns

def get_numerical_variables(df):
    df['converted'] = df['converted'].astype('category')
    df['new_user'] = df['new_user'].astype('category')
    return df.select_dtypes(exclude=['category','object']).columns

def get_numerical_variables_percentile(df):
    df['converted'] = df['converted'].astype('category')
    df['new_user'] = df['new_user'].astype('category')
    var = df.select_dtypes(exclude=['category','object'])
    return var.describe()


def get_categorical_variables_modes(df):
    df['converted'] = df['converted'].astype('category')
    df['new_user'] = df['new_user'].astype('category')
    var = df.select_dtypes(include=['category','object'])
    return var.mode()


def get_missing_values_count(df):
    return df.isnull()


def plot_histogram_with_numerical_values(df):
    return df.plot.hist()


def plot_facet_box(df):
    return df.plot.box()
