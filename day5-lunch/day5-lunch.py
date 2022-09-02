#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

df = np.genfromtxt("aau1043_dnm.csv", delimiter = ",", dtype = None, encoding = None, names = True) 
print(df)
              
              
