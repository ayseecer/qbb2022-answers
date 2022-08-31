# QBB2022 - Day 1 - Homework Exercises Submission

Exercise 1:

Fixed Script: 

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v nucleotide="$nuc" '/^#/{next} {if ($4 == nucleotide) {print $5}}' $1 | sort | uniq -c
done

Run-> 
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
The results make sense since the most common alternatives are purines for purines and pyrimidines for pyrimidines, which are more common transition mutations rather than the more disruptive and less common transversion mutations.

Exercise 2: Create promoter file with regions 1,2,10,11.
Use bed tools to intersect promoter regions and SNP regions.

vcffile=~/data/vcf_files/random_snippet.vcf
promofile=~/qbb2022-answers/day1-homework/promoter.bed

bedtools intersect -a $vcffile -b $promofile > promoterSNP.vcf

Run -> bash exercise1.sh promoterSNP.vcf
Considering  A
   6 C
  32 G
   8 T
Considering  C
  12 A
  11 G
  39 T
Considering  G
  46 A
  17 C
  11 T
Considering  T
  10 A
  29 C
   8 G
Answer:
Considering  C
  12 A
  11 G
  39 T

Exercise 3: 

2 errors, one is tab delimited, other is sorting

awk 'BEGIN{OFS="\t"} {print}' input_file

awk '/^#/{next} BEGIN{OFS="\t"} {print $1,$2-1, $2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed


  