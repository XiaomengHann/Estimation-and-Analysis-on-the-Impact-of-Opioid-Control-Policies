import pandas as pd
import numpy as np

inpath = "../../00_source/Mortality Data/"

outpath = "../../20_intermediate_files/Mortality_Intermediate/"

mortality = pd.read_csv(inpath + "Underlying Cause of Death, 2003.txt", sep = "\t")


for i in range(2004,2016):

    new_df = pd.read_csv(inpath +"Underlying Cause of Death, {}.txt".format(str(i)), sep = "\t")

    mortality = pd.concat([mortality,new_df])

mortality.to_csv(outpath + "Underlying Cause 2003-2015.csv")
