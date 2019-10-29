import pandas as pd
import numpy as np


path = "../../20_intermediate_files/Mortality_Intermediate/"

mortality_drug_death_byCountybyYear = pd.read_csv(path + "Drug Deaths aggregated by County and Year.csv")

temp = mortality_drug_death_byCountybyYear['County'].str.split(",", expand = True)

mortality_drug_death_byCountybyYear['County_Name'] = temp[0]

mortality_drug_death_byCountybyYear['State'] = temp[1]

mortality_drug_death_byCountybyYear.to_csv(path + "Drug Deaths aggregated by State,County and Year.csv", index = False)