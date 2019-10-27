import pandas as pd
import numpy as np

path = "../../20_intermediate_files/Mortality_Intermediate/"

drug_deaths_by_state_year_county = pd.read_csv(path + "Drug Deaths aggregated by State,County and Year.csv")


drug_deaths_by_state_year_county = drug_deaths_by_state_year_county.drop(['County'], axis = 1)

drug_deaths_by_state_year_county.to_csv(path + "Drug Deaths aggregated by State,County and Year cleaned.csv", index = False)