import pandas as pd

def get_categorical_variables(df):
    #returning for now based on visual analysis
    return df[['country','new_user','source','converted']]


def get_numerical_variables(df):
    return pd.DataFrame._get_numeric_data(df)


def get_numerical_variables_percentile(df):
    df = pd.DataFrame._get_numeric_data(df)
    df = df.groupby('converted').describe()
    return df


def get_categorical_variables_modes(df):
    dfn = df[['country','new_user','source','converted']]
    df_mode =  dfn.mode()
    return df_mode

def get_missing_values_count(df):
    ndf = df.isnull().sum()
    ndf = pd.DataFrame(ndf)
    ndf2 = ndf.reset_index()
    ndf2 = ndf2.rename(columns={'index':'var_name',0:'missing_value_count'})
    return ndf2


def plot_histogram_with_numerical_values(df):
    age = df['age'].tolist()
    new_user = df['new_user'].tolist()
    total_pages_visited = df['total_pages_visited'].tolist()
    converted = df['converted'].tolist()

    fig, axes = plt.subplots(2, 2)

    axes[0,0].hist(age)
    axes[0,0].set_title('age')

    axes[0,1].hist(new_user)
    axes[0,1].set_title('new_user')

    axes[1,0].hist(total_pages_visited)
    axes[1,0].set_title('total_pages_visited')

    axes[1,1].hist(converted)
    axes[1,1].set_title('converted')

    plt.tight_layout()
    plt.show()


def plot_facet_box(df):
    list_of_columns = df.columns.values
    for col in list_of_columns:
        plt.boxplot(df[col])
        plt.title(col)
        plt.show()
