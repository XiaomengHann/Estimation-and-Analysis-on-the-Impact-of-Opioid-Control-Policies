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

#FIXES
<<<<<<< Updated upstream
#1 - Add space to La Moure
#arcos_all['COUNTY'] = arcos_all[arcos_all['COUNTY'].str.replace("LAMOURE", "LA MOURE", case = False)
arcos_all[(arcos_all['COUNTY']=='LAMOURE') & (arcos_all['STATE']=='ND')] = arcos_all[(arcos_all['COUNTY']=='LAMOURE') & (arcos_all['STATE']=='ND')].replace("LAMOURE", "LA MOURE")
#2 - Broomfield, CO was missing from FIPS_list. added it to the csv.
#3 - Changed Saint Lawrence, NY to St Lawrence, NY
arcos_all[(arcos_all['COUNTY']=='SAINT LAWRENCE') & (arcos_all['STATE']=='NY')] = arcos_all[(arcos_all['COUNTY']=='SAINT LAWRENCE') & (arcos_all['STATE']=='NY')].replace("SAINT LAWRENCE", "ST LAWRENCE")
#Question: how come I had to save the slice to itself? There are attributes where you dont need to do that.
#4 - FIPS had La Grange but .gov fips has it as LaGrange
arcos_all[(arcos_all['COUNTY']=='LAGRANGE') & (arcos_all['STATE']=='IN')] = arcos_all[(arcos_all['COUNTY']=='LAGRANGE') & (arcos_all['STATE']=='IN')].replace("LAGRANGE", "LA GRANGE")
#5 - FIPS had De Kalb but .gov fips has it as DeKalb. changed csv.
arcos_all[arcos_all['COUNTY']=='DEKALB'] = arcos_all[arcos_all['COUNTY']=='DEKALB'].replace("DEKALB", "DE KALB")
# Searched FIPS for 'FIPS_list[FIPS_list.COUNTY.str.contains('SAINT')]', but they all amost all ST. Going to do a replace all

