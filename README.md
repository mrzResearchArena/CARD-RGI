### RGI

#### Color Code
- Yellow represents a perfect hit, 
- Teal represents a strict hit, 
- Purple represents no hit.


rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --category gene_family
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --category gene_family --display fill
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --category gene_family --display text
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --frequency
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --category drug_class --frequency --display text
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --cluster both
rgi heatmap --input /home/mrz/rgi-4.2.2/tests/inputs/heatmap_inputs --cluster samples --category resistance_mechanism --display fill

