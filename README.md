### RGI

#### Color Code
- Yellow represents a perfect hit, 
- Teal represents a strict hit, 
- Purple represents no hit.

#### Step 1: Default
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH
```
#### Step 2: Gene Family Deault

```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category gene_family

```
##### Step 2.1: Gene Family Display (Fill) 
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category gene_family --display fill
```

#### Step 2.2: Gene Family Display (Text)
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category gene_family --display text
```

#### Step 2.3: Frequency
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --frequency
```

#### Step 3: Drug Class Frequency
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category drug_class --frequency --display text
```

#### Step 1: Cluster
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --category drug_class --frequency --cluster both
```

#### Step 1: Cluster on Resistance Mechanism
```console
rafsanjani@mrz:~$ rgi heatmap --input PATH --cluster samples --category resistance_mechanism --display fill
```