arcos_all[(arcos_all['COUNTY']=='SAINT BERNARD') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT BERNARD') & (arcos_all['STATE']=='LA')].replace("SAINT BERNARD", "ST BERNARD")
#arcos_all[(arcos_all['COUNTY']=='SAINT CHARLES') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT CHARLES') & (arcos_all['STATE']=='LA')].replace("SAINT CHARLES", "ST CHARLES")
#arcos_all[(arcos_all['COUNTY']=='SAINT HELENA') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT HELENA') & (arcos_all['STATE']=='LA')].replace("SAINT HELENA", "ST HELENA")
arcos_all[(arcos_all['COUNTY']=='SAINT JAMES') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT JAMES') & (arcos_all['STATE']=='LA')].replace("SAINT JAMES", "ST JAMES")
arcos_all[(arcos_all['COUNTY']=='SAINT LANDRY') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT LANDRY') & (arcos_all['STATE']=='LA')].replace("SAINT LANDRY", "ST LANDRY")
arcos_all[(arcos_all['COUNTY']=='SAINT MARTIN') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT MARTIN') & (arcos_all['STATE']=='LA')].replace("SAINT MARTIN", "ST MARTIN")
arcos_all[(arcos_all['COUNTY']=='SAINT MARY') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT MARY') & (arcos_all['STATE']=='LA')].replace("SAINT MARY", "ST MARY")
arcos_all[(arcos_all['COUNTY']=='SAINT HELENA') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT HELENA') & (arcos_all['STATE']=='LA')].replace("SAINT HELENA", "ST HELENA")
arcos_all[(arcos_all['COUNTY']=='SAINT TAMMANY') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT TAMMANY') & (arcos_all['STATE']=='LA')].replace("SAINT TAMMANY", "ST TAMMANY")
=======

#NOTE OUR FIPS DATA IS OLD https://www.cdc.gov/nchs/data/nvss/bridged_race/County_Geography_Changes.pdf im pretty sure our FIPS data is old. fml.. Prince of Wales-Hyder Census Area (FIPS code = 02198). Prince of Wales-Hyder Census Area was created from the remainder of the former Prince of Wales-Outer Ketchikan Census Area (FIPS code = 02201) after part (Outer Ketchikan) was annexed by Ketchikan Gateway Borough (FIPS code = 02130) effective May 19, 2008 and another part was included in the new Wrangell Borough (effective June 1, 2008). Note that no data for this Census Area appear on NCHS birth and mortality files.

arcos_all['COUNTY'] = arcos_all['COUNTY'].replace('SAINT','ST', regex = True)
arcos_all[(arcos_all['COUNTY']=='LAMOURE') & (arcos_all['STATE']=='ND')] = arcos_all[(arcos_all['COUNTY']=='LAMOURE') & (arcos_all['STATE']=='ND')].replace("LAMOURE", "LA MOURE")
#2 - Broomfield, CO was missing from FIPS_list. Deleted the data
arcos_all[(arcos_all['COUNTY']=='LAGRANGE') & (arcos_all['STATE']=='IN')] = arcos_all[(arcos_all['COUNTY']=='LAGRANGE') & (arcos_all['STATE']=='IN')].replace("LAGRANGE", "LA GRANGE")
arcos_all[arcos_all['COUNTY']=='DEKALB'] = arcos_all[arcos_all['COUNTY']=='DEKALB'].replace("DEKALB", "DE KALB")
arcos_all[(arcos_all['COUNTY']=='SAINT BERNARD') & (arcos_all['STATE']=='LA')] = arcos_all[(arcos_all['COUNTY']=='SAINT BERNARD') & (arcos_all['STATE']=='LA')].replace("SAINT BERNARD", "ST BERNARD")
>>>>>>> Stashed changes
arcos_all[(arcos_all['COUNTY']=='ST JOSEPH') & (arcos_all['STATE']=='IN')] = arcos_all[(arcos_all['COUNTY']=='ST JOSEPH') & (arcos_all['STATE']=='IN')].replace("ST JOSEPH", "SAINT JOSEPH")
arcos_all[arcos_all['COUNTY']=='DEWITT'] = arcos_all[arcos_all['COUNTY']=='DEWITT'].replace("DEWITT", "DE WITT")
arcos_all[(arcos_all['COUNTY']=='DUPAGE') & (arcos_all['STATE']=='IL')] = arcos_all[(arcos_all['COUNTY']=='DUPAGE') & (arcos_all['STATE']=='IL')].replace("DUPAGE", "DU PAGE")
arcos_all[(arcos_all['COUNTY']=='MATANUSKA SUSITNA') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='MATANUSKA SUSITNA') & (arcos_all['STATE']=='AK')].replace("MATANUSKA SUSITNA", "MATANUSKA-SUSITNA")
arcos_all[(arcos_all['COUNTY']=='PETERSBURG') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='PETERSBURG') & (arcos_all['STATE']=='AK')].replace('PETERSBURG', 'WRANGELL-PETERSBURG')
<<<<<<< Updated upstream
#NOTE OUR FIPS DATA IS OLD https://www.cdc.gov/nchs/data/nvss/bridged_race/County_Geography_Changes.pdf im pretty sure our FIPS data is old. fml.. Prince of Wales-Hyder Census Area (FIPS code = 02198). Prince of Wales-Hyder Census Area was created from the remainder of the former Prince of Wales-Outer Ketchikan Census Area (FIPS code = 02201) after part (Outer Ketchikan) was annexed by Ketchikan Gateway Borough (FIPS code = 02130) effective May 19, 2008 and another part was included in the new Wrangell Borough (effective June 1, 2008). Note that no data for this Census Area appear on NCHS birth and mortality files
=======
>>>>>>> Stashed changes
arcos_all[(arcos_all['COUNTY']=='PRINCE OF WALES HYDER') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='PRINCE OF WALES HYDER') & (arcos_all['STATE']=='AK')].replace('PRINCE OF WALES HYDER', 'PRINCE OF WALES-OUTER KETCHIKAN')
arcos_all[(arcos_all['COUNTY']=='SKAGWAY') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='SKAGWAY') & (arcos_all['STATE']=='AK')].replace('SKAGWAY', 'SKAGWAY-HOONAH-ANGOON')
arcos_all[(arcos_all['COUNTY']=='VALDEZ CORDOVA') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='VALDEZ CORDOVA') & (arcos_all['STATE']=='AK')].replace('VALDEZ CORDOVA', 'VALDEZ-CORDOVA')
arcos_all[(arcos_all['COUNTY']=='WRANGELL') & (arcos_all['STATE']=='AK')] = arcos_all[(arcos_all['COUNTY']=='WRANGELL') & (arcos_all['STATE']=='AK')].replace('WRANGELL', 'WRANGELL-PETERSBURG')
arcos_all[arcos_all['COUNTY']=='SAINT JOSEPH'] = arcos_all[arcos_all['COUNTY']=='SAINT JOSEPH'].replace('SAINT JOSEPH', 'ST CLAIR')
arcos_all[(arcos_all['COUNTY']=='OBRIEN') & (arcos_all['STATE']=='IA')] = arcos_all[(arcos_all['COUNTY']=='OBRIEN') & (arcos_all['STATE']=='IA')].replace('OBRIEN', 'O BRIEN')
<<<<<<< Updated upstream
arcos_all[(arcos_all['COUNTY']=='SAINT FRANCIS') & (arcos_all['STATE']=='AR')] = arcos_all[(arcos_all['COUNTY']=='SAINT FRANCIS') & (arcos_all['STATE']=='AR')].replace('SAINT FRANCIS', 'ST FRANCIS')
#UHHH THIS IS A BIG ONE THAT MIGHT SCREW US UP
arcos_all[(arcos_all['COUNTY']=='MIAMI-DADE') & (arcos_all['STATE']=='FL')] = arcos_all[(arcos_all['COUNTY']=='MIAMI-DADE') & (arcos_all['STATE']=='FL')].replace('MIAMI-DADE', 'DADE')
arcos_all[(arcos_all['COUNTY']=='SAINT JOHNS') & (arcos_all['STATE']=='FL')] = arcos_all[(arcos_all['COUNTY']=='SAINT JOHNS') & (arcos_all['STATE']=='FL')].replace('SAINT JOHNS', 'ST JOHNS')
arcos_all[(arcos_all['COUNTY']=='SAINT LUCIE') & (arcos_all['STATE']=='FL')] = arcos_all[(arcos_all['COUNTY']=='SAINT LUCIE') & (arcos_all['STATE']=='FL')].replace('SAINT LUCIE', 'ST JOHNS')
arcos_all[(arcos_all['COUNTY']=='SAINT CROIX') & (arcos_all['STATE']=='WI')] = arcos_all[(arcos_all['COUNTY']=='SAINT CROIX') & (arcos_all['STATE']=='WI')].replace('SAINT CROIX', 'ST CROIX')
arcos_all[(arcos_all['COUNTY']=='SAINT MARYS') & (arcos_all['STATE']=='MD')] = arcos_all[(arcos_all['COUNTY']=='SAINT MARYS') & (arcos_all['STATE']=='MD')].replace('SAINT MARYS', 'ST MARYS')
=======
>>>>>>> Stashed changes
arcos_all[(arcos_all['COUNTY']=='BRISTOL') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='BRISTOL') & (arcos_all['STATE']=='VA')].replace('BRISTOL', 'BRISTOL CITY')
arcos_all[(arcos_all['COUNTY']=='COLONIAL HEIGHTS CITY') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='COLONIAL HEIGHTS CITY') & (arcos_all['STATE']=='VA')].replace('COLONIAL HEIGHTS CITY', 'COLONIAL HEIGHTS CIT')
arcos_all[(arcos_all['COUNTY']=='RADFORD') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='RADFORD') & (arcos_all['STATE']=='VA')].replace('RADFORD', 'RADFORD CITY')
arcos_all[(arcos_all['COUNTY']=='SALEM') & (arcos_all['STATE']=='VA')] = arcos_all[(arcos_all['COUNTY']=='SALEM') & (arcos_all['STATE']=='VA')].replace('SALEM', 'SALEM CITY')
arcos_all[arcos_all['COUNTY']=='DESOTO'] = arcos_all[arcos_all['COUNTY']=='DESOTO'].replace("DESOTO", "DE SOTO")
<<<<<<< Updated upstream
arcos_all[arcos_all['COUNTY']=='SAINT CHARLES'] = arcos_all[arcos_all['COUNTY']=='SAINT CHARLES'].replace('SAINT CHARLES', 'ST CHARLES')
arcos_all[arcos_all['COUNTY']=='SAINT CLAIR'] = arcos_all[arcos_all['COUNTY']=='SAINT CLAIR'].replace('SAINT CLAIR', 'ST CLAIR')
arcos_all[(arcos_all['COUNTY']=='SAINT FRANCOIS') & (arcos_all['STATE']=='MO')] = arcos_all[(arcos_all['COUNTY']=='SAINT FRANCOIS') & (arcos_all['STATE']=='MO')].replace('SAINT FRANCOIS', 'ST FRANCOIS')
arcos_all[(arcos_all['COUNTY']=='SAINT LOUIS') & (arcos_all['STATE']=='MO')] = arcos_all[(arcos_all['COUNTY']=='SAINT LOUIS') & (arcos_all['STATE']=='MO')].replace('SAINT LOUIS', 'ST LOUIS')
arcos_all[(arcos_all['COUNTY']=='SAINT LOUIS CITY') & (arcos_all['STATE']=='MO')] = arcos_all[(arcos_all['COUNTY']=='SAINT LOUIS CITY') & (arcos_all['STATE']=='MO')].replace('SAINT LOUIS CITY', 'ST LOUIS CITY')
arcos_all[(arcos_all['COUNTY']=='SAINTE GENEVIEVE') & (arcos_all['STATE']=='MO')] = arcos_all[(arcos_all['COUNTY']=='SAINTE GENEVIEVE') & (arcos_all['STATE']=='MO')].replace('SAINTE GENEVIEVE', 'STE. GENEVIEVE')
arcos_all[(arcos_all['COUNTY']=='SAINT LOUIS') & (arcos_all['STATE']=='MN')] = arcos_all[(arcos_all['COUNTY']=='SAINT LOUIS') & (arcos_all['STATE']=='MN')].replace('SAINT LOUIS', 'ST LOUIS')
#arcos_all[(arcos_all['COUNTY']=='ST CLAIR') & (arcos_all['STATE']=='IL')] = arcos_all[(arcos_all['COUNTY']=='ST CLAIR') & (arcos_all['STATE']=='IL')].replace('ST CLAIR', 'SAINT CLAIR')
#arcos_all[(arcos_all['COUNTY']=='ST CLAIR') & (arcos_all['STATE']=='IN')] = arcos_all[(arcos_all['COUNTY']=='ST CLAIR') & (arcos_all['STATE']=='IN')].replace('ST CLAIR', 'SAINT CLAIR')
#note: i wish i knew how to batch change "SAINT" to "ST"...

#merge_arcos_test = pd.merge(arcos_all,FIPS_list, left_on = ['COUNTY','STATE'], right_on = ['COUNTY','STATE'], how = "outer", validate="m:1", indicator = True)
#merge_arcos_test._merge.value_counts()

arcos_merged =  pd.merge(arcos_all, FIPS_list, on=['COUNTY','STATE'], how='left', )
arcos_merged[arcos_merged['FIPS'].isna()]

#have rows that say St Clair, IN; but St Clair IN doesnt exist. possibly St Clair IL?
arcos_all[arcos_all['COUNTY']=='ST CLAIR']


#dont want to write yet.
#arcos_all.to_csv('20_intermediate_files/arcos_grouped_all_FIPS.csv')

# #code used to search for things within FIPS
#FIPS_list[FIPS_list['FIPS'] == 26147]
#FIPS_list[FIPS_list.COUNTY.str.startswith('BROOM')]
#FIPS_list[FIPS_list.COUNTY.str.contains('ST CLAIR')]
#[FIPS_list['COUNTY'].str.contains('ST.*)']
=======
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
arcos_all.to_csv('../20_intermediate_files/arcos_grouped_all_FIPS.csv')
>>>>>>> Stashed changes
