#!/usr/bin/env python
import matplotlib.pyplot as plt 
import numpy as np
import scanpy as sc

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

# PCA plot unfiltered data
#sc.tl.pca(adata, svd_solver='arpack')
#sc.pl.pca(adata, save='before.png')

# PCA plot unfiltered data
#sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
#sc.tl.pca(adata, svd_solver='arpack')
#sc.pl.pca(adata, save='after.png')

# Plotting 
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)
sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata)

# Step 3 Distinguishing Genes
sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)
sc.pl.pca(adata, save='t-test.png')
sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save='rank_genes_groups.png')
sc.pl.pca(adata, save='logreg.png')
sc.pl.tsne(adata, save='tsne.png')




