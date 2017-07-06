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
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    # Histogram
    ax[0].hist(df['age'],color='yellow',bins=10,align='mid',normed=True)
    ax[1].hist(df['total_pages_visited'],color='yellow',bins=10,align='mid',normed=True)
    ax[0].set_xlabel('age')
    ax[1].set_xlabel('total_pages_visited')
    plt.tight_layout()
    # Normal Curve for age
    mu, std = norm.fit(df['age'])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 20)
    p = norm.pdf(x, mu, std)
    ax[0].plot(x, p, 'k', linewidth=2)
    # Normal Curve for total_pages_visited
    mu, std = norm.fit(df['total_pages_visited'])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 70)
    p = norm.pdf(x, mu, std)
    ax[1].plot(x, p, 'k', linewidth=2)
    plt.show()


def plot_facet_box(df):
    pass
