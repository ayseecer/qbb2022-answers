Part 0: 
`conda create -n medaka medaka`
`conda activate medaka`
`sudo /usr/bin/xcode-select --install`
`pip install whatshap==1.0`
`curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/ont_data.tar.gz --output ont_data.tar.gz
tar xzf ont_data.tar.gz`
`cp /Users/cmdb/data/genomes/hg38.fa ./`

Part 1: Region specifics were found in regions.bed
`medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11 -p chr11_phased.vcf`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14 -p chr14_phased.vcf`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15 -p chr15_phased.vcf`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20 -p chr20_phased.vcf`

Part 2: Mark reads with the correct haplotype tag
`whatshap haplotag -o chr11_phased.bam --reference hg38.fa --regions chr11:1900000:2800000 round_0_hap_mixed_phased.vcf.gz round_0_hap_mixed_phased.bam --output-haplotag-list Haplotag_List`

== SUMMARY ==
Total alignments processed:                      4063
Alignments that could be tagged:                 3323
Alignments spanning multiple phase sets:            0

`whatshap haplotag -o chr14_phased.bam --reference hg38.fa --regions chr14:100700000:100990000 round_0_hap_mixed_phased.vcf.gz round_0_hap_mixed_phased.bam --output-haplotag-list Haplotag_List`

== SUMMARY ==
Total alignments processed:                      1439
Alignments that could be tagged:                 1303
Alignments spanning multiple phase sets:            0

`whatshap haplotag -o chr15_phased.bam --reference hg38.fa --regions chr15:23600000:25900000 round_0_hap_mixed_phased.vcf.gz round_0_hap_mixed_phased.bam --output-haplotag-list Haplotag_List`

== SUMMARY ==
Total alignments processed:                     10395
Alignments that could be tagged:                 8000
Alignments spanning multiple phase sets:            0

`whatshap haplotag -o chr20_phased.bam --reference hg38.fa --regions chr20:58800000:58912000 round_0_hap_mixed_phased.vcf.gz round_0_hap_mixed_phased.bam --output-haplotag-list Haplotag_List`

== SUMMARY ==
Total alignments processed:                       648
Alignments that could be tagged:                   87
Alignments spanning multiple phase sets:            0

Part 3:
`whatshap split --output-h1 chr11_output_H1.bam --output-h2 chr11_output_H2.bam --output-untagged chr11_output_untagged.bam chr11_phased.bam Haplotag_List`

Total number of reads in haplotag list: 4063
Total number of haplo-tagged reads: 3323
Total number of untagged reads: 740
[E::idx_find_and_load] Could not retrieve index file for 'chr11_phased.bam'

== SUMMARY ==
Total reads processed: 4063
Number of output reads "untagged": 740
Number of output reads haplotype 1: 1625
Number of output reads haplotype 2: 1698
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 0

`whatshap split --output-h1 chr14_output_H1.bam --output-h2 chr14_output_H2.bam --output-untagged chr14_output_untagged.bam chr14_phased.bam Haplotag_List`

Total number of reads in haplotag list: 1439
Total number of haplo-tagged reads: 1303
Total number of untagged reads: 136
[E::idx_find_and_load] Could not retrieve index file for 'chr14_phased.bam'

== SUMMARY ==
Total reads processed: 1439
Number of output reads "untagged": 136
Number of output reads haplotype 1: 638
Number of output reads haplotype 2: 665
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 0

`whatshap split --output-h1 chr15_output_H1.bam --output-h2 chr15_output_H2.bam --output-untagged chr15_output_untagged.bam chr15_phased.bam Haplotag_List`

Total number of reads in haplotag list: 10395
Total number of haplo-tagged reads: 8000
Total number of untagged reads: 2395
[E::idx_find_and_load] Could not retrieve index file for 'chr15_phased.bam'

== SUMMARY ==
Total reads processed: 10395
Number of output reads "untagged": 2395
Number of output reads haplotype 1: 3996
Number of output reads haplotype 2: 4004
Number of unknown (dropped) reads: 0

Total number of reads in haplotag list: 648
Total number of haplo-tagged reads: 87
Total number of untagged reads: 561
[E::idx_find_and_load] Could not retrieve index file for 'chr20_phased.bam'

== SUMMARY ==
Total reads processed: 648
Number of output reads "untagged": 561
Number of output reads haplotype 1: 43
Number of output reads haplotype 2: 44
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 0

Part 3b: Create a .bai index using samtools index
`samtools index chr11_output_H1.bam`
`samtools index chr11_output_H2.bam`
`samtools index chr14_output_H1.bam`
`samtools index chr14_output_H2.bam`
`samtools index chr15_output_H1.bam`
`samtools index chr15_output_H2.bam`
`samtools index chr20_output_H1.bam`
`samtools index chr20_output_H2.bam`

Part 4: Setting up IGV
`conda deactivate`
`conda create -n igv gradle openjdk=11 -y`
`conda activate igv`
`git clone https://github.com/igvteam/igv.git`
`cd igv`
`./gradlew createDist`
`cd ../`
`ln -s ${PWD}/igv/build/IGV-dist/igv.sh ./`
`./igv.sh`

Part 5: Configuring IGV for differential methylation





