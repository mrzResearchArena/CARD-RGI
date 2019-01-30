# Resistance Gene Identifier (RGI)

## HeatMap ( Commands )

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

## HeatMap ( Image )

![image_1](https://github.com/mrzResearchArena/CARD-RGI/blob/master/Cluster_RGI_heatmap.png)


## Color Code
- Yellow represents a perfect hit, 
- Teal represents a strict hit, 
- Purple represents no hit.

