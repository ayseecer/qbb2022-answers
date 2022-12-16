README Week14

python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
python week14.py /Users/cmdb/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197

(base) [~/qbb2022-answers/week14-homework $]'ktImportText -q ./*_krona.txt'

Question 1: In your README, briefly comment on the trends you see in the gut microbiota throughout the first week.
answer: almost all are bacteria, 0.5% are viruses. Of the bacteria, most are in the terrabacteria group

Question 2: In your README, comment on what metrics in the contigs could we use to group them together?

(base) [~/qbb2022-answers/week14-homework $]bwa index -p assembly_fasta -a is metagenomics_data/step0_givendata/assembly.fasta

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492183_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > SRR492183.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492186_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492186_2.fastq > SRR492186.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492188_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492188_2.fastq > SRR492188.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492189_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492189_2.fastq > SRR492189.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492190_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492190_2.fastq > SRR492190.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492193_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492193_2.fastq > SRR492193.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492194_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492194_2.fastq > SRR492194.mem

(base) [~/qbb2022-answers/week14-homework $]bwa mem -t 4 assembly ./metagenomics_data/step0_givendata/READS/SRR492197_1.fastq ./metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.mem

(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492183.bam -O BAM -@4 SRR492183.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492186.bam -O BAM -@4 SRR492186.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492188.bam -O BAM -@4 SRR492188.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492189.bam -O BAM -@4 SRR492189.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492190.bam -O BAM -@4 SRR492190.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492193.bam -O BAM -@4 SRR492193.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492194.bam -O BAM -@4 SRR492194.mem
(base) [~/qbb2022-answers/week14-homework $]samtools sort -o SRR492197.bam -O BAM -@4 SRR492197.mem

(metabat2) [~/qbb2022-answers/week14-homework $]jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam

(metabat2) [~/qbb2022-answers/week14-homework $]metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin

Question 3A: In your README, answer: How many bins did you get? 
answer: 6 bins

Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?

Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?

Question 3D:In your README, describe how you might estimate how complete and how contaminated each bin is?

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.1.fa 
>NODE_12_length_269228_cov_106.168966
GCCAACTTGCACATTATTGTAAGCTGACTTTCCGCCAGCTTCTGTGTTGGGGCCCACCCC
AACTTGCACATTATTGTAAGCTGACTTTCCGTCAGCTTCTGTGTTGGGGCACCGCTATAA
TTGAAAAGTTTGTTATAGGTGTATTTTCTTTTGGTTAACTATTGGTAATATAACATTGTA
GATTTTAGGATGTTGATTTTTGACTTAGCCTTTGTCTGTTTATGTTAAATGTTACAGCTA
GTCAAACATTGAGTTTGTAATTATTATATTAAGCTAGTTTAAATTTTTTGTGATTTATGT
TTTATTCATACCAATTTTGTGAAATGATACAGTGACAGATGTTTATTGATTTTAAAGGGT
GATGATGATGGCTATTGTAAATAAAGTGATAATTGTTGAAGGAAAATCTGATAAAAAAAG
GGTGCAACAGGTTATTGCAGAACCAGTCAATATTATTTGTACTCATGGAACAATGAGTAT
AGATAAGCTTGATGATATGATAGAATCACTGTATGATAAACAAGTTTTTGTATTAGCCGA

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_12_length_269228_cov_106.168966 assembly.kraken`

NODE_12_length_269228_cov_106.168966	
root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.2.fa 
>NODE_20_length_181746_cov_381.691663
AAAGAGCCTAGGACAATTCGTTTTGTCCTAAGCTCTGTTTTAATAATCATTATTTATTAG
CTGACATAAGTTTAGATTTAATACGGTCAGCTTTATTAGAATGGATTAAATTACTTTGAG
ATGCTTTGTCAACTTGTTTGATAGCAAATCTTAATAATTCATCTTTGTTTTCAGCATCAG
TAGAGATAGCTGTTTTAGCTCGTTTCACAGCTGTACGCATAGCGTTTTTCTTAGAAATAT
TTCTTTCTTCAGCTGTTTCAGTTGTTCTTACACGTTTGATTGCAGATTTAATATTTGGCA
TTACTGTCACCTCCTAAAAGTGATCATAACTTATCAAAATTTATTTGATTACAACAAGAA
ATATTTTATCAAATGTCTTATATTTGTGCAATCATTTATTTAAAAGTAACTTCATTTGAA
TTTATTACTTTTTAATTGTTGGAATGAACTACTGAACTAGATATAATAGTTATGTTAGAA
TTTACATTTAATTAATTATGTCAAAGATATATTGCATTAAAGTAATAAAAACGTTACTAT

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_20_length_181746_cov_381.691663 assembly.kraken`

NODE_20_length_181746_cov_381.691663	
root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.3.fa 
>NODE_3_length_498518_cov_181.760000
CTAACCTATAAAGTTGGCATCTCTTCTTAATTATACATCATTATTCACTTACTTTCAACA
ACTGCAAGAAAATCATCCCATATAAATTCCCTCTTAATTATACATCATTATTCACTTACT
TTTAAAAGACCTATCTTAATAGTCACTTTCTACCTGTTTTTAGCGTCACTTAATAAGCCT
ATAGGCTTATTTTCCTAAAAGCTAATTCTTTTATTCAGTTCTTGTATATTATTCAAGTGC
TAATATTCTATTTCTAAATCTTTTGAAATTTTTCATTCCAAATGTTATTCTCTTTAATAC
TTTTATTTTATTGTTAATTCCTTCTACATATCCATTTGTAAATTCGTAATCAAAACTGTT
TGATATTTGTTCTATCCAGTTCTTAAATGCTGTTAGACAGGACCTCCATTTAATGGATCC
ATCTTCTAACAGGTAAACTATCCAACCTTGTATGTTTCTTTGAGCTTTCTCTTTGTTTTC
ACTCTTCATAACTAGGTTGTAGAAGGTTTCTTTTGTTAGGTATGCTTTTCTTATTTCTTC

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_3_length_498518_cov_181.760000 assembly.kraken`

NODE_3_length_498518_cov_181.760000	
root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.4.fa 
>NODE_14_length_235766_cov_39.967778
TGAATCACTCTATCTGCTTCTGTTTTTGCTGCTTCAAGTTCATCATGAATTTTAGTCATT
TCATTATTGTATGCAGTCACGCTCGCTGGTTTCTTACCTTCGGTAACTCCCACATGATTT
AATCCTGGACGTTTTTGTTCTAACACTGACTTATCTGCTTTTAATGCATTTTTTGCTTCA
GTTAATTGAGTTAATGCTTCTTCTACTTTCGCTTTCTCATTTCTGATTTCTTCAGCTGTC
GCATCTCCATTGTTAATCACGCCTTGGGCTTCTGCACTAATTCGCTCTGCTTCTACTTTT
TTCGCTCTATAATTATCTGATGTTACTTGTGTCATTCCTGGCGTTGGATCTTGTTCTGCC
GTTGCTTCATCAAGTTGACGTTTTGCTTCAACTAAAGCACTATTATCTGCTTTATTTTGT
AGTAATGAAATTGCATGTTGAATTTTCAATGAGACATCATTAATATTATTTGTCACATTT
GCAACATCAGTATTTGTTGCTCTATCATTTGATAACACTTCATTAGCTTTTCTTCGAACT

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_14_length_235766_cov_39.967778 assembly.kraken`

NODE_14_length_235766_cov_39.967778	
root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.5.fa 
>NODE_4_length_455101_cov_112.371015
TTCCCTTGAGGACATTCGCGGTCTTGTTGACGGCACCTGCGGCACGGCGATCGTTCGCTG
AGTTCTTCCCCGATGGGCCCGCCAGCATGGTGGCATACTGGGATTAAAGCCGTTGACGTG
GTTACGGTTTTCTGGCGGGGTTTGGCATGGGACGAGATGAGCATTGGGCCGGCGATGTGT
GTAAGGAGGCGGTATTGTTGACCAGTGGTGATAACACAGCGGTTCCCGCGTCCCGGACGG
CACGACTGTCTCGCATCAGAGCTTTGATCCGGTCTGAGCAAATCTCGTCCCAGGCCGAGT
TGGCGCGCAGACTGGCCGGTGAGGGAATTGTTGTCAGCCAGGGCACGCTGTCCCGCGATC
TGAAGGATGCGGGTGCGGTACGGGGCCGAGATCATCTGGGGAATTTCCAGTACAGCATTC
CCGAGGGTGAGCATCCGTCCGACGTGACGACGGGACTGCCGGCATGGAATCATCTCGCCA
AAATATGCCATACGTTGTGTACCGAGGTGAGCTGCAACGACGGTGCAGTAGTCGTCAAGA

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_4_length_455101_cov_112.371015 assembly.kraken`

NODE_4_length_455101_cov_112.371015	
root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.6.fa 
>NODE_1_length_1447137_cov_2268.097092
AGCGCCGATTGTAGTGAAGGGTTTCCCTTTGTGAGAGTAGGACGTCGCCACGCGATTATT
CCGGCATAGCTCAGTTGGTAGTAGCGCATGACTGTTAATCATGATGTCGTAGGTTCGAGT
CCTACTGCCGGAGTTGAGCAAAAGCAAAAACCAACTTGGTTTTTGCTTTTTTTGTTTTAT
TCACTATTTTTTGATAAGCTTGAAGAAGGGACCTTAAAAACATTTATAAGATTAAAAGGA
TCCTACCGAAGAATGAATACATCAAATTTTAGCTATGGTATAATGTGTTTATTATAGTTA
GTAAAGCAGAAAAGGAGGAGCGGGTTTGAAAATATTGTTATATTTTGAAGGTGAGAAAAT
CTTAGCTAAATCAGGTATTGGTCGAGCATTAGATCACCAGAAACGAGCGCTCTCTGAAGT
TGGAATAGAATATACATTAGATGCTGATTGCAGTGACTATGATATATTGCATATTAATAC
ATACGGCGTAAATAGCCATCGTATGGTCAGAAAAGCACGCAAACTAGGAAAAAAAGTTAT

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_1_length_1447137_cov_2268.097092 assembly.kraken`

NODE_1_length_1447137_cov_2268.097092	
root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF

Question 4: 
(A) Within your README, record your predictions for each bin?
(B) This approach to classification is fast, but not very quantitative. Within your README, propose one method to more robustly infer the taxonomy of a metagenomic bin.
