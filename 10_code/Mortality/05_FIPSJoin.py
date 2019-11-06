import pandas as pd
import numpy as np

path = "../../20_intermediate_files/Mortality_Intermediate/"
inpath = "../../00_Source/"

drug_deaths_by_state_year_county = pd.read_csv(path + "Drug Deaths aggregated by State,County and Year.csv")

fips = pd.read_csv(inpath + "FIPS list.csv")


drug_deaths_by_state_year_county = drug_deaths_by_state_year_county.drop(['County'], axis = 1)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' County', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' Parish', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' Borough', '', regex = True)

#drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' city', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' City', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' Area', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace('St. ', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' Census', '', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace('District of Columbia', 'Washington', regex = True)



drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace(' ', '', regex = True)



#fips['Name'] = fips['Name'].replace(' City', '', regex = True)
fips['Name'] = fips['Name'].replace('St. ', '', regex = True)
fips['Name'] = fips['Name'].replace('St ', '', regex = True)
fips['Name'] = fips['Name'].replace(' ', '', regex = True)
##Strip the spaces
drug_deaths_by_state_year_county['State'] = drug_deaths_by_state_year_county['State'].str.strip()

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].str.strip().str.lower()

fips['Name'] = fips['Name'].str.strip().str.lower()

#Check for duplicates in fip
#fips[fips.duplicated(['Name', 'State'])]
#fips[(fips['Name'] == "baltimore") & (fips['State'] == "MD")]

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace("mary's", 'marys', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace("princegeorge's", 'princegeorges', regex = True)

drug_deaths_by_state_year_county['County_Name'] = drug_deaths_by_state_year_county['County_Name'].replace("carson", 'carsoncity', regex = True)

#Test
#drug_deaths_by_state_year_county[drug_deaths_by_state_year_county['County_Name'] == "Yuma"]

#drug_deaths_by_state_year_county.loc[drug_deaths_by_state_year_county['County_Name'] == 'Acadia Parish' ,'County_Name'] = "Acadia"

test = pd.merge(drug_deaths_by_state_year_county ,fips, left_on = ["County_Name", "State"], right_on = ["Name","State"], how = "outer", validate="m:1", indicator = True)

#test = pd.merge(drug_deaths_by_state_year_county ,fips, on = ["State"], how = "outer", validate="m:m", indicator = True)

test._merge.value_counts()


    
#for i in np.sort(test[test._merge == "left_only"]['County_Name'].unique()):
#    print(i)
    
#for i in (test.loc[test._merge == "left_only",['County_Name','State']]):
#    print(i)

#for i in np.sort(test[test._merge == "right_only"]['Name'].unique()):
#    print(i)

drug_deaths_by_state_year_county_fip = pd.merge(drug_deaths_by_state_year_county ,fips, left_on = ["County_Name", "State"], right_on = ["Name","State"], how = "left", validate="m:1")
    
    
drug_deaths_by_state_year_county_fip.to_csv(path + "Drug Deaths aggregated by State,County and Year fip.csv", index = False)