import pandas as pd
import operator
def load_data():
    df = pd.read_csv("./data/conversion_data.csv")
    return df

def get_categorical_variables(df):
    #return df[['country','new_user','source','converted']]
    key = []
    values = []
    dic = {}
    delta_limit = 20

    for cols in list(df.columns):
        dic[cols] = len(df[cols].unique())

    dic_sorted = sorted(dic.items(), key=operator.itemgetter(1))

    for k,v in dic_sorted:
        key.append(k)
        values.append(v)

    for i in range(len(values)-1):
        next_delta = values[i+1] - values[i] / values[i] #measure the increase in value

        if next_delta > delta_limit:
            return df[key[:i+1]]


def get_numerical_variables(df):
    df_numeric = pd.DataFrame._get_numeric_data(df)
    return list(df_numeric)


def get_numerical_variables_percentile(df):
    return df.describe().transpose()


def get_categorical_variables_modes(df):
    df_cat = df[['country','new_user','source','converted']]
    df_mode =  df_cat.mode()
    return df_mode

def get_missing_values_count(df):
     ans_df = pd.DataFrame(df[df.isnull()].count(), columns=['missing_value_count'])
     return ans_df


def plot_histogram_with_numerical_values(df):
    pass


def plot_facet_box(df):
    pass

df = load_data()
get_categorical_variables(df)
#get_numerical_variables_percentile(df)
