import pandas as pd
import numpy as np

# Reusing Washington code!!!!

#importing file
merged0=pd.read_csv("../../20_intermediate_files/Merged_Files/PopMort.csv")

prescriptions = pd.read_csv("../../20_intermediate_files/Prescriptions_Intermediate/arcos_grouped_all_FIPS.csv")

#Merge prescriptions

prescriptions = prescriptions.drop(columns = ['Unnamed: 0','Unnamed: 0.1']) 

mergedU=pd.merge(merged0,prescriptions,on='FIPS',how='left',validate="m:m", indicator=True)

mergedU._merge.value_counts()

#25 rows have no prescripts, in DC and Indiana. For now, I will drop them.
mergedU.drop(mergedU[mergedU['_merge']=='left_only'].index,inplace=True)

#dropmerge column and set up Florida 
mergedU = mergedU.drop(columns = ['_merge']) 
mergedW=(mergedU[mergedU['STNAME']=='Florida'])
##############################DEATHS ANALYSIS####################################

#per capita data
mergedW['DeathsPC']=mergedW['Deaths']/mergedW['POPULATION']

#numbers seem low, lets do it by 10000  people
mergedW['DeathsPC']=mergedW['Deaths']/(mergedW['POPULATION']/10000)

#Same for USA
#per capita data
mergedU['DeathsPC']=merged0['Deaths']/(merged0['POPULATION']/10000)



#EDA plots
from plotnine import *
import warnings
warnings.filterwarnings('ignore', module='plotnine')

p=(ggplot(mergedW, aes(x='Year', y='DeathsPC')) +
        geom_point() +
       geom_smooth()
   
)

p

#Group on yearly mean
mergedWG=mergedW.groupby(['Year']).mean()
mergedWG['Year']=mergedWG.index

#USA
mergedUG=mergedU.groupby(['Year']).mean()
mergedUG['Year']=mergedUG.index

#Policy Years
mergedWG['Policy']=0
mergedWG.Policy[mergedWG['Year']>=2010]=1

#Initial Comparison
p0=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
        geom_smooth(method='lm',color='green') +
        geom_vline(xintercept=2009.5)
  )

p0
## Seems there might be something, lets do PrePost

#Policy years comparison aka PrePost
PrePost=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2009.5)
  )

PrePost
## Seems like there is a change

#Initial DIF DIF plot
p2=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_vline(xintercept=2006.5)
  )

p2
##Looks like USA has a clear upward trend, but Florida isnt following

# Without overall
DifDif2=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black', se =False) +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue',se=False) +
        geom_vline(xintercept=2009.5)
  )

DifDif2

#Save Plots
PrePost.save("../../30_results/Graphs/FloridaDEATHSPrePost.png")
DifDif2.save("../../30_results/Graphs/FloridaDEATHSDifDif.png")



##################################PRESCRIBES ANALYSIS#########################

#per capita data
mergedW['PrescribePC']=mergedW['MME_Str']/mergedW['POPULATION']
mergedW.head()


#Same for USA
#per capita data
mergedU['PrescribePC']=mergedU['MME_Str']/(mergedU['POPULATION'])
mergedU.head()



#EDA plots
from plotnine import *
import warnings
warnings.filterwarnings('ignore', module='plotnine')

p=(ggplot(mergedW, aes(x='Year', y='PrescribePC')) +
        geom_point() +
       geom_smooth()
   
)

p

#Group on yearly mean
mergedWG=mergedW.groupby(['Year']).mean()
mergedWG['Year']=mergedWG.index

#USA
mergedUG=mergedU.groupby(['Year']).mean()
mergedUG['Year']=mergedUG.index

#Policy Years
mergedWG['Policy']=0
mergedWG.Policy[mergedWG['Year']>=2010]=1

#Initial Comparison
p0=(ggplot(mergedWG, aes(x='Year', y='PrescribePC')) +
        geom_point() +
        geom_smooth(method='lm',color='green') +
        geom_vline(xintercept=2009.5)
  )

p0
## Seems like there was no change

#Policy years comparison aka PrePost
PrePost=(ggplot(mergedWG, aes(x='Year', y='PrescribePC')) +
        geom_point() +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2009.5)
  )

PrePost
## Seems like there is little proof of change, it's always been falling

#Initial DIF DIF plot
p2=(ggplot(mergedWG, aes(x='Year', y='PrescribePC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_vline(xintercept=2006.5)
  )

p2
##Looks like USA has a similar trend but in a smaller overall mean
# Without overall
DifDif2=(ggplot(mergedWG, aes(x='Year', y='PrescribePC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black', se =False) +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue',se=False) +
        geom_vline(xintercept=2009.5)
  )

DifDif2

PrePost.save("../../30_results/Graphs/FloridaPRESCRIBEPrePost.png")
DifDif2.save("../../30_results/Graphs/FloridaPRESCRIBEDifDif.png")
