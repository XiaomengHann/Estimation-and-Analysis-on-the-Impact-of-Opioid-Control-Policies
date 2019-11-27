import pandas as pd
import numpy as np


path = "../../20_intermediate_files/Mortality_Intermediate/"

mortality_drug_death_filter = pd.read_csv(path + "Drug Deaths 2003-2015.csv")

#Replace Missing Data with NaN
mortality_drug_death_filter.loc[mortality_drug_death_filter['Deaths'] == "Missing", ['Deaths']] = np.NaN

#Change data type for deaths from object to float64
mortality_drug_death_filter = mortality_drug_death_filter.astype({'Deaths':'float64'})


#Apply groupby on County and Year and sum Deaths
mortality_drug_death_byCountybyYear = mortality_drug_death_filter[["County","Year","Deaths"]].groupby(["County","Year"], as_index = False).sum()


mortality_drug_death_byCountybyYear.to_csv(path + "Drug Deaths aggregated by County and Year.csv", index = False)

