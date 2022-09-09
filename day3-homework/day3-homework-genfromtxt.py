#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

vals_per_gene = np.genfromtxt("joined_file.txt", dtype = None, encoding = None, names= ["locus1", "locus2", "val1", "val2", "val3", "pop", "super_pop", "gender"])

# print(np.unique(vals_per_gene["pop"]))
#
#pops = np.unique(vals_per_gene["pop"])

#fig, ax=plt.subplots()

# for pop in pops:
#     list_of_people_pops = np.where(vals_per_gene["pop"]==pop)
#     pop_data = vals_per_gene[list_of_people_pops]
#     print(pop)
#     print(pop_data)
#     ax.scatter(pop_data["val1"], pop_data["val2"], label = pop)
#
# ax.set_ylabel("PCA2")
# ax.set_xlabel("PCA1")
# plt.title('PC1 vs. PC2 According to Population')
# plt.legend(bbox_to_anchor =(1, 1))
# #plt.show()
# #plt.savefig("ex3_a.png")
# ---------------------------
# super_pops = np.unique(vals_per_gene["super_pop"])
#
# fig, ax=plt.subplots()
#
# for super_pop in super_pops:
#     list_of_people_super_pops = np.where(vals_per_gene["super_pop"]==super_pop)
#     super_pop_data = vals_per_gene[list_of_people_super_pops]
#     print(super_pop)
#     print(super_pop_data)
#     ax.scatter(super_pop_data["val1"], super_pop_data["val2"], label = super_pop)
#
# ax.set_ylabel("PCA2")
# ax.set_xlabel("PCA1")
# plt.title('PC1 vs. PC2 According to Super Population')
# plt.legend(bbox_to_anchor =(1, 1))
# #plt.show()
# plt.savefig("ex3_b.png")
#----------------------------
genders = np.unique(vals_per_gene["gender"])

fig, ax=plt.subplots()

for gender in genders:
    list_of_people_genders = np.where(vals_per_gene["gender"]==gender)
    gender_data = vals_per_gene[list_of_people_genders]
    print(gender)
    print(gender_data)
    ax.scatter(gender_data["val1"], gender_data["val2"], label = gender)

ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
plt.title('PC1 vs. PC2 According to Gender')
plt.legend(bbox_to_anchor =(1, 1))
#plt.show()
plt.savefig("ex3_c.png")










#ax[1].scatter(vals_per_gene["val1"], vals_per_gene["val3"])

#ax[0].set_ylabel("PCA2")
#ax[0].set_xlabel("PCA1")

#ax.plot(x1,y1)
#ax.plot(x2,y2)

# fig, ax = plt.subplots(nrows = 3)
# ax[0].set_ylabel("PCA2")
# ax[0].set_xlabel("PCA1")
# ax[0].scatter(vals_per_gene["val1"], vals_per_gene["val2"])
#
# fig.tight_layout()
# plt.savefig("")