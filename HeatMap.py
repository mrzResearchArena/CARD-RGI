PATH = '/home/mrz/Desktop/All/Research/RGI/Datasets'

import os
os.chdir(PATH)

#%%
def defaultHeatMap():
    os.system('rgi heatmap --input {}'.format(PATH))

def geneFamilyHeatMap():
    os.system('rgi heatmap --input {} --category gene_family --display text'.format(PATH))

def profileFrequencyHeatMap():
    os.system('rgi heatmap --input {} --frequency'.format(PATH))

def drugClassFrequency():
    os.system('rgi heatmap --input {} --category drug_class --frequency --display text'.format(PATH))

def cluster():
    os.system('rgi heatmap --input {} --cluster both'.format(PATH))
    
def clusterResistanceMechanism():
    os.system('rgi heatmap --input {} --cluster samples --category resistance_mechanism --display text'.format(PATH))
    
    
#%%
defaultHeatMap()

#%%
geneFamilyHeatMap()

#%%
profileFrequencyHeatMap()

#%%
drugClassFrequency()

#%%
cluster()

#%%
clusterResistanceMechanism()

#%%
