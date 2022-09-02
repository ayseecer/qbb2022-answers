#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

vals_per_gene = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names= ["locus1", "locus2", "val1", "val2", "val3", "pop", "super_pop", "gender"])

print(np.unique(vals_per_gene["pop"]))

pops = np.unique(vals_per_gene["pop"])

fig, ax=plt.subplots()

for pop in pops:
    list_of_people_pops = np.where(vals_per_gene["pop"]==pop)
    vals_per_gene[list_of_people_pops]
    
ax[0].scatter(vals_per_gene["val1"], vals_per_gene["val2"])
ax[1].scatter(vals_per_gene["val1"], vals_per_gene["val3"])




#ax.plot(x1,y1)
#ax.plot(x2,y2)
    

#Super_pop has (AFR, AMR, EAS, EUR, SAS) unique elements
#pop has = ['ACB' 'ASW' 'BEB' 'CDX' 'CEU' 'CHB' 'CHS' 'CLM' 'ESN' 'FIN' 'GBR' 'GIH'
 #'GWD' 'IBS' 'ITU' 'JPT' 'KHV' 'LWK' 'MSL' 'MXL' 'PEL' 'PJL' 'PUR' 'STU'
 #'TSI' 'YRI']

# fig, ax = plt.subplots(nrows = 3)
#
# ax[0].set_ylabel("PCA2")
# ax[0].set_xlabel("PCA1")
# ax[0].scatter(vals_per_gene["val1"], vals_per_gene["val2"])
#
# fig.tight_layout()
# #plt.savefig("")
# plt.show()