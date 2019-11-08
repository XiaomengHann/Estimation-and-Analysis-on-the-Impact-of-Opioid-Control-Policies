import pandas as pd
from fastparquet import ParquetFile
from tqdm import tqdm
import numpy as np
from datetime import datetime
import os

os.chdir('/Users/joseph.hsieh/Documents/Duke/Course Work/Fall 2019/IDS 690 - Practical Data Science 1/IDS690_team_project/by_state_parquet/')
# varify the path using getcwd()
cwd = os.getcwd()
# print the current directory
print("Current working directory is:", cwd)

arcos_fl.to_parquet('by_state_parquet/arcos_fl.parquet')
arcos_tx.to_parquet('by_state_parquet/arcos_tx.parquet')
arcos_wa.to_parquet('by_state_parquet/arcos_wa.parquet')
arcos_id.to_parquet('by_state_parquet/arcos_id.parquet')
arcos_or.to_parquet('by_state_parquet/arcos_or.parquet')
arcos_ga.to_parquet('by_state_parquet/arcos_ga.parquet')
arcos_al.to_parquet('by_state_parquet/arcos_al.parquet')
arcos_la.to_parquet('by_state_parquet/arcos_la.parquet')
arcos_nm.to_parquet('by_state_parquet/arcos_nm.parquet')

arcos_fl = pd.read_parquet('arcos_fl.parquet')
arcos['TRANSACTION_DATE'] = np.mod(arcos['TRANSACTION_DATE'],10000)
arcos.rename(columns={"BUYER_STATE":"STATE", "BUYER_COUNTY":"COUNTY","TRANSACTION_DATE":"YEAR"},inplace=True)
arcos.rename(columns={"TRANSACTION_DATE":"YEAR"},inplace=True)
arcos.head()


#arcos_fl.shape
''' couldn't get the .apply to run for the state.
arcos_t1 = arcos_fl.head(100)
arcos_t1
arcos_t1['TRANSACTION_DATE'] = arcos_t1['TRANSACTION_DATE'].apply(str)
arcos_t1
arcos_t1['TRANSACTION_DATE']
arcos_t1.apply(datetime.strptime(arcos_t1['TRANSACTION_DATE'],'%m%d%Y'))
'''


arcos_fl.to_parquet('by_state_parquet/arcos_fl.parquet')
datalist = list()
for row, date in enumerate(tdqm(arcos_fl['TRANSACTION_DATE'])):
    date_raw = str(date)
    date_object = datetime.strptime(date_raw, '%m%d%Y')
    #date_string = date_object.strftime('%m/%d/%Y')
    date_string = date_object.strftime('%Y')
    datalist.append(date_string)
arcos_fl['Year'] = pd.DataFrame(datalist)
arcos_fl = arcos_fl.drop(['TRANSACTION_DATE'], axis=1)
arcos_fl.rename(columns={"BUYER_STATE":"STATE", "BUYER_COUNTY":"COUNTY"},inplace=True)
arcos_fl.head()
arcos_fl.to_parquet('arcos_fl1.parquet')
arcos_fl1 = pd.read_parquet('arcos_fl1.parquet')

arcos_fl1_test = arcos_fl1.head(100)
arcos_fl1_test
arcos_fl1_test2 = arcos_fl1_test.groupby(['COUNTY','Year','DRUG_CODE','MME_Conversion_Factor','dos_str'], as_index=False).sum()
arcos_fl1_test2
FIPS_list = pd.read_csv('FIPS_list.csv')
FIPS_list
FIPS_list_FL = FIPS_list[FIPS_list['State'] == 'FL']
FIPS_list_FL.rename(columns={"Name":"COUNTY"},inplace=True)
FIPS_list_FL['COUNTY'] = FIPS_list_FL['COUNTY'].str.upper()
FIPS_list_FL['FIPS']
FIPS_list_FL
new_data = pd.merge(arcos_fl1_test2, FIPS_list_FL, on='COUNTY', how='left')
new_data
new_data[new_data['FIPS'] == 'nan']
