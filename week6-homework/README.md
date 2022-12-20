Part 1:

Q1: What percentage of reads are valid interactions (duplicates do not count as valid)?
answer: based on the "plotHiCFragment" figures 37.8% for dCTCF and 36.6% for ddCTCF.

Q2: What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)?
-> Dangling-end pairs (62.9%). It reveals a problem during the digestion, fill-in or ligation steps.

Part 2: ran load_data.py using this bash command:
`python load_data.py hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap`

then ran my heatmap.py script (uploaded in GitHub) with this bash command:
`python heatmap.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap1.pdf`

