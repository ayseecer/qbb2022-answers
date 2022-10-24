# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 0.5 + 1 + 1 + 1 + 0.5 + 1 = 9 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * fantastic! --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * very good --> +1

4. variant call with freebayes

  * perfect! --> +1

5. filter variants

  * I see what you're going for here, but you want to use `QUAL > 20` as your filter criteria. [A PHRED score of 20 corresponds to a base call accuracy of 99%](https://en.wikipedia.org/wiki/Phred_quality_score)
  * --> +0.5

6. decompose complex haplotypes

  * good --> +1

7. variant effect prediction

  * good --> +1

8. python plotting script

  * you plot `read_depth` in three different histograms rather than plotting `quality_distribution` and `allele_freq` in the second and third histograms respectively
  * --> +1

9. 4 panel plot (0.25 points each panel)

  * I would expect the allele frequencies to be between 0 and 1, not super huge numbers, but I can see what happened given your python script. See notes above. (this also explains why the three histograms look the same)
  * --> +0.5

10. 1000 line vcf

  * --> +1
