import pandas as pd
import numpy as np
import csv
import os
import re

# varify the path using getcwd()
cwd = os.getcwd()
# print the current directory
print("Current working directory is:", cwd)

#import datasets
arcos_all = pd.read_csv('../20_intermediate_files/arcos_intermediate/arcos_grouped_all.csv')
FIPS_list = pd.read_csv('../00_source/FIPS list.csv')

#clean FIPS dataset
FIPS_list.rename(columns={"Name":"COUNTY","State":"STATE"},inplace=True)
FIPS_list['COUNTY'] = FIPS_list['COUNTY'].str.upper()

#FIXES

#NOTE OUR FIPS DATA IS OLD https://www.cdc.gov/nchs/data/nvss/bridged_race/County_Geography_Changes.pdf im pretty sure our FIPS data is old. fml.. Prince of Wales-Hyder Census Area (FIPS code = 02198). Prince of Wales-Hyder Census Area was created from the remainder of the former Prince of Wales-Outer Ketchikan Census Area (FIPS code = 02201) after part (Outer Ketchikan) was annexed by Ketchikan Gateway Borough (FIPS code = 02130) effective May 19, 2008 and another part was included in the new Wrangell Borough (effective June 1, 2008). Note that no data for this Census Area appear on NCHS birth and mortality files.

arcos_all['COUNTY'] = arcos_all['COUNTY'].replace('SAINT','ST', regex = True)
arcos_all[(arcos_all['COUNTY']=='LAMOURE') & (arcos_all['STATE']=='ND')] = arcos_all[(arcos_all['COUNTY']=='LAMOURE') & (arcos_all['STATE']=='ND')].replace("LAMOURE", "LA MOURE")
#2 - Broomfield, CO was missing from FIPS_list. Deleted the data
arcos_all[(arcos_all['COUNTY']=='LAGRANGE') & (arcos_all['STATE']=='IN')] = arcos_all[(arcos_all['COUNTY']=='LAGRANGE') & (arcos_all['STATE']=='IN')].replace("LAGRANGE", "LA GRANGE")
arcos_all[arcos_all['COUNTY']=='DEKALB'] = arcos_all[arcos_all['COUNTY']=='DEKALB'].replace("DEKALB", "DE KALB")
arcos_all[(arcos_all['COUNTY']=='SAINT BERNARD') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT BERNARD') & (arcos_all['STATE']=='LA')].replace("SAINT BERNARD", "ST BERNARD")
arcos_all[(arcos_all['COUNTY']=='ST JOSEPH') & (arcos_all['STATE']=='IN')] = arcos_all[(arcos_all['COUNTY']=='ST JOSEPH') & (arcos_all['STATE']=='IN')].replace("ST JOSEPH", "SAINT JOSEPH")
arcos_all[arcos_all['COUNTY']=='DEWITT'] = arcos_all[arcos_all['COUNTY']=='DEWITT'].replace("DEWITT", "DE WITT")
arcos_all[(arcos_all['COUNTY']=='DUPAGE') & (arcos_all['STATE']=='IL')] = arcos_all[(arcos_all['COUNTY']=='DUPAGE') & (arcos_all['STATE']=='IL')].replace("DUPAGE", "DU PAGE")
arcos_all[(arcos_all['COUNTY']=='MATANUSKA SUSITNA') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='MATANUSKA SUSITNA') & (arcos_all['STATE']=='AK')].replace("MATANUSKA SUSITNA", "MATANUSKA-SUSITNA")
arcos_all[(arcos_all['COUNTY']=='PETERSBURG') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='PETERSBURG') & (arcos_all['STATE']=='AK')].replace('PETERSBURG', 'WRANGELL-PETERSBURG')
arcos_all[(arcos_all['COUNTY']=='PRINCE OF WALES HYDER') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='PRINCE OF WALES HYDER') & (arcos_all['STATE']=='AK')].replace('PRINCE OF WALES HYDER', 'PRINCE OF WALES-OUTER KETCHIKAN')
arcos_all[(arcos_all['COUNTY']=='SKAGWAY') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='SKAGWAY') & (arcos_all['STATE']=='AK')].replace('SKAGWAY', 'SKAGWAY-HOONAH-ANGOON')
arcos_all[(arcos_all['COUNTY']=='VALDEZ CORDOVA') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='VALDEZ CORDOVA') & (arcos_all['STATE']=='AK')].replace('VALDEZ CORDOVA', 'VALDEZ-CORDOVA')
arcos_all[(arcos_all['COUNTY']=='WRANGELL') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='WRANGELL') & (arcos_all['STATE']=='AK')].replace('WRANGELL', 'WRANGELL-PETERSBURG')
arcos_all[arcos_all['COUNTY']=='SAINT JOSEPH'] = arcos_all[arcos_all['COUNTY']=='SAINT JOSEPH'].replace('SAINT JOSEPH', 'ST CLAIR')
arcos_all[(arcos_all['COUNTY']=='OBRIEN') & (arcos_all['STATE']=='IA')] = arcos_all[(arcos_all['COUNTY']=='OBRIEN') & (arcos_all['STATE']=='IA')].replace('OBRIEN', 'O BRIEN')
arcos_all[(arcos_all['COUNTY']=='BRISTOL') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='BRISTOL') & (arcos_all['STATE']=='VA')].replace('BRISTOL', 'BRISTOL CITY')
arcos_all[(arcos_all['COUNTY']=='COLONIAL HEIGHTS CITY') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='COLONIAL HEIGHTS CITY') & (arcos_all['STATE']=='VA')].replace('COLONIAL HEIGHTS CITY', 'COLONIAL HEIGHTS CIT')
arcos_all[(arcos_all['COUNTY']=='RADFORD') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='RADFORD') & (arcos_all['STATE']=='VA')].replace('RADFORD', 'RADFORD CITY')
arcos_all[(arcos_all['COUNTY']=='SALEM') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='SALEM') & (arcos_all['STATE']=='VA')].replace('SALEM', 'SALEM CITY')
arcos_all[arcos_all['COUNTY']=='DESOTO'] = arcos_all[arcos_all['COUNTY']=='DESOTO'].replace("DESOTO", "DE SOTO")
arcos_all[(arcos_all['COUNTY']=='STE GENEVIEVE') & (arcos_all['STATE']=='MO')] = arcos_all[(arcos_all['COUNTY']=='STE GENEVIEVE') & (arcos_all['STATE']=='MO')].replace('STE GENEVIEVE', 'STE. GENEVIEVE')

# #merge testing
#merge_arcos_test = pd.merge(arcos_all,FIPS_list, left_on = ['COUNTY','STATE'], right_on = ['COUNTY','STATE'], how = "outer", validate="m:1", indicator = True)
#merge_arcos_test._merge.value_counts()
#Deleted these rows from arcos_all. Broomfield wasn't in our FIPS data due to an outdated FIPS list, and St. Clair, IN doesn't exist.
arcos_all = arcos_all[~((arcos_all['COUNTY']=='BROOMFIELD') & (arcos_all['STATE']=='CO'))]
arcos_all = arcos_all[~((arcos_all['COUNTY']=='ST CLAIR') & (arcos_all['STATE']=='IN'))]

#merge
arcos_merged =  pd.merge(arcos_all, FIPS_list, on=['COUNTY','STATE'], how='left', )
#check if there are any NAs
arcos_merged[arcos_merged['FIPS'].isna()]

#write to file
arcos_merged.to_csv('../20_intermediate_files/arcos_grouped_all_FIPS.csv')
