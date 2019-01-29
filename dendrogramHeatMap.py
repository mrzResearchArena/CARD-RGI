### load a json file:
import json
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir('/home/mrz/Desktop/All/Research/RGI/OriginalDatasets')

#%%
### Find all antibiotic using SET

Files = os.listdir()

Antibiotics = []
for file in Files:
    D = open(file, 'r').read()
    D = json.loads(D)
    for _, u in D.items():
        for _, v in u.items():
            Antibiotics.append(v['ARO_name'])
            #print(v['ARO_name'])
            

Antibiotics = sorted(set(Antibiotics))
nameAntibiotics = Antibiotics.copy()
nameGenes = [gene[:-5] for gene in os.listdir()]

Antibiotics = { antibiotic : float(50)  for antibiotic in Antibiotics }
 
#%%

Files = os.listdir()
#print(Files)
Information = {}

for file in Files:
    information = Antibiotics.copy()
    D = open(file, 'r').read()
    D = json.loads(D)
    for _, u in D.items():
        for _, v in u.items():
            information[v['ARO_name']] = v['perc_identity']

            
    Information[file[:-5]] = information


V = []
for key, value in Information.items():
    v = []
#    v.append(key)
    for _, val in value.items():
        v.append(float(val))
    V.append(v)

V = np.array(V)        


#%%
D = pd.DataFrame(data=V,            # values
                 index=nameGenes,    # 1st column as index
                 columns=nameAntibiotics).to_csv('/home/mrz/on.csv', index=True)  # 1st row as the column names

#%%
### Goto the .csv and add Genes at the first-line
D = pd.read_csv('/home/mrz/on.csv')
D = D.set_index('Genes')
#%%
def clusterHeatMapSTD():
    sns.clustermap(D, standard_scale=1)

def clusterHeatMapZ():
    sns.clustermap(D, z_score=1)
    

#%%
clusterHeatMapSTD()

#%%
clusterHeatMapZ()
