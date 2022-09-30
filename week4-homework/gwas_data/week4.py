#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

PCA_data = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names= ["ID_1,", "ID_2", "PCA_1", "PCA_2", "PCA_3", "PCA_4", "PCA_5", "PCA_6", "PCA_7", "PCA_8", "PCA_9", "PCA_10"])

fig, ax = plt.subplots()

ax.scatter(PCA_data["PCA_1"], PCA_data["PCA_2"])

ax.set_ylabel("PCA1")
ax.set_xlabel("PCA2")
plt.title("Genetic Relatedness Between the Cell Lines")
#plt.show()
plt.savefig("week4_plot1.png")