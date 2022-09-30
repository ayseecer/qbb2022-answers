#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

af_data = np.genfromtxt("plink.frq", dtype = None, encoding = None, skip_header=1, names= ["CHR,", "SNP", "A1", "A2", "MAF", "NCHROBS"])

fig, ax = plt.subplots()

ax.hist(af_data["MAF"])
plt.title("Alelle Frequencies")
ax.set_ylabel("Number of Frequencies")
ax.set_xlabel("Alelle Frequency")
#plt.show()
plt.savefig("week4_plot2.png")