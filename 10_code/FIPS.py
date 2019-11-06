import pandas as pd
import numpy as np
import csv
import os

os.chdir('/Users/joseph.hsieh/Documents/GitHub/estimating-impact-of-opioid-prescription-regulations-team-1/')
# varify the path using getcwd()
cwd = os.getcwd()
# print the current directory
print("Current working directory is:", cwd)

#import datasets
arcos_all = pd.read_csv('20_intermediate_files/arcos_intermediate/arcos_grouped_all.csv')
FIPS_list = pd.read_csv('00_source/FIPS_list.csv')

#clean FIPS dataset
FIPS_list.rename(columns={"Name":"COUNTY","State":"STATE"},inplace=True)
FIPS_list['COUNTY'] = FIPS_list['COUNTY'].str.upper()

arcos_all
FIPS_list
arcos_merged =  pd.merge(arcos_all, FIPS_list, on=['COUNTY','STATE'], how='left')
arcos_merged[arcos_merged['FIPS'].isna()]
