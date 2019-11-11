import pandas as pd
import numpy as np

# Reusing Washington code!!!!

#importing file
merged0=pd.read_csv("../../20_intermediate_files/Merged_Files/PopMort.csv")

mergedW=(merged0[merged0['STNAME']=='Texas'])

#per capita data
mergedW['DeathsPC']=mergedW['Deaths']/mergedW['POPULATION']
mergedW.head()
#numbers seem low, lets do it by 10000  people
mergedW['DeathsPC']=mergedW['Deaths']/(mergedW['POPULATION']/10000)
mergedW.head()

#Same for USA
#per capita data
mergedU=merged0
mergedU['DeathsPC']=merged0['Deaths']/(merged0['POPULATION']/10000)
mergedU.head()



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
mergedWG.Policy[mergedWG['Year']>=2007]=1

#Initial Comparison
p0=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
        geom_smooth(method='lm',color='green') +
        geom_vline(xintercept=2006.5)
  )

p0
## Seems inconclusive, lets do PrePost

#Policy years comparison aka PrePost
PrePost=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue') +
        geom_vline(xintercept=2006.5)
  )

PrePost
## Seems like there is at least a stabilizing effect

#Initial DIF DIF plot
p2=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_vline(xintercept=2006.5)
  )

p2
##Looks like USA has a clear upward trend, but Texas is



DifDif=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_smooth(method='lm',color='green') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black', se =False) +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue',se=False) +
        geom_vline(xintercept=2006.5)
  )

DifDif

# Without overall
DifDif2=(ggplot(mergedWG, aes(x='Year', y='DeathsPC')) +
        geom_point() +
       geom_point(data=mergedUG, color='red') +
       geom_smooth(data=mergedUG, method='lm',color='red') +
        geom_smooth(data=mergedWG[mergedWG['Policy']==0], method='lm',color='black', se =False) +
        geom_smooth(data=mergedWG[mergedWG['Policy']==1], method='lm',color='blue',se=False) +
        geom_vline(xintercept=2006.5)
  )

DifDif2

#Save Plots
PrePost.save("../../30_results/Graphs/TexasPrePost.png")
DifDif.save("../../30_results/Graphs/TexasDifDif.png")
DifDif2.save("../../30_results/Graphs/TexasDifDif2.png")