import pandas as pd
import numpy as np

#importing file
merged0=pd.read_csv("../../20_intermediate_files/Merged_Files/PopMort.csv")

prescriptions = pd.read_csv("../../20_intermediate_files/Prescriptions_Intermediate/arcos_grouped_all_FIPS.csv")

#Merge prescriptions

prescriptions = prescriptions.drop(columns = ['Unnamed: 0','Unnamed: 0.1']) 
prescriptions.rename(columns={'YEAR':'Year'}, inplace=True)

mergedUSA=pd.merge(merged0,prescriptions,on=['FIPS','Year'],how='left',validate="m:m", indicator=True)

mergedUSA._merge.value_counts()

left=(mergedUSA[mergedUSA['_merge']=='left_only'])
left.Year.value_counts()

#Looks ok, all left_only belong to years prescrips info not available

#In case I want to loop
#States=['Florida','Washington','Texas']

#dropmerge column and set up policy states and policy years
mergedUSA = mergedUSA.drop(columns = ['_merge']) 
mergedUSA['PolState']=0
mergedUSA.PolState[mergedUSA['STNAME']=='Florida']=1
mergedUSA.PolState[mergedUSA['STNAME']=='Washington']=1
mergedUSA.PolState[mergedUSA['STNAME']=='Texas']=1

#Florida policy = 2010, Texas = 2007, Wash = 2012
##Policy Year distance for difdif
mergedUSA['polyearF']=mergedUSA['Year']-2010
mergedUSA['polyearT']=mergedUSA['Year']-2007
mergedUSA['polyearW']=mergedUSA['Year']-2012

##Policy year binary (is it a policy year?)
mergedUSA['Policy']=0
mergedUSA.Policy[(mergedUSA['STNAME'] == 'Florida') & (mergedUSA['Year'] >= 2010 )]=1
mergedUSA.Policy[(mergedUSA['STNAME'] == 'Texas') & (mergedUSA['Year'] >= 2007 )]=1
mergedUSA.Policy[(mergedUSA['STNAME'] == 'Washington') & (mergedUSA['Year'] >= 2012 )]=1

#Per capita data, scaled up for convenience
mergedUSA['DeathsPC']=mergedUSA['Deaths']/(mergedUSA['POPULATION']/10000)

#Convenience variables for subsets
Florida=mergedUSA[mergedUSA['STNAME']=='Florida']
Texas=mergedUSA[mergedUSA['STNAME']=='Texas']
Washington=mergedUSA[mergedUSA['STNAME']=='Washington']

##############################DEATHS ANALYSIS####################################

States=[Florida,Texas,Washington]

#EDA plots
from plotnine import *
import warnings
warnings.filterwarnings('ignore', module='plotnine')

for i in States:
    print(i.STNAME.max())
    p=(ggplot(mergedUSA, aes(x='Year', y='DeathsPC')) +
           geom_point(data=Florida)+
            geom_smooth(data=Florida)
   
    )

    print(p)
    pass

#Nothing useful


