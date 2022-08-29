# QBB2022 - Day 1 - Lunch Exercises Submission

 Question 2b: 62
 1. wc genes.chr21.bed 
 Run: 219     657    5256 genes.chr21.bed
 2. wc exons.chr21.bed
 Run: 13653   40959  327672 exons.chr21.bed
 Answer: 13653/219 = 62
 
 Question 2c: I would subtract the start position from the end position column and create a new column called exon length. Then I would sort the new column and extract the 6826th position using the head function.
 
 Question 3: The largest fraction of the genome is state 7.
 1. cut -f4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c
 Run: 
 305 1
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
 
 Question 4b:
 1. grep AFR integrated_call_samples.panel | cut -f 2 | sort | uniq -c
 Run: 
   123 ACB
   112 ASW
   173 ESN
   180 GWD
   122 LWK
   128 MSL
   206 YRI
   
Question 4c: I would replace AFR would the other population names.

Question 5b: cut -f 1-9,13 random_snippet.vcf > HG00100.vcf


   
  
   
  
 