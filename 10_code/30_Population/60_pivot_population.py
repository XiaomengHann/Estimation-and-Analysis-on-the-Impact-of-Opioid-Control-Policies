# melt and pivot the dataset
pop_2003_2015_melt = pop_2003_2015.melt(id_vars = ['FIPS','STNAME','CTYNAME'])
pop_2003_2015_melt.head()

pop_2003_2015_pivot = pop_2003_2015_melt.pivot_table(index = ['FIPS','STNAME','CTYNAME','variable'])

pop_2003_2015_pivot = pop_2003_2015_pivot.reset_index()
pop_2003_2015_pivot.head()

pop_2003_2015_pivot = pop_2003_2015_pivot.rename(columns = {'variable':'YEAR','value':'POPULATION'})
pop_2003_2015_pivot.to_csv(outpath + 'population_2003_2015_pivot.csv')
