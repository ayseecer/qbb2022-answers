#QB2022 Week 1 Homework

######Question 1.1. How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?
1Mbp x 5x = 5Mbp of data
5Mbp / 100 bp / read = 50000 reads for 5x coverage

1Mbp x 15x = 5Mbp of data
15Mbp / 100 bp / read = 150000 reads for 15x coverage

######Question 1.2. Write a program to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads and plot the histogram of coverage. Note you do not need to actually output the sequences of the reads, you can just randomly sample positions in the genome and record the coverage. You do not need to consider the strand of each read. The start position of each read should have a uniform random probabilty at each possible starting position (1 through 999,901). You can record the coverage in an array of 1M positions. Overlay the histogram with a Poisson distribution with lambda=5

Submitted script and two plots to GitHub.

######Question 1.3. Using the histogram from Q1.2, how much of the genome has not been sequenced (has 0x coverage)? How well does this match Poisson expectations?

less than 5% of the genome seems to not be sequenced (has 0x coverage) and the Poisson distribution mathes pretty well with that assumption (however the predictions are not as good for the middle of the distribution).

######Question 1.4. Now repeat the analysis with 15x coverage: 1. simulate the appropriate number of reads, 2. make a histogram, 3. overlay a Poisson distribution with lambda=15, 4. compute the number of bases with 0x coverage, and 5. evaluate how well it matches the Poisson expectation.

The Poisson distribution got less accurate compared to the 5X coverage Poisson distribution. The number of bases with 0x coverage is 0, and the Poisson predicts that pretty well.

######Question 2. De novo assembly: using the data described in the Data section above, assemble the reads using Spades.

######Question 2.1. How many contigs were produced? [Hint: try grep -c '>' contigs.fasta]

Ran this bash command to get the answer 4 contigs were produced:
`[~/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm $] grep -c '>' contigs.fasta`


######Question 2.2. What is the total length of the contigs? [Hint: try samtools faidx, plus a short script if necessary]

Ran this bash command to get the output file of contigs.fasta.fai which gave me the lengths of each contig in column 2: `samtools faidx contigs.fasta`

NODE_1_length_105830_cov_20.649193      105830  36      60      61
NODE_2_length_47860_cov_20.367392       47860   107665  60      61
NODE_3_length_41351_cov_20.528098       41351   156358  60      61
NODE_4_length_39426_cov_20.336388       39426   198434  60      61

######Question 2.3. What is the size of your largest contig? [Hint: check samtools faidx plus sort -n]

The largest contig is the first one (NODE_1_length_105830_cov_20.649193) with a size of 105830 bases.

######Question 2.4. What is the contig N50 size? [Hint: Write a short script if necessary]

Ran this bash command to get the output file of ref.fa.fai which gave me the length of the reference genome:`samtools faidx ref.fa`
Halomonas       233806  11      70      71

To get the N50 I found that the second largest contig length would surpass the halfway mark of the length of the reference genome which is 233806/2 = 116903, so N50 is 47860. 

######Question 3.1. What is the average identify of your assembly compared to the reference? [Hint: try dnadiff]

Ran this bash command to get these files: `dnadiff /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta`

Which gave me the outputs...
   out.report  - Summary of alignments, differences and SNPs
   out.delta   - Standard nucmer alignment output
   out.1delta  - 1-to-1 alignment from delta-filter -1
   out.mdelta  - M-to-M alignment from delta-filter -m
   out.1coords - 1-to-1 coordinates from show-coords -THrcl .1delta
   out.mcoords - M-to-M coordinates from show-coords -THrcl .mdelta
   out.snps    - SNPs from show-snps -rlTHC .1delta
   out.rdiff   - Classified ref breakpoints from show-diff -rH .mdelta
   out.qdiff   - Classified qry breakpoints from show-diff -qH .mdelta
   out.unref   - Unaligned reference sequence IDs and lengths
   out.unqry   - Unaligned query sequence IDs and lengths

When I checked my week1-homework directory, I saw the additional out.1coords, out.1delta, out.delta, outmcoords, out.mdelta, out.qdiff, out.rdiff, out.report, and out.snps. When I did less -S on out.report, I saw that the average identity of my assembly compared to the reference was 99.9955.

######Question 3.2. What is the length of the longest alignment [Hint: try nucmer and show-coords]

Ran this bash command to get the file out.delta:
`nucmer /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/contigs.fasta`

This step produces out.delta. How can we make it obvious that `out.delta` was literally the OUTPUT of `nucmer .fa .fasta` ? 
`mkdir nucmer_out`
`mv out.delta nucmer_out`

(show-coords displays a summary of the coordinates, percent identity, etc. of the alignment regions) 
Then you want to use show-coords to do... 
`show-coords /Users/cmdb/qbb2022-answers/week1-homework/nucmer_out/out.delta > show_coords_out.out` (do cat show_coords_out.out to see)

The output format of out-coords has:
[LEN 1] length of the alignment region in the reference sequence 
[LEN 2] length of the alignment region in the query sequence

which happen to be the same for all (meaning no insertions or deletions to change the alignment length etc.)

So, the longest alingment would be 105830 bases long.

######Question 3.3. How many insertions and deletions are in the assembly? [Hint: try dnadiff]

(Note: ls -lt gives time created, ls -lh gives the file size in ways "humans" can understand) 

`dnadiff /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/SPAdes-3.15.5-Darwin/bin/asm/out.snps`

I made a directory using `mkdir dnadiff_outputs` and moved all files starting with "out" (which are the outputs of dnadiff) into the directory using `mv out.* dnadiff_outputs` for organization purposes.

Then I checked the out.reports file since it was the most general output of dnadiff, and found that 710 bases (0.3028%) of the assembly (query) was unaligned, which refers to insertions and deletions.

######Question 4. Decoding the insertion

Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. [Hint: try show-coords]

Question 4.2. How long is the novel insertion? [Hint: try show-coords]

Question 4.3. What is the DNA sequence of the encoded message? [Hint: try samtools faidx to extract the insertion]

Question 4.4. What is the secret message? [Hint: Run the provided script dna-decode.py to decode the string from 4.3.]