Part 0: 
`conda create -n medaka medaka`
`conda activate medaka`
`sudo /usr/bin/xcode-select --install`
`pip install whatshap==1.0`
`curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/ont_data.tar.gz --output ont_data.tar.gz
tar xzf ont_data.tar.gz`
`cp /Users/cmdb/data/genomes/hg38.fa ./`

Part 1: Region specifics were found in regions.bed
`medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11_new -p -t 6`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14_new -p -t 6`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15_new -p -t 6`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20_new -p -t 6`

Part 2: Mark reads with the correct haplotype tag
`whatshap haplotag -o chr11_phased.bam --reference hg38.fa --regions chr11:1900000:2800000 chr11_new/round_0_hap_mixed_phased.vcf.gz --output-haplotag-list chr11_new/haplotag_list.tsv methylation.bam`

== SUMMARY ==
Total alignments processed:                      4063
Alignments that could be tagged:                 3323
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 4.637377977371216

`whatshap haplotag -o chr14_phased.bam --reference hg38.fa --regions chr14:100700000:100990000 chr14_new/round_0_hap_mixed_phased.vcf.gz --output-haplotag-list chr14_new/haplotag_list.tsv methylation.bam`

== SUMMARY ==
Total alignments processed:                      1439
Alignments that could be tagged:                 1303
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 1.686579942703247

`whatshap haplotag -o chr15_phased.bam --reference hg38.fa --regions chr15:23600000:25900000 chr15_new/round_0_hap_mixed_phased.vcf.gz --output-haplotag-list chr15_new/haplotag_list.tsv methylation.bam`

== SUMMARY ==
Total alignments processed:                     10395
Alignments that could be tagged:                 8000
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 10.335565090179443

`whatshap haplotag -o chr20_phased.bam --reference hg38.fa --regions chr20:58800000:58912000 chr20_new/round_0_hap_mixed_phased.vcf.gz --output-haplotag-list chr20_new/haplotag_list.tsv methylation.bam`

== SUMMARY ==
Total alignments processed:                       648
Alignments that could be tagged:                   87
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 0.6722192764282227

Part 3:
`whatshap split chr11_phased.bam haplotag_list.tsv --output-h1 chr11_output_H1.bam --output-h2 chr11_output_H2.bam`
`whatshap split chr14_phased.bam haplotag_list.tsv --output-h1 chr14_output_H1.bam --output-h2 chr14_output_H2.bam`
`whatshap split chr15_phased.bam haplotag_list.tsv --output-h1 chr15_output_H1.bam --output-h2 chr15_output_H2.bam`
`whatshap split chr20_phased.bam haplotag_list.tsv --output-h1 chr20_output_H1.bam --output-h2 chr20_output_H2.bam`

Part 3b: Index bam files
`samtools index chr11_output_H1.bam`
`samtools index chr11_output_H2.bam`
`samtools index chr14_output_H1.bam`
`samtools index chr14_output_H2.bam`
`samtools index chr15_output_H1.bam`
`samtools index chr15_output_H2.bam`
`samtools index chr20_output_H1.bam`
`samtools index chr20_output_H2.bam`

Part 3c: cat files
samtools cat ./chr11_new/chr11_output_H1.bam ./chr14_new/chr14_output_H1.bam ./chr15_new/chr15_output_H1.bam ./chr20_new/chr20_output_H1.bam > H1_all.bam 
samtools cat ./chr11_new/chr11_output_H2.bam ./chr14_new/chr14_output_H2.bam ./chr15_new/chr15_output_H2.bam ./chr20_new/chr20_output_H2.bam > H2_all.bam

samtools index H1_all.bam
samtools index H2_all.bam