#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import vcfParser

vcf = vcfParser.parse_vcf("ann_dec_filt_var.vcf")

read_depth = []
quality_distribution = []
alelle_freq = []
eff = []

for header in vcf[1:]:
    for value in header[9:]:
        read_depth.append(value[4])
        quality_distribution.append(value[1])
    alelle_freq.append(header[7]["AF"])
    eff_wholething = header[7]["ANN"]
    eff_wholething_split = eff_wholething.split("|")
    eff.append(eff_wholething_split[2])
    
eff_dict = {}
for i in eff:
    if i in eff_dict.keys():
        eff_dict[i] +=1
    else:
        eff_dict[i] = 1

read_depth = [int(d) for d in read_depth if d != '.']
quality_distribution = [float(d) for d in quality_distribution if d != '.']
alelle_freq = [float(d) for d in alelle_freq if d != '.']

fig, axs = plt.subplots(2,2)

axs[0,0].hist(read_depth, density=True)
axs[0,0].set_title("distribution of alelle depth")
axs[0,0].set_xlabel("depth")
axs[0,0].set_ylabel("density")
axs[0,0].set_yscale("log")

axs[0,1].hist(read_depth, density=True)
axs[0,1].set_title("distribution of alelle quality")
axs[0,1].set_xlabel("quality score")
axs[0,1].set_ylabel("density")
axs[0,1].set_yscale("log")

axs[1,0].hist(read_depth, density=True)
axs[1,0].set_title("distribution of alelle frequency")
axs[1,0].set_xlabel("frequency")
axs[1,0].set_ylabel("density")
axs[1,0].set_yscale("log")

axs[1,1].bar(eff_dict.keys(), eff_dict.values())
axs[1,1].set_title("effect of alleles")
axs[1,1].set_xlabel("effect of allele")
axs[1,1].set_ylabel("count")

plt.show()












