import pandas as pd
import numpy as np
merged0=pd.read_csv("../../20_intermediate_files/Merged_Files/PopMort.csv")

prescriptions = pd.read_csv("../../20_intermediate_files/Prescriptions_Intermediate/arcos_grouped_all_FIPS.csv")
prescriptions = prescriptions.drop(columns = ['Unnamed: 0','Unnamed: 0.1'])

mergedU=pd.merge(merged0,prescriptions,on='FIPS',how='left',validate="m:m", indicator=True)

mergedU._merge.value_counts()

mergedU.drop(mergedU[mergedU['_merge']=='left_only'].index,inplace=True)

mergedU = mergedU.drop(columns = ['_merge'])
mergedU['DeathsPC']=merged0['Deaths']/(merged0['POPULATION']/10000)

# Generate the did regression for Florida
# First generate a dummy variable to indicate whether we are in the period of the policy implementation
# The policy in Florida is implemented in 2010.
mergedW['Policy']=0
mergedW.Policy[mergedW['Year']>=2010]=1

# Then generate a dummy variable to indicate whether we are in the state experienced a policy change
mergedU['State'] = [1 if x == 'Florida' else 0 for x in mergedU['STNAME']]

# Generate the interaction of the two above variables to get the did coefficient
mergedU['Policy:State'] = mergedU['Policy'] * mergedU['State']

from plotnine import *
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm

# First allow for the level changes
did_Florida = smf.ols('DeathsPC ~  Policy + Policy:State',data = mergedU).fit()
print(did_Florida.summary())

# Then allow for the level changes and trend changes
# Adjust the variable of year to have value of 0 in the year of policy implementation
mergedU['adj_year'] = mergedU['Year'] - 2010
# Generate the interactions
mergedU['Policy:adj_year'] = mergedU['Policy'] * mergedU['adj_year']
mergedU['State:adj_year'] = mergedU['State'] * mergedU['adj_year']
mergedU['Policy:State:adj_year'] = mergedU['Policy'] * mergedU['State'] * mergedU['adj_year']

# Get the second did regression for Florida
did2_Florida = smf.ols('DeathsPC ~  adj_year + Policy + Policy:State + Policy:adj_year + State:adj_year + Policy:State:adj_year',data = mergedU).fit()
print(did2_Florida.summary())

# Similar process for Texas and Washington
mergedU['Policy_T']=0
mergedU.Policy_T[mergedU['Year']>=2007]=1
mergedU['State_T'] = [1 if x == 'Texas' else 0 for x in mergedU['STNAME']]

mergedU['Policy_T:State_T'] = mergedU['Policy_T'] * mergedU['State_T']
did_Texas = smf.ols('DeathsPC ~  Policy_T + Policy_T:State_T',data = mergedU).fit()
print(did_Texas.summary())

mergedU['adj_year_T'] = mergedU['Year'] - 2007
mergedU['Policy_T:adj_year_T'] = mergedU['Policy_T'] * mergedU['adj_year_T']
mergedU['State_T:adj_year_T'] = mergedU['State_T'] * mergedU['adj_year_T']
mergedU['Policy_T:State_T:adj_year_T'] = mergedU['Policy_T'] * mergedU['State_T'] * mergedU['adj_year_T']

did2_Texas = smf.ols('DeathsPC ~  adj_year_T + Policy_T + Policy_T:State_T + Policy_T:adj_year_T + State_T:adj_year_T + Policy_T:State_T:adj_year_T',data = mergedU).fit()
print(did2_Texas.summary())

mergedU['Policy_W']=0
mergedU.Policy_W[mergedU['Year']>=2012]=1
mergedU['State_W'] = [1 if x == 'Washington' else 0 for x in mergedU['STNAME']]

mergedU['Policy_W:State_W'] = mergedU['Policy_W'] * mergedU['State_W']
did_Washington = smf.ols('DeathsPC ~  Policy_W + Policy_W:State_W',data = mergedU).fit()
print(did_Washington.summary())

mergedU['adj_year_W'] = mergedU['Year'] - 2012
mergedU['Policy_W:adj_year_W'] = mergedU['Policy_W'] * mergedU['adj_year_W']
mergedU['State_W:adj_year_W'] = mergedU['State_W'] * mergedU['adj_year_W']
mergedU['Policy_W:State_W:adj_year_W'] = mergedU['Policy_W'] * mergedU['State_W'] * mergedU['adj_year_W']

did2_Washington = smf.ols('DeathsPC ~  adj_year_W + Policy_W + Policy_W:State_W + Policy_W:adj_year_W + State_W:adj_year_W + Policy_W:State_W:adj_year_W',data = mergedU).fit()
print(did2_Washington.summary())

# Similar process for the prescription in Florida
mergedU['PrescribePC']=mergedU['MME_Str']/(mergedU['POPULATION'])

did_Florida_Pre= smf.ols('PrescribePC ~  Policy + Policy:State',data = mergedU).fit()
print(did_Florida_Pre.summary())

did2_Florida_Pre = smf.ols('PrescribePC ~  adj_year + Policy + Policy:State + Policy:adj_year + State:adj_year + Policy:State:adj_year',data = mergedU).fit()
print(did2_Florida_Pre.summary())
