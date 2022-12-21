Great start, Ayse! Just a few more things we need before this is complete:

1. Missing answer to Question 2 (-0.5 point)
2. Missing answers and any code you used for Question 3 (-3 points)
3. You've got a start for Question 4, but we want to look at the taxonomy of ALL contiigs within each bin, not just the first contig. How might we do this with code? Also, we want to look at the breakdown at specific levels of the taxonomy, so we want to grab specific parts of the taxonomy string. How could we do that? We need answers for both 4A and 4B. (-1 point)

(5.5/10)

REGRADE 12/21/22 -- Dylan

Great work Ayse! Question 3 looks great! As do questions 2 and 4B. Still missing the rest of 4A but great work on this (-0.5 point)

If you are interested in how you might do 4A, I would suggest--for each bin-- use a for loop to loop through each of the contigs in that bin. And then you can grep each of those contigs against `assembly.kraken`. Something like this:

```
for contig_id in $(grep ">" bin.1.fa |  cut -d ">" -f 2)
do
    grep $contig_id assembly.kraken
done
```

Then, we could pipe the output of that for loop to a couple of `cut` commands to get the taxonomic information we're interested in. If you haven't seen the `$()` structure before, it essentially allows you "capture" the output of running a command, where you can store it in a variable, or in this case, loop through it.

Anyways, great work!

(9.5/10)
