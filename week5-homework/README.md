ChIP-Seq Data Analysis:

Part 1: Make a for loop to filter all four bam files.
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

Part 1:





