# QBB2022 - Day 4 - Lunch Exercise

Exercise 1:

1a) 
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp

1b) Typed in "open -a preview exons.chr21.bed.vcf.png" into terminal and viewed the figure to confirm it was the same.

1c) lncRNA, miRNA, and protein coding. I thought that miRNA would be interesting to look at alongside protein coding because 
miRNA can negatively regulate protein expression and I would like to look at the relationship between them. Likewise with lncRNA, which can regulate epigenetic expression.

Exercise 2: Improve plots with modified script below.
#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )
	
ac = np.log1p(ac)

fig, ax = plt.subplots()
ax.hist( ac, density=True )

ax.set_xlabel("Allele Count")
ax.set_ylabel("Density")
ax.set_title("Allele Count vs Density")

fig.tight_layout()
fig.savefig( vcf + ".png" )

fs.close()

2b) change the "for TYPE in protein_coding processed_pseudogene" to "for TYPE in lncRNA" to get lncRNA files. 
command line this to run the script and produce the figures again:
bash do_all.sh random_snippet.vcf gencode.v41.annotation.gtf

Exercise 3:

SYNOPSIS
     bxlab/cmdb-plot-vcfs -- to extract a subset of data in order to create plots.

 USAGE
     bash do_all.sh <random_snippet.vcf> ...

     <gencode.v41.annotation.gtf>   ...

 DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script
         - Use grep to select portions of interest
		 - create plots using python
		 
REQUIRED SOFTWARE
		 conda create --name day4-lunch
		 conda activate day4-lunch
		 conda install bedtools matplotlib


