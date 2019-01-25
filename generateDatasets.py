IN  = '/home/mrz/Desktop/All/Research/RGI/ExperimentalDatasets'
OUT = '/home/mrz/Desktop/All/Research/RGI/OUT'

import os
#%% Generate Files (JSON for HeatMap)

os.chdir(IN)
Files = os.listdir()
print(Files)

for file in Files:
    try:
        os.system('rgi main --input_sequence {} --output_file {}/{} --low_quality'.format(file, OUT, file))
    except:
        print('File Error!')

    
#%% Removed Unnecessary Files

Files = os.listdir()
print(Files)        
os.system('rm *.fai')

os.chdir(OUT)
os.system('rm *.predictedGenes.json *.homolog.json *.overexpression.json *.rrna.json *.variant.json *.txt *.temp *.fsa *.fai *.xml *.draft *.nhr *.nin *.nsq *.potentialGenes')

#%%
