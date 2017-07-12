import pandas as pd
def get_categorical_variables(df):

    return ['country', 'new_user', 'source', 'converted']


def get_numerical_variables(df):
    return ['age', 'total_pages_visited']


def get_numerical_variables_percentile(df):
    a = df.describe()
    new_a =  a.T
    new_a.drop(['count', 'std', 'min', 'max'], inplace = True, axis=1)

    new_a['variable name'] = new_a.index.values
    new_a['median'] = new_a['50%']
    new_a['25th percentile'] = new_a['25%']
    new_a['50th percentile'] = new_a['50%']
    new_a['75th percentile'] = new_a['75%']

    variable_percentile = pd.DataFrame(new_a, columns = ['variable name','mean','median','25th percentile', '50th percentile', '75th percentile'])
    return variable_percentile


def get_categorical_variables_modes(df):
    a = df.mode(axis = 0)
    return a


def get_missing_values_count(df):
    vals= []
    for cols in df.columns.values:
        vals.append(df[cols].isnull().sum())

    ndf = zip(df.columns.values,vals)

    miss = pd.DataFrame(ndf)
    missing = miss.rename(columns={"0":"var_name","1":"missing_value_count"})
    return missing


def plot_histogram_with_numerical_values(df):
    pass


def plot_facet_box(df):
    pass
