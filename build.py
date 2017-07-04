import pandas as pd

def get_categorical_variables(df):
    categorical_data = list(df[['country', 'new_user', 'source', 'converted']])
    return categorical_data


def get_numerical_variables(df):
    numerical_data = list(df[['age', 'total_pages_visited']])
    return numerical_data


def get_numerical_variables_percentile(df):
    return df.describe()


def get_categorical_variables_modes(df):
    return df[get_categorical_variables(df)].mode()

def get_missing_values_count(df):
    return pd.DataFrame(df.isnull().sum())


def plot_histogram_with_numerical_values(df):
    plt.hist(df['age'], color='r', bins=50)
    plt.hist(df['total_pages_visited'], color='b', bins=50)
    plt.xlabel('age')
    plt.ylabel('total_pages_visited')
    plt.show()


def plot_facet_box(df):
    pass
