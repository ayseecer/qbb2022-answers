#!/usr/bin/env python
import matplotlib.pyplot as plt 
import numpy as np
import scanpy as sc

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
filtered_data = sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)  
#read in data and filtered the data

#STEP 1
# PCA plot unfiltered data
sc.tl.pca(adata, svd_solver='arpack') #getting the pca
sc.tl.pca(filtered_data, svd_solver='arpack') #getting the pca

#fig, ax = plt.subplots(1, 2) #set up subplots 
#sc.pl.pca(adata, ax = ax[0], title="Raw Data", show=False) #makes the data
#sc.pl.pca(filtered_data, ax = ax[1],title="Filtered Data", show=False) #makes the data and attaches it to scanpy
#plt.savefig("Part1_PCA_plots.png") #save the figure

# STEP 2
sc.pp.neighbors(filtered_data, n_neighbors=10, n_pcs=40)
sc.tl.leiden(filtered_data)
sc.tl.umap(filtered_data, maxiter=1000)
sc.tl.tsne(filtered_data)

#fig, ax = plt.subplots(1, 2)
#sc.pl.umap(filtered_data, ax = ax[0], title="UMAP", color="leiden", show=False)
#sc.pl.tsne(filtered_data, ax = ax[1], title="t-SNE", color="leiden", show=False)
#plt.tight_layout()
#plt.savefig("Part2_plots.png")

# STEP 3
t_test = sc.tl.rank_genes_groups(filtered_data, 'leiden', method='t-test', copy=True)
logreg = sc.tl.rank_genes_groups(filtered_data, 'leiden', method='logreg', copy=True)

genes = []
n = len(logreg.uns["leiden_colors"])
for i in range(n):
    names = logreg.uns['rank_genes_groups']["names"][str(i)]
    scores = logreg.uns['rank_genes_groups']["scores"][str(i)]
    genes.append(names[np.argmax(scores)])
# plot the tsne with the genes for each gene, should be ~9-10
sc.pl.tsne(logreg, color=genes, show=False, save="logreg_tsne_by_genes.png")

logreg.uns['rank_genes_groups']["names"]
logreg.uns['rank_genes_groups']["scores"]
#sc.pl.rank_genes_groups(t_test, n_genes=25, sharey=False, save='t_test_rank_genes_groups.png')
#sc.pl.rank_genes_groups(logreg, n_genes=25, sharey=False, save='logreg_rank_genes_groups.png')
#sc.pl.rank_genes_groups_matrixplot(logreg, save='logreg_matrix.png')
celltypes = ["Oligodendrocytes-2", "Astrocytes-14", "Pericytes-25"] 

#one plot, different tsne's to show where each gene is enriched
sc.pl.umap(filtered_data, title="UMAP", color="celltypes", show=False)
plt.show()

#AQP4 in astrocytes28
#APOLD1 in endothelial cells29
#CCL4 in microglia30 
#RELN in neurons31
#PLP1 in oligodendrocytes32
#PDGFRA in OPCs




