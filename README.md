# Resistance Gene Identifier (RGI)

## Code Description

[]()
### 1. Generate Datasets
##### Step 1.1: Basic Process [ [Generate Datasets](https://github.com/mrzResearchArena/CARD-RGI/blob/master/generateDatasets.py) ]
##### Step 1.2: Parallel Processing [ [Generate Datasets](https://github.com/mrzResearchArena/CARD-RGI/blob/master/generateDatasetsParallelProcessing.py) ]

#### Step X:
[Draw Dendrogram HeatMap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/%20dendrogramHeatMap.py)


#### Step X:
[Generate CSV](https://github.com/mrzResearchArena/CARD-RGI/blob/master/CSV.py)

#### Step X:
[Generate CSV](https://github.com/mrzResearchArena/CARD-RGI/blob/master/CSV.py)

#### Step X:
[Draw Dendrogram HeatMap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/dendrogramHeatMap.py)

## HeatMap ( Command-line )

#### Step 1: Default
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH
```

#### Step 2: Gene Family
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category gene_family --display text
```

#### Step 3: Profile Frequency
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --frequency
```

#### Step 3: Drug Class Frequency
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category drug_class --frequency --display text
```
#### Step 4: Cluster

##### Step 4.1: Default Cluster
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --cluster both
```

##### Step 4.2: Cluster on Resistance Mechanism
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --cluster samples --category resistance_mechanism --display text
```

## Heatmap ( Image )

##### Gene Family RGI Heatap
![Cluster RGI Heatmap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Gene_Family_RGI_heatmap.png)

##### Profile Frequency RGI Heatmap
![Cluster RGI Heatmap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Profile_Frequency_RGI_heatmap.png)

##### Drug Class Frequency RGI Heatmap
![Cluster RGI Heatmap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Drug_Class_Frequency_RGI_heatmap.png)

##### Cluster RGI Heatmap
![Cluster RGI Heatmap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Cluster_RGI_heatmap.png)

##### Cluster Resistance Mechanism RGI Heatmap
![Cluster RGI Heatmap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Cluster_Resistance_Mechanism_RGI_heatmap.png)


## Dendrogram with Heatmap ( Image )

##### Dendrogram with Heatmap ( using standard daviation )
![STD](https://github.com/mrzResearchArena/CARD-RGI/blob/master/STD.png)

##### Dendrogram with Heatmap ( using z-score )
![Z](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Z.png)


## Color Code
- Yellow represents a perfect hit, 
- Teal represents a strict hit, 
- Purple represents no hit.

