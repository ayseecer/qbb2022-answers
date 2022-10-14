ChIP-Seq Data Analysis:

Part 1: make a for loop to filter all four bam files.
`for file in D2_Sox2_R1 D2_Sox2_R1_input D2_Sox2_R2 D2_Sox2_R2_input; do samtools view ${file}.bam -q 10 -b > ${file}_filtered.bam; done`

Part 2:
`macs2 callpeak -t D2_Sox2_R1_filtered.bam -c D2_Sox2_R1_input_filtered.bam -g 95000000 -n D2_Sox2_R1 -B`
`macs2 callpeak -t D2_Sox2_R2_filtered.bam -c D2_Sox2_R2_input_filtered.bam -g 95000000 -n D2_Sox2_R2 -B`

Part 3:
`bedtools intersect -a D2_Sox2_R1_peaks.narrowPeak -b D2_Sox2_R2_peaks.narrowPeak -wa > D2_Sox2_intersected_peaks.bed`

Part 4:
`bedtools intersect -a D2_Sox2_intersected_peaks.bed -b D2_Klf4_peaks.bed -wa > Sox2_Klf4_intersected_peaks.bed`
`wc -l D2_Klf4_peaks.bed` showed 60 peaks and `wc -l Sox2_Klf4_intersected_peaks.bed` showed 41 peaks, so 41/60 = 68% in Klf4 were also in Sax2.

`wc -l D2_Sox2_R1_peaks.narrowPeak` = 765 peaks
`wc -l D2_Sox2_R2_peaks.narrowPeak` = 1318 peaks

Part 5: File name is plot.py and is uploaded on github.

`python scale_bdg.py D2_Sox2_R1_treat_pileup.bdg D2_Sox2_R1_treat_pileup_scaled.bdg`
`python scale_bdg.py D0_H3K27ac_treat.bdg D0_H3K27ac_treat_scaled.bdg`
`python scale_bdg.py D2_H3K27ac_treat.bdg D2_H3K27ac_treat_scaled.bdg`
`python scale_bdg.py D2_Klf4_treat.bdg D2_Klf4_treat_scaled.bdg`

`awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_Sox2_R1_treat_pileup_scaled.bdg > D2_Sox2_R1_treat_pileup_scaled_cropped.bdg`
`awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0_H3K27ac_treat_scaled.bdg > D0_H3K27ac_treat_scaled_cropped.bdg`
`awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_H3K27ac_treat_scaled.bdg > D2_H3K27ac_treat_scaled_cropped.bdg`
`awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_Klf4_treat_scaled.bdg > D2_Klf4_treat_scaled_cropped_.bdg`

Motif Discovery:

Prep Part: ran `conda activate meme`, `conda install -c conda-forge openmpi=4.1.4 -y`, and `ln -s /Users/cmdb/data/genomes/mm10.fa ./`.

Part 1: ran `sort -k 5 -r -n D2_Sox2_intersected_peaks.bed > D2_Sox2_intersected_peaks_sorted.bed` to sort the 5th column in reverse order.

Part 2: ran `head -n 300 D2_Sox2_intersected_peaks_sorted.bed > D2_Sox2_intersected_peaks_sorted_head300` to sort store the top 300 lines in another file.

Part 3: ran `awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' D2_Sox2_intersected_peaks_sorted_head300 > D2_Sox2_intersected_peaks_sorted_head300_awk.txt` to reformat the 300 lines so they can be used as input to samtools faidx.

Part 4: ran `samtools faidx -o peaks.fa mm10.fa -r D2_Sox2_intersected_peaks_sorted_head300_awk.txt` to extract the sequences of these peaks from the mm10 reference genome into a fasta file. Used -r to reformat the input file to chr:from-to, one per line.

Part 5: ran `meme-chip -maxw 7 peaks.fa -oc MEME_output` to perform motif finding in these strongest 300 peaks from Sox2 with motif widths up to 7bp (using -maxw).

Motif Identification:

Part 1: scanned my motifs using the command `tomtom combined.meme /Users/cmdb/Downloads/motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme`

Part 2: opened my tomtom.html file and saw that I got 108 matches.