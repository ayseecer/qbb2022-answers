This is a really great start! Everything you have so far looks good. Just a few more things until it's complete:
1. You'll want to re-run the regression not including sex as a covariate. Just modify your regressiong formula a little bit. (-0.5 point)
2. After that, get the list of transcripts that are signficant at a 10% FDR for both models: the one with sex as a covariate, and the one without. Looks like you already got started on this. Then, quantify the amount of overlap between the two sets (-1 point)
3. Generate a volcano plot for the model with sex as a covariate. For this, you'll also need the betas from the regression model, not just the pvalues. Try `statmodel_out.params["stage"]` (-1 point)

Excellent start!
(7.5/10)
