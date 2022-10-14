Question 1: Made README.md file in week4-homework directory.

Question 2: cd into gwas_data and run `plink --vcf genotypes.vcf --pca 10` to make plink.eigenval, plink.eigenvec, plink.log, and plink.nosex. The figure is in github and is saved as week4_plot1.png. The python script is in github and is saved as week4.py.

Question 3: Ran `plink --vcf genotypes.vcf --freq` to get a plink.frq file. The python script I used is in github named week4_2.py and the histogram image is in github called week4.py.

Question 4: Ran `plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar plink.eigenvec --allow-no-sex --out GS451_IC50_gwas_results` and `plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar plink.eigenvec --allow-no-sex --out CB1908_IC50_gwas_results`

Question 5: Ran the python script named week4_3.py for the first drug and saved my colored manhattan plot into week4_manhatton_plot_GS451.png. Ran the python script named week4_4.py for the second drug and saved my colored manhattan plot into week4_manhatton_plot_CB1908.png. All are uploaded in github.

Question 6: IC50's should match 0|1, 1|0, 1|1 in GS451_IC50.txt and genotypes.vcf (the 1001, 1002 ID's are patients). 


