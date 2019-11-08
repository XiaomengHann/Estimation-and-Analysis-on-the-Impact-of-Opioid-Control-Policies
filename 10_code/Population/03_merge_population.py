# drop unrelated columns
pop1 = pop1.drop(["SUMLEV","REGION", "DIVISION"], axis = 1)
pop2 = pop2.drop(["SUMLEV","REGION", "DIVISION"], axis = 1)

# merge two datasets (2000-2010 and 2010-2018)
pop_2000_2018 = pd.merge(pop1, pop2, on = ['FIPS'], how = 'left', validate = '1:m')
