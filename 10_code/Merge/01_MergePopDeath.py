import pandas as pd
import numpy as np

##Path for mortality intermediate file

mortalityPath = "../../20_intermediate_files/Mortality_Intermediate/"

##Path for Population

popPath = "../../20_intermediate_files/Population_intermediate/"

## Output Path

outPath = "../../20_intermediate_files/Merged_Files/"


mortality_df = pd.read_csv(mortalityPath + "Drug Deaths aggregated by State,County and Year fip.csv" )

population_df= pd.read_csv(popPath + "population_2003_2015_pivot.csv")

#Clean up, dropping columns

mortality_df = mortality_df.drop(columns = ['Name']) #,'County_Name','State'
mortality_df['Year'] = mortality_df['Year'].astype('int64')

population_df = population_df.drop(columns = ['Unnamed: 0'])

mergePopMort_test = pd.merge(mortality_df  ,population_df, left_on = ["FIPS",'Year'], right_on = ["FIPS","YEAR"], how = "outer", validate="1:1", indicator = True)

mergePopMort_test._merge.value_counts()

##Bedford City, VA has no 2015 data
##Clifton, VA has no 2015 data
#AK skagway-hoonah-angoon no 2015 data
#AK wrangell-petersburg no 2015 data

##Checks

#mergePopMort.loc[mergePopMort._merge == "left_only",]
#mergePopMort.loc[mergePopMort._merge == "both",]

#Since we have missing data in 2015, we can drop it, we use an inner join. By doing so, we only lose 5 rows of data for 2015 for counties that we do not need

mergePopMort = pd.merge(mortality_df  ,population_df, left_on = ["FIPS",'Year'], right_on = ["FIPS","YEAR"], how = "inner")

## Dataframe clean up drop unnecessary duplicates of county and state name

mergePopMort = mergePopMort.drop(columns = ['YEAR','County_Name','State'], axis = 1)

mergePopMort.to_csv(outPath + "PopMort.csv", index = False)