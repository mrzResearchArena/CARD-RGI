import pandas as pd
import seaborn as sns

### Web: https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

#%%
### Generate dataset using CSV.py
D = pd.read_csv('/home/mrz/binaryOutput.csv')
D = D.set_index('Genes')

#%%
# method='single' ->    Nearest Point Algorithm. 
# method='complete' ->  Farthest Point Algorithm or Voor Hees Algorithm.  
# method='average' ->   UPGMA algorithm
# method='weighted' ->  WPGMA algorithm
# method='median' ->    WPGMC algorithm
# method='centroid' ->  UPGMC algorithm

def clusterHeatMap():
    sns.clustermap(data=D, method='average')
    
#%%
clusterHeatMap()

#%%
