import pandas as pd
import seaborn as sns

#%%
### Generate dataset using CSV.py
D = pd.read_csv('/home/mrz/Documents/out.csv')
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
