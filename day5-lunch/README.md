Exercise 1:

1) Make the script tab delimited by using the python script below

!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

df = np.genfromtxt("aau1043_dnm.csv", delimiter = ",", dtype = None, encoding = None, names = True)
              
print(df)

2) Sort by Proband_id and save it in a file named aau1043_dnm_sorted.csv by using this in the command line below 

./day5-lunch.py | sort -k 5 > aau1043_dnm_sorted.csv

3) Do the same things for parental age using bash (you get away with bash not recognizing a column since the Proband_id is in the first column) running this in the command line shown below

sort -k 1

Exercise 2: To get the pvalues use the script below

!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

df = np.genfromtxt("mf_joined.txt", delimiter = None, dtype = None, encoding = None, names = ["ID", "m_count", "parent", "f_count", "parent", "father_age", "mother_age"]) 

model = smf.ols(formula = "m_count ~ 1 + mother_age", data = df)
results = model.fit()
print(results.summary())

3) The relationship is very significant because the p value for the association between maternal age and maternally inherited de novo mutations is 6.878208e-24. The size of the relationship is 0.3776.

4) The relationship is very significant because the p value for the association between paternal age and paternally inherited de novo mutations is 1.552294e-84.
The size of the relationship is 1.3538.

6) The number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband because the p value is 2.198603179308129e-264, which is lower than 0.05.

7) The predicted number of paternal de novo mutations for a proband with a father who was 50.5 years old at the proband's time of birth is 78.018535. Used the portion of code below.

new_data = df[0]
new_data.fill(0)
new_data["father_age"] = 50.5 
print(model.summary())
print(model.predict(new_data))