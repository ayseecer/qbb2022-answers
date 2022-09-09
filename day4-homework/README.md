Day 4 Homework

Part A: the inside of the function numpy.arange(0.55, 1.05, 0.05) is saying create an array that starts from 0.55 and ends at 1.05 that contains numbers incrementing with 0.05. It also won't include 1.05, so it will stop at 1. When I print(prob_heads), I run it in terminal and see the aformentioned array: [1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]. The numpy.around( ,decimals=2 should be evenly rounding numbers to the given number of decimals, which is 2. When I print(numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)) and run it in terminal I get the array: [0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]


Part C: I see that in the non-corrected heatmap as the number of tosses increase the power decreases and the trend is less obvious/intense in the corrected heatmap. Power also seems to decrease as the probability of heads increase; however, the corrected heatmap shows no significant trend.