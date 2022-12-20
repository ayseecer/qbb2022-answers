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
answer:

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
answer: 6 bins (bin.1.fa	bin.2.fa	bin.3.fa	bin.4.fa	bin.5.fa	bin.6.fa)

Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?
answer:  13407206/38071689 = 35.2%

Run: Getting us the number of contigs across all bins.
for i in {1..6};
do cat bin.${i}.fa; done | grep ^">" | wc -l
Ran: 197
 
Getting us the number of bases in the assembly.
(base) [~/qbb2022-answers/week14-homework $]cat depth.txt | awk '{ sum+=$2} END {print sum}'
38071689

Getting us the number of bases across all 6 bins (197 contigs).
(base) [~/qbb2022-answers/week14-homework/bins_dir $]for i in {1..6};
> do cat bin.${i}.fa; done | grep -v ^">" | wc -c
 13407206

Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?

answer: Yes, because the bins are less than 5 Mb which is expected of the prokaryotic genome. In fact, the larger contigs made it into the bins.
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
answer: We could use coverage. We could look at the ratio of the bases or specifically GC content.

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
answer: 6 bins (bin.1.fa	bin.2.fa	bin.3.fa	bin.4.fa	bin.5.fa	bin.6.fa)

Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?
answer:  13407206/38071689 = 35.2%

Run: Getting us the number of contigs across all bins.
for i in {1..6};
do cat bin.${i}.fa; done | grep ^">" | wc -l
Ran: 197
 
Getting us the number of bases in the assembly.
(base) [~/qbb2022-answers/week14-homework $]cat depth.txt | awk '{ sum+=$2} END {print sum}'
38071689

Getting us the number of bases across all 6 bins (197 contigs).
(base) [~/qbb2022-answers/week14-homework/bins_dir $]for i in {1..6};
> do cat bin.${i}.fa; done | grep -v ^">" | wc -c
 13407206

Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?
answer: Yes, because the bins are less than 5 Mb which is expected of the prokaryotic genome.
Largest Bin: 2910568
Smallest Bin: 1248387

(base) [~/qbb2022-answers/week14-homework/bins_dir $]for i in {1..6}; do echo "bin ${i}"; grep -v ^">" bin.${i}.fa | wc -c; done
bin 1
 2750133
bin 2
 2289418
bin 3
 1683638
bin 4
 1248387
bin 5
 2525062
bin 6
 2910568

Question 3D:In your README, describe how you might estimate how complete and how contaminated each bin is?
answer: I can look at the BLAST database and see how well it compares to previously sequenced prokaryotic genomes. If it's not comlete the seqeucnes could be on the shorter side, and if it's contaminated the sequences could be longer.

(metabat2) [~/qbb2022-answers/week14-homework/bins_dir $]head bin.1.fa 
>NODE_12_length_269228_cov_106.168966
GCCAACTTGCACATTATTGTAAGCTGACTTTCCGCCAGCTTCTGTGTTGGGGCCCACCCC
AACTTGCACATTATTGTAAGCTGACTTTCCGTCAGCTTCTGTGTTGGGGCACCGCTATAA

(metabat2) [~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN $]`grep NODE_12_length_269228_cov_106.168966 assembly.kraken`

NODE_12_length_269228_cov_106.168966	
root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

Question 4: 
(A) Within your README, record your predictions for each bin? 
(B) This approach to classification is fast, but not very quantitative. Within your README, propose one method to more robustly infer the taxonomy of a metagenomic bin.
answer: you can use BLAST to get a score for the sequence alignment. This score is a more quantitative measure of predicition which bin belongs to which species of bacteria.