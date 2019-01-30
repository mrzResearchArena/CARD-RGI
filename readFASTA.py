### load a json file:
setNaN = 0.0
threshold = 95
import json
import os
import numpy as np

os.chdir('/home/mrz/Desktop/All/Research/RGI/OriginalDatasets')

OUT = open('/home/mrz/binaryOutput.csv', 'w')

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
        #print(antibiotic, end='')
        OUT.write(antibiotic)
        ensure=False
    else:
        #print(',{}'.format(antibiotic), end='')
        OUT.write(','+antibiotic)

#print()        
OUT.write('\n')

for gene, info in zip(nameGenes, V):
    ensure=True
    #print(gene, end='')
    OUT.write(gene)
    for v in info:
        if v==0.0:
            #print(',{}'.format(1), end='')
            OUT.write(','+str(0))            
        else:
            #print(',{}'.format(0), end='')
            OUT.write(','+str(1))
        
        #OUT.write(','+str(v))            
    
    #print(end='\n')
    OUT.write('\n')

OUT.close()
    
#%%