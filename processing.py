## This module deals with computing a single or multidimensional index given an input provided by the user
## in gui.py of this project.

import pandas as pd
import datetime
import numpy
import math
##import pandas_datareader as web
##from pandas_datareader import data, wb
##import matplotlib.pyplot as plt
##from matplotlib import style

ogdf = pd.read_csv("edited5.csv")

def indicator_list():
    name_list = ogdf.Indicator_Name.unique()
    return name_list.tolist()

def computeIndex(year,dictionary):
    df1=ogdf.copy()
    df2=pd.DataFrame(columns=['Country_Code','Index'])
    df1=df1[df1['Indicator_Name'].isin(list(dictionary.keys()))]

    
    df1['Status']='N'
 
    for i in range(5):
        weight = dictionary[df1.at[df1.index[214*i],'Indicator_Name']]
        for j in range(214):
            if weight == 0:
                df1.at[df1.index[214*i + j],'Status'] = 'Z'
            df1.at[df1.index[214*i + j],year]= df1.at[df1.index[214*i + j],year]*weight

    df1 = df1.sort_values('Country_Code')    
    for i in range(214):
        Country_Code = df1.at[df1.index[5*i],'Country_Code']
        index = 0
        for j in range(5):
            if (not(df1.at[df1.index[5*i + j],year] > 0) or math.isnan(df1.at[df1.index[5*i + j],year])) and (df1.at[df1.index[5*i + j],'Status'] != 'Z'):
                index = 0
                break
            else:
                if math.isnan(df1.at[df1.index[5*i + j],year]):
                    continue
                index += df1.at[df1.index[5*i + j],year]

        df2 = df2.append({'Country_Code': Country_Code,'Index':index},ignore_index=True)
        df2.to_csv("index.csv")
            
##year = '2010'
##dictionary = {'GNI per capita, Atlas method (current US$)':0.00, 'Incidence of tuberculosis (per 100,000 people)':0.00, 'Unemployment, male (% of male labor force)':0.00,'Life expectancy at birth, total (years)':0.20,'Survival to age 65, female (% of cohort)':0.00}
##computeIndex(year,dictionary)
    
    

#appends a weighted sum column
##def concatSum(df, dict = {}, *args):
##    for key, value in dict.items():
##        print(df[key].head())
##        df[key] = df1[key].apply(lambda x: x*value)
##    dictlist = [key for key in dict.keys()]
##    df["Sum"] = df[dictlist].sum(axis=1)

##
###merges the "Sum" column with the countries column"
##def mergeTables(original, summed):
##    sumdf = summed[["Sum"]].copy()
##    cydf = original[["Country Code"]].copy()
##    return pd.concat([cydf, sumdf], axis = 1)
##
##
##d = {"Human Development Index (HDI)":0.2, "Life Expectancy at Birth":0.8}
##
##
##df1 = ogdf.copy()
##concatSum(df1, d)
##
##new = mergeTables(ogdf, df1)
##print(new)

##if __name__ == '__main__':
##    print(indicator_list())
