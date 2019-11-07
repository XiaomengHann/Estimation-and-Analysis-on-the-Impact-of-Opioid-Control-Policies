from fastparquet import ParquetFile
from datetime import datetime
from tqdm import tqdm
import pandas as pd
import numpy as np
import csv
import os
from glob import glob

os.chdir('/Users/joseph.hsieh/Documents/Duke/Course Work/Fall 2019/IDS 690 - Practical Data Science 1/IDS690_team_project/')
# varify the path using getcwd()
cwd = os.getcwd()
# print the current directory
print("Current working directory is:", cwd)
%pwd

arcos-ak-statewide-itemized.tsv.gz
arcos-in-statewide-itemized.tsv.gz
path_list = glob('By_State/*-in-*.gz')
state_list = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']
#filter down columns, took out 'DRUG_NAME', but may need to add it back after cleaning
col_vars = ['BUYER_STATE','BUYER_COUNTY','DRUG_CODE','TRANSACTION_DATE','CALC_BASE_WT_IN_GM','DOSAGE_UNIT','MME_Conversion_Factor','dos_str','QUANTITY']
FIPS_list = pd.read_csv('FIPS_list.csv')
FIPS_list.rename(columns={"Name":"COUNTY"},inplace=True)
FIPS_list['COUNTY'] = FIPS_list['COUNTY'].str.upper()
FIPS_list['State'] = FIPS_list['State'].str.lower()


for path in tqdm(path_list):
    iter_csv = pd.read_csv(path, iterator=True, chunksize=500000,delimiter = '\t',encoding = 'utf-8', usecols=(col_vars))

    #concationate the chunks together
    arcos_temp = pd.concat([chunk for chunk in tqdm(iter_csv)])
    #create a copy of the file
    #change transation date into year only
    arcos_temp['TRANSACTION_DATE'] = np.mod(arcos_temp['TRANSACTION_DATE'],10000)
    #rename columns
    arcos_temp.rename(columns={'BUYER_STATE':'STATE', 'BUYER_COUNTY':'COUNTY','TRANSACTION_DATE':'YEAR'},inplace=True)
    #generate MME_Str value by multiplying DEA's CALC_BASE_WT_IN_GM with the MME_Conversion_Factor
    arcos_temp['MME_Str'] = arcos_temp.loc[:,'CALC_BASE_WT_IN_GM'].astype(float)*arcos_temp.loc[:,'MME_Conversion_Factor'].astype(float)
    #drop intermediate columns
    arcos_temp = arcos_temp.drop(['QUANTITY','CALC_BASE_WT_IN_GM','DOSAGE_UNIT','MME_Conversion_Factor','dos_str'], axis=1)
    #groupby to collaspe files
    arcos_temp = arcos_temp.groupby(['STATE','COUNTY','YEAR'], as_index=False).sum()
    #write to file
    state = path.split('-')[1]
    arcos_temp.to_parquet(f'by_state_parquet/arcos_{state}.parquet', engine='fastparquet')



# #extra code
# arcos_id = arcos_id.groupby(['STATE','COUNTY','YEAR'], as_index=False).sum()
# #filter down FIPS list to state
# FIPS_list_id = FIPS_list[FIPS_list['State'] == 'id']
# #merge FIPS onto county
# arcos_id_w_FIPS = pd.merge(arcos_id, FIPS_list_id, on='COUNTY', how='left')
# #write to file
# arcos_id_w_FIPS.to_parquet('by_state_parquet/arcos_id.parquet', engine='fastparquet')
