import pandas as pd
import datetime
##import pandas_datareader as web
##from pandas_datareader import data, wb
##import matplotlib.pyplot as plt
##from matplotlib import style

ogdf = pd.read_csv("edited5.csv")

#appends a weighted sum column
def concatSum(df, dict = {}, *args):
    for key, value in dict.items():
        print(df[key].head())
        df[key] = df1[key].apply(lambda x: x*value)
    dictlist = [key for key in dict.keys()]
    df["Sum"] = df[dictlist].sum(axis=1)

#merges the "Sum" column with the countries column"
def mergeTables(original, summed):
    sumdf = summed[["Sum"]].copy()
    cydf = original[["Country Code"]].copy()
    return pd.concat([cydf, sumdf], axis = 1)


d = {"Human Development Index (HDI)":0.2, "Life Expectancy at Birth":0.8}


df1 = ogdf.copy()
concatSum(df1, d)

new = mergeTables(ogdf, df1)
print(new)



