#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy
from scipy.stats import poisson

list = [0] * 1000000

reads = 150000 #50000 for 5X coverage

for i in range(reads):
    start = numpy.random.randint(100, 999900)
    for j in range(start, start+100):
        list[j] += 1 
        
fig, ax = plt.subplots()

ax.hist(list, label = "Data")

x = numpy.arange(0, 35, 1) #15 instead of 35 for 5X coverage
y = poisson.pmf(x, 15)*1000000 #5 instead of 15 for 5X coverage

ax.plot(x, y, label = "Poisson")
ax.set_xlabel("Coverage")
ax.set_ylabel("Frequency")
ax.legend()
ax.set_title("15x coverage of a 1Mbp genome with 100bp reads")
fig.tight_layout()
#fig.savefig("week1_homework_15X")
plt.show() 





