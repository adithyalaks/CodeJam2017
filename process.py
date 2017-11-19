import pandas as pd
import csv
# this module will process data based on weights passed by users
# define generic functions that will calculate a custom index based on weights assigned by users
# generate a sorted list of tuples containing Country Name,Rank and Index 


def generateDict(file):
    with open(file, mode='r') as infile:
        global ccodes
        reader=csv.reader(infile)
        ccodes={rows[0]:rows[1] for rows in reader}

generateDict('dict.csv')
print(ccodes)

#TO-DO: actually generate df, a DataFrame
df.replace({'Country':cc.mydict})
