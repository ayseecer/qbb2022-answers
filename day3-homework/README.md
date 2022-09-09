Exercise 1:

Run -> plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3

Results saved to plink.eigenval and plink.eigenvec .

Exercise 2:

#!/usr/bin/env python

import matplotlib.pyplot as plt import numpy as np

vals_per_gene = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names= ["locus1", "locus2", "val1", "val2", "val3", "pop", "super_pop", "gender"])

fig, ax = plt.subplots(nrows = 2)

ax[0].set_ylabel("PCA2") ax[0].set_xlabel("PCA1") ax[1].set_ylabel("PCA3") ax[1].set_xlabel("PCA1") ax[0].scatter(vals_per_gene["val1"], vals_per_gene["val2"]) ax[1].scatter(vals_per_gene["val1"], vals_per_gene["val3"])

fig.tight_layout() plt.savefig("homework2_figures1and2.png") plt.show()

I see clustering in the plot, which might indicate SNP clustering based on a certain variable such as demographic.

Exercise 3:

join <(sort plink.eigenvec) <(sort integrated_call_samples.panel) > joined_file.txt

#!/usr/bin/env python

import matplotlib.pyplot as plt import numpy as np

vals_per_gene = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names= ["locus1", "locus2", "val1", "val2", "val3", "pop", "super_pop", "gender"])

print(np.unique(vals_per_gene["super_pop"]))

pops = np.unique(vals_per_gene["super_pop"])

for pop in pops np.where(vals_per_gene["super_pop"]==pop)