####Prepost####
STN='Florida'
#Florida
State=Florida
PrePostF=(ggplot(State, aes(x='Year', y='DeathsPC')) +
        geom_point(alpha=0.006) +
        geom_smooth(data=State[State['Policy']==0], method='lm',color='black') +
        geom_smooth(data=State[State['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2009.5)
  )

PrePostF
#mergedUSA.Policy[(mergedUSA['STNAME'] == 'Florida') & (mergedUSA['Year'] >= 2010 )]
#Washington
State=Washington
PrePostW=(ggplot(State, aes(x='Year', y='DeathsPC')) +
        geom_point(alpha=0.006) +
        geom_smooth(data=State[State['Policy']==0], method='lm',color='black') +
        geom_smooth(data=State[State['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2011.5)
  )

PrePostW

#Texas
State=Texas
PrePostT=(ggplot(State, aes(x='Year', y='DeathsPC')) +
        geom_point(alpha=0.006) +
        geom_smooth(data=State[State['Policy']==0], method='lm',color='black') +
        geom_smooth(data=State[State['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2006.5)
  )

PrePostT
    
## Not sure of anything yet

#### Difference in Difference
# Florida
State=Florida
DifDifF=(ggplot(mergedUSA, aes(x='polyearF', y='DeathsPC')) +
        geom_smooth(data=mergedUSA[mergedUSA['polyearF']<0], method='lm',color='red') +
        geom_smooth(data=mergedUSA[mergedUSA['polyearF']>=0], method='lm',color='darkred') +
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Florida') & (mergedUSA['Policy'] == 0)],color='blue',method='lm')+
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Florida') & (mergedUSA['Policy'] == 1)],color='darkblue',method='lm')+
        geom_vline(xintercept=0)
  )

DifDifF

# Washington
DifDifW=(ggplot(mergedUSA, aes(x='polyearW', y='DeathsPC')) +
        geom_smooth(data=mergedUSA[mergedUSA['polyearW']<0], method='lm',color='red') +
        geom_smooth(data=mergedUSA[mergedUSA['polyearW']>=0], method='lm',color='darkred') +
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Washington') & (mergedUSA['Policy'] == 0)],color='blue',method='lm')+
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Washington') & (mergedUSA['Policy'] == 1)],color='darkblue',method='lm')+
        geom_vline(xintercept=0)
  )

DifDifW

# Texas
DifDifT=(ggplot(mergedUSA, aes(x='polyearT', y='DeathsPC')) +
        geom_smooth(data=mergedUSA[mergedUSA['polyearT']<0], method='lm',color='red') +
        geom_smooth(data=mergedUSA[mergedUSA['polyearT']>=0], method='lm',color='darkred') +
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Texas') & (mergedUSA['Policy'] == 0)],color='blue',method='lm')+
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Texas') & (mergedUSA['Policy'] == 1)],color='darkblue',method='lm')+
        geom_vline(xintercept=0)
  )

DifDifT

#Save Plots
PrePostF.save("../../30_results/Graphs/FloridaDEATHSPrePost.png")
DifDifF.save("../../30_results/Graphs/FloridaDEATHSDifDif.png")

PrePostT.save("../../30_results/Graphs/TexasDEATHSPrePost.png")
DifDifT.save("../../30_results/Graphs/TexasDEATHSDifDif.png")

PrePostW.save("../../30_results/Graphs/WashingtonDEATHSPrePost.png")
DifDifW.save("../../30_results/Graphs/WashingtonDEATHSDifDif.png")



##################################PRESCRIBES ANALYSIS#########################

#per capita data
mergedUSA['PrescribePC']=mergedUSA['MME_Str']/mergedUSA['POPULATION']
mergedUSA.head()

Florida=mergedUSA[mergedUSA['STNAME']=='Florida']

p=(ggplot(Florida, aes(x='Year', y='PrescribePC')) +
        geom_point() +
       geom_smooth()
   
)

p


#Policy years comparison aka PrePost
PrePostFP=(ggplot(Florida, aes(x='Year', y='PrescribePC')) +
        geom_point(alpha=0.075) +
        geom_smooth(data=Florida[Florida['Policy']==0], method='lm',color='black') +
        geom_smooth(data=Florida[Florida['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2009.5) +
         xlim(2006,2012) +
         ylim(0,1.5)
  )

PrePostFP
## Seems like there is something

#Initial DIF DIF plot
DifDifFP=(ggplot(mergedUSA, aes(x='polyearF', y='PrescribePC')) +
        geom_smooth(data=mergedUSA[mergedUSA['polyearF']<0], method='lm',color='red') +
        geom_smooth(data=mergedUSA[mergedUSA['polyearF']>=0], method='lm',color='darkred') +
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Florida') & (mergedUSA['Policy'] == 0)],color='blue',method='lm')+
        geom_smooth(data=mergedUSA[(mergedUSA['STNAME'] == 'Florida') & (mergedUSA['Policy'] == 1)],color='darkblue',method='lm')+
        geom_vline(xintercept=0)
  )

DifDifFP

PrePostFP.save("../../30_results/Graphs/FloridaPRESCRIBEPrePost.png")
DifDifFP.save("../../30_results/Graphs/FloridaPRESCRIBEDifDif.png")

