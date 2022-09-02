#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

df = np.genfromtxt("mf_joined.txt", delimiter = None, dtype = None, encoding = None, names = ["ID", "m_count", "parent", "f_count", "parent", "father_age", "mother_age"]) 
#print(df)

#print(df["m_count"])
# print(df["m_count"])

# fig, ax = plt.subplots()
# ax.hist(df["m_count"], alpha = 0.5, label = "maternal de novo mutations")
# ax.hist(df["f_count"], alpha = 0.5, label = "paternal de novo mutations")
# ax.set_xlabel("Mutation Count")
# ax.set_ylabel("Freq of Mutation Count")
# ax.legend()
# plt.savefig("ex2_c.png")

#print(stats.ttest_ind(df["m_count"],df["f_count"]))

model = smf.ols(formula = "f_count ~ 1 + father_age", data = df).fit()

new_data = df[0]
new_data.fill(0)
new_data["father_age"] = 50.5 
# print(model.summary())
print(model.predict(new_data))

# print(model(new_data))

# results = model.fit()
# print(results.summary())