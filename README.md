# Resistance Gene Identifier (RGI)

## Code Description

### 1. Generate Datasets (JSON)
##### Step 1.1: Basic Process [ [Generate Datasets](https://github.com/mrzResearchArena/CARD-RGI/blob/master/generateDatasets.py) ]
##### Step 1.2: Parallel Processing [ [Generate Datasets](https://github.com/mrzResearchArena/CARD-RGI/blob/master/generateDatasetsParallelProcessing.py) ]

`Note: The programme will take FASTA sequences as inputs; it will produce JSON file for each sequence.`

&nbsp;

### 2. HeatMap:
##### Step 2.1 Heatmap [ [HeatMap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/heatMap.py) ]
`Note: The programme will take previously generated JSON file as inputs; it will produce heatmap.`

&nbsp;

### 3. Generate Datasets (CSV)
##### Step 3.1 [ [Generate CSV](https://github.com/mrzResearchArena/CARD-RGI/blob/master/WriteCSV.py) ]
`Note: The programme will take previously generated JSON file as inputs; it will produce the name of antibiotic resistance ontology (ARO) and the percentage of identity for each ARO.`
`[Visualized CSV file](https://github.com/mrzResearchArena/CARD-RGI/blob/master/output.csv).'

&nbsp;

### 4. Dendrogram with HeatMap:
##### Step 4.1 [ [Draw Dendrogram HeatMap](https://github.com/mrzResearchArena/CARD-RGI/blob/master/dendrogramHeatMap.py) ]
`Note: The programme will take previously generated CSV file as input; it will produce dendrogram with heatmap.`

&nbsp;

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

&nbsp;

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


&nbsp;

## Dendrogram with Heatmap ( Image )

##### Dendrogram with Heatmap ( using standard daviation )
![STD](https://github.com/mrzResearchArena/CARD-RGI/blob/master/STD.png)

##### Dendrogram with Heatmap ( using z-score )
![Z](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Z.png)

&nbsp;

## Color Code
- Yellow represents a perfect hit, 
- Teal represents a strict hit, 
- Purple represents no hit.
