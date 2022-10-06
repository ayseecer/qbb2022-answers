#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

drug = "CB1908_IC50"
# define dictionary to have chr and position value
p_value_by_pos = {}
total_snps = 0
log_p_values_for_plot = []
log_p_values_for_plot_filtered = []

for i, line in enumerate(open(f"{drug}_gwas_results.assoc.linear")):
    fields = line.strip().split()
    if i == 0:
        continue
    chrom = int(fields[0])
    position = int(fields[2])
    p_values = float(fields[8])
    log_p_values = -1*np.log10(p_values)
    # use the enumerate to count the total number of SNPs
    total_snps+=1
    # use chr and position info 
    p_value_by_pos.setdefault(chrom, [])
    # assign the position and the p-value to each chr
    p_value_by_pos[chrom].append((position, log_p_values))
    # sort by chromosome color
    log_p_values_for_plot.append(log_p_values)
    if log_p_values >= 5:
        log_p_values_for_plot_filtered.append('red')
    else:
        log_p_values_for_plot_filtered.append('black')
    
x_count = [x for x in range(total_snps)]
# change x location for x axis to snp count

fig, ax = plt.subplots()
ax.scatter(x = x_count, y = log_p_values_for_plot, color = log_p_values_for_plot_filtered, s=0.5)
plt.title("Manhattan Plot (SNPs associated with IC50's from CB1908)")
ax.set_ylabel("-log10(p)")
ax.set_xlabel("SNPs")
plt.tight_layout()
plt.show()
plt.savefig("week4_manhatton_plot_CB1908.png")