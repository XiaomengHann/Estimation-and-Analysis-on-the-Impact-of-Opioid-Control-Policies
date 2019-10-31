inpath = "../../00_source/Population data/"

outpath = "../../20_intermediate_files/Population_intermediate/"

import pandas as pd
pop1 = pd.read_csv(inpath + "co-est00int-tot.csv",encoding = "ISO-8859-1")
pop2 = pd.read_csv(inpath + "co-est2018-alldata.csv",encoding = "ISO-8859-1")
