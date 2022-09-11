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

Question 2. De novo assembly

Using the data described in the Data section above, assemble the reads using Spades.

Question 2.1. How many contigs were produced? [Hint: try grep -c '>' contigs.fasta]

Question 2.2. What is the total length of the contigs? [Hint: try samtools faidx, plus a short script if necessary]

Question 2.3. What is the size of your largest contig? [Hint: check samtools faidx plus sort -n]

Question 2.4. What is the contig N50 size? [Hint: Write a short script if necessary]


Question 3. Whole Genome Alignment

Use MUMmer for whole genome alignment.

Question 3.1. What is the average identify of your assembly compared to the reference? [Hint: try dnadiff]

Question 3.2. What is the length of the longest alignment [Hint: try nucmer and show-coords]

Question 3.3. How many insertions and deletions are in the assembly? [Hint: try dnadiff]


Question 4. Decoding the insertion

Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. [Hint: try show-coords]

Question 4.2. How long is the novel insertion? [Hint: try show-coords]

Question 4.3. What is the DNA sequence of the encoded message? [Hint: try samtools faidx to extract the insertion]

Question 4.4. What is the secret message? [Hint: Run the provided script dna-decode.py to decode the string from 4.3.]