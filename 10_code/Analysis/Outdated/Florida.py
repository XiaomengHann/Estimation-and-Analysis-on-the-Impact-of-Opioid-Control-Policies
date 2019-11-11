import pandas as pd
import numpy as np

# Reusing Washington code!!!!

#importing file
merged0=pd.read_csv("../../20_intermediate_files/Merged_Files/PopMort.csv")

prescriptions = pd.read_csv("../../20_intermediate_files/Prescriptions_Intermediate/arcos_grouped_all_FIPS.csv")

#Merge prescriptions

prescriptions = prescriptions.drop(columns = ['Unnamed: 0','Unnamed: 0.1']) 
prescriptions.rename(columns={'YEAR':'Year'}, inplace=True)

mergedUSA=pd.merge(merged0,prescriptions,on=['FIPS','Year'],how='left',validate="m:m", indicator=True)

mergedU=pd.merge(merged0,prescriptions,on='FIPS',how='left',validate="m:m", indicator=True)

mergedU._merge.value_counts()

#Looks good.

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

#Policy Years MergedXG is grouped data for visualizations
mergedWG['Policy']=0
mergedWG.Policy[mergedWG['Year']>=2010]=1
mergedUG['Policy']=0
mergedUG.Policy[mergedUG['Year']>=2010]=1
mergedW['Policy']=0
mergedW.Policy[mergedW['Year']>=2010]=1
mergedU['Policy']=0
mergedU.Policy[mergedU['Year']>=2010]=1


#Initial Comparison
p0=(ggplot(mergedW, aes(x='Year', y='DeathsPC')) +
        geom_point(alpha=0.01) +
        geom_smooth(method='lm',color='green') +
        geom_vline(xintercept=2009.5)
  )

p0
## Not sure of anything yet

#Policy years comparison aka PrePost
PrePost=(ggplot(mergedW, aes(x='Year', y='DeathsPC')) +
        geom_point(alpha=0.006) +
        geom_smooth(data=mergedW[mergedW['Policy']==0], method='lm',color='black') +
        geom_smooth(data=mergedW[mergedW['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2009.5)
  )

PrePost
## Seems like there is a change

#Year from policy data
mergedW['polyear']=mergedW['Year']-2010
mergedU['polyear']=mergedU['Year']-2010
mergedUG['polyear']=mergedUG['Year']-2010
mergedWG['polyear']=mergedWG['Year']-2010


# Without overall
DifDif2=(ggplot(mergedW, aes(x='polyear', y='DeathsPC')) +
         geom_point(data=mergedWG,color='darkblue',alpha=0.5) +
         geom_point(data=mergedUG,color='darkred',alpha=0.5)+
        geom_smooth(data=mergedW[mergedW['Policy']==0], method='lm',color='blue') +
        geom_smooth(data=mergedW[mergedW['Policy']==1], method='lm',color='darkblue') +
          geom_smooth(data=mergedU[mergedU['Policy']==0], method='lm',color='red') +
        geom_smooth(data=mergedU[mergedU['Policy']==1], method='lm',color='darkred') 
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
mergedUG['Policy']=0
mergedUG.Policy[mergedUG['Year']>=2010]=1

#Initial Comparison
p0=(ggplot(mergedWG, aes(x='Year', y='PrescribePC')) +
        geom_point() +
        geom_smooth(method='lm',color='green') +
        geom_vline(xintercept=2009.5)
  )

p0
## Seems like there was no change

#Policy years comparison aka PrePost
PrePost=(ggplot(mergedW, aes(x='Year', y='PrescribePC')) +
        geom_point(alpha=0.005) +
        geom_smooth(data=mergedW[mergedW['Policy']==0], method='lm',color='black') +
        geom_smooth(data=mergedW[mergedW['Policy']==1], method='lm',color='blue') +
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
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black', se =False) +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue',se=False)  +
          geom_smooth(data=mergedUG[mergedUG['Policy']==0], method='lm',color='red', se=False) +
        geom_smooth(data=mergedUG[mergedUG['Policy']==1], method='lm',color='darkred', se=False) +
        geom_vline(xintercept=2009.5)
  )

DifDif2

PrePost.save("../../30_results/Graphs/FloridaPRESCRIBEPrePost.png")
DifDif2.save("../../30_results/Graphs/FloridaPRESCRIBEDifDif.png")

