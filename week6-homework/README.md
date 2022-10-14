Part 1:

Q1: What percentage of reads are valid interactions (duplicates do not count as valid)?
-> 92% for dCTCF and 88% for ddCTCF.

Q2: What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)?
-> Dangling-end pairs (62.9%). It reveals a problem during the digestion, fill-in or ligation steps.

Part 2: ran this command into bash.
`python load_data.py hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap`