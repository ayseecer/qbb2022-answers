First thing: try not to add data files to github (so all the plink.eigenvec, integrated_call_samples.panel, etc. shouldn't be uploaded to the repo). It's not a big deal for now, but if we're wokring with large files, it starts being more of an issue.

Exercise 1: It looks like you have the output of running plink, but I don't see a README file where you wrote the actual plink command to get the eigenvector output. We do want you to keep track of the commands you run, so definitely add that to a README and upload it.

Exercise 2: Your code for this looks good and your output looks like what I would expect. Nice work! 

Exercise 3: As with Exercise 1, definitely please include the code you used to join the columns in a README, so that we can make sure you're doing the right thing, and you can keep track of it later. RE: python, it looks like you're on the right path to getting the colored figure! (You do have one colored figure in your repo `day3-homework.png`, but I don't see the code that you used to generate it, and it also doesn't necessarily look like anything I would have expected...). But, so far you've gotten to this:
```
for pop in pops:
    list_of_people_pops = np.where(vals_per_gene["pop"]==pop)
    vals_per_gene[list_of_people_pops]
```
This looks good, but we actually want to store the output of running `vals_per_gene[list_of_people_pops]` in a variable. And then we can use this variable to actually do the plot, as we did before. Definitely ask for help if you're not sure how to do this!


Really great start!
