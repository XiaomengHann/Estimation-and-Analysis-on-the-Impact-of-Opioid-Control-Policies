import pandas as pd
import numpy as np



path = "../../20_intermediate_files/Mortality_Intermediate/"

mortality = pd.read_csv(path + "Underlying Cause 2003-2015.csv")

mortality = mortality.drop(["Unnamed: 0","Notes", "Year Code"], axis = 1)
mortality.sample(5)
mortality.dtypes
mortality.shape

drug_related_death_filter = [ 'Drug poisonings (overdose) Unintentional (X40-X44)', 'All other drug-induced causes', 'Drug poisonings (overdose) Undetermined (Y10-Y14)', 'Drug poisonings (overdose) Homicide (X85)']

#Missing Data Check
mortality.loc[mortality['Drug/Alcohol Induced Cause'].isin(drug_related_death_filter),].isnull().sum()

#Filter out the data
mortality_drug_death_filter = mortality.loc[mortality['Drug/Alcohol Induced Cause'].isin(drug_related_death_filter),]

mortality_drug_death_filter.to_csv(path + "Drug Deaths 2003-2015.csv", index = False)