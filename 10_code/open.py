import pandas as pd
import csv
    
df = pd.read_csv('arcos_all_washpost.tsv', delimiter = "\t", nrows = 300, encoding = 'utf-8')

df.head(10)
df.BUYER_NAME.head()
for i in df:
    print(i)