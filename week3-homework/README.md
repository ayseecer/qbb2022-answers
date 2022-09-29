WEEK 3 - Homework

Question 1: Index the sacCer3 genome using `bwa index sacCer3.fa `

Question 2: Bash command used: `for file in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63; do bwa mem -t 4 -R "@RG\tID:${file}\tSM:${file}" -o output/${file}.sam sacCer3.fa ${file}.fastq; done`

Question 3a: Sort bam files using this command: `for file in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63; do samtools sort -@ 4 -o output/${file}_sorted.bam -O bam output/${file}.sam; done`

Question 3b: Index bam files using this command: `for file in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63; do samtools index output/${file}_sorted.bam; done`

Question 4: Alignment using freebayes using this command:
`ls *.bam > input_bams.txt`
`freebayes -f ../sacCer3.fa -L input_bams.txt --genotype-qualities -p 1 > var.vcf` (ran it in the output directory)

Question 5: Used the command `vcffilter -f "QUAL > 0.99" var.vcf > filtered_var.vcf` to filter out the lower then 0.99 quality values.

Question 6: `vcfallelicprimitives -k -g filtered_var.vcf > decomposed_filtered_var.vcf`

Question 7: `snpEff ann R64-1-1.99 decomposed_filtered_var.vcf > ann_dec_filt_var.vcf`

Question 8: 

