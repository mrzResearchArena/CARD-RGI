### load a json file:
setNaN = -1
import json
import os
import numpy as np

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
nameAntibiotics = ['Genes'] + nameAntibiotics

nameGenes = [gene[:-5] for gene in os.listdir()]

Antibiotics = { antibiotic : setNaN  for antibiotic in Antibiotics }
 
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
        v.append(val)
    V.append(v)

V = np.array(V)        

#%%
ensure=True
for antibiotic in nameAntibiotics:
    if ensure==True:
        print(antibiotic, end='')
        ensure=False
    else:
        print(',{}'.format(antibiotic), end='')
print()
for gene, info in zip(nameGenes, V):
    ensure=True
    print(gene, end='')
    for v in info:
        print(',{}'.format(v), end='')            
    print(end='\n')
    
