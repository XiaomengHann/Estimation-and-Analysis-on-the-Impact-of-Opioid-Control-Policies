# generate population for 56 states
state = list(range(57))
for i in range(57):
    if i in range(11):
        state[i] = '0' + str(i) + '000'
    else: state[i] = str(i) + '000'

state_2003_2015 = pop_2003_2015.loc[pop_2003_2015['FIPS'].isin(state),]

state_2003_2015.to_csv(outpath + 'population_2003_2015_state_level.csv')
