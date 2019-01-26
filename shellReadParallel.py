import os
from multiprocessing import Process

IN  = '/home/mrz/Desktop/All/Research/RGI/ExperimentalDatasets'
OUT = '/home/mrz/Desktop/All/Research/RGI/ExperimentalOUT'

os.chdir(IN)
Files = os.listdir()


#%%
def run(file):
    try:
        os.system('rgi main --input_sequence {} --output_file {}/{} --low_quality'.format(file, OUT, file))
    except:
        print('File Error is {}!'.format(file))
    
    
P = []

def beginParallel(): [p.start() for p in P]    
def endParallel():   [p.join() for p in P]    

def parallel():
    for file in Files:
        P.append(Process(target=run, args=(file,)))
        
    
    beginParallel()
    endParallel()


#%%
import time

begin = time.time()
parallel()
print(time.time()-begin)


#%%
### Don't execute before run: parallel()
def removeUnnecessaryFiles():
    os.system('rm *.fai') # Remove from IN 
    os.chdir(OUT)
    os.system('rm *.predictedGenes.json *.homolog.json *.overexpression.json *.rrna.json *.variant.json *.txt *.temp *.fsa *.fai *.xml *.draft *.nhr *.nin *.nsq *.potentialGenes')  # Remove from OUT 
    
 
#%%
removeUnnecessaryFiles()
    
#%%
