import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/conversion_data.csv')
#print df.head(10)




def get_categorical_variables(df):
    col_names = df.columns.values
    ls = []
    for ele in col_names:
        #print df[ele].value_counts().index
        if len(df[ele].value_counts().index)<10:
            #print("{} is a categorical column as it has only {} categories\n".format(ele,len(df[ele].value_counts().index)))
            ls.append(ele)
    df2 = pd.DataFrame(df,columns=ls)
    #print df.info()
    return df2



def get_numerical_variables(df):
    col_names = df.columns.values
    ls = []
    for ele in col_names:
        if (df[ele].dtype == 'int64' or df[ele].dtype == 'float64') & (ele not in get_categorical_variables(df).columns.values):
            ls.append(ele)
    df2 = pd.DataFrame(df,columns=ls)
    return df2




def get_numerical_variables_percentile(df):
    df_1 = get_numerical_variables(df)
    dic1 =  df_1.describe().values
    ls = zip(*dic1)
    df_2 = pd.DataFrame(ls,columns=['count','mean','std','min','25th Percentile','50th Percentile','75th Percentile','max'])
    ls2 = ['age','total_pages_visited']
    df_2['variable name']=ls2
    df_2 = df_2[['variable name','mean','25th Percentile','50th Percentile','75th Percentile']]
    df_2['median'] = df_2['50th Percentile']
    df_2 = df_2[['variable name','mean','median','25th Percentile','50th Percentile','75th Percentile']]
    return df_2


def get_categorical_variables_modes(df):
    df_3 = get_categorical_variables(df)
    dic = {}
    for ele in df_3.columns.values:
        #print('mode of {} is {}'.format(ele,df_3[ele].mode().values[0]))
        if ele not in dic:
            dic[ele] = df_3[ele].mode().values[0]
    print dic
    df_x = pd.DataFrame(dic,index=[0],columns=dic.keys())
    return df_x


def get_missing_values_count(df):
    cols = df.columns.values
    cnt = 0
    df_tmp = df
    col_ls = []
    val_ls = []
    for col in cols:
        col_ls.append(col)
        for e in df[col].values:
            if pd.isnull(e) == True:
                cnt+=1
        val_ls.append(cnt)
        cnt = 0
    print zip(col_ls,val_ls)
    dfz = pd.DataFrame([col_ls,val_ls])
    dfz =  dfz.T
    dfz.rename(columns={0:'var_name',1:'missing_value_count'},inplace=True)
    return dfz


def plot_histogram_with_numerical_values(df):
    pass


def plot_facet_box(df):
    pass
