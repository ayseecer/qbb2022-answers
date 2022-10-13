#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy

def load_data(fname):
    # Load in the bedgraph with columns chr, start, end, and score
    bg = numpy.loadtxt(fname, usecols=(1,2,3), dtype=numpy.dtype([
        ('start', int), ('end', int), ('score', float)]))
    # Find the lowest coordinate
    start = bg['start'][0]
    # Create an array at bp resolution
    array = numpy.zeros(bg['end'][-1] - start, dtype=numpy.dtype(
        [('pos', int), ('score', float)]))
    # For each line in the bedgraph, set positions across range with score
    for i in range(bg.shape[0]):
        array['score'][bg['start'][i] - start:bg['end'][i] - start] = bg['score'][i]
    # Set coordinates in array
    array['pos'] = numpy.arange(start, start + array.shape[0])
    # Bin array into 100bp bins
    hist = numpy.histogram(array['pos'], weights=array['score'], bins=(array.shape[0] // 100))
    # Create final data dict
    X = (hist[1][1:] + hist[1][:-1]) / 2
    Y = hist[0]
    data = {'X': X, 'Y':Y}
    return data
    
def main():
    #produce and save a 4 panel plot
    # name the things you're reading in (e.g., sox2 filename, kl4file name, etc) using the above function 
    sox2, klf4, D0_H3K27ac, D2_H3K27ac = sys.argv[1:5]
    # make an empty data structure for your data
    data = []
    # make a dummy maxval to start with 
    maxval = 0
    # add data from each file to the list, and set the max value for the plot based on the Y information from each file 
    for filename in [sox2, klf4, D0_H3K27ac, D2_H3K27ac]:
        data.append(load_data(filename))
        # create a variable for the maximum value for your y axis based on figure K from the 2019 paper 
        maxval = max(maxval, numpy.amax(data[-1]['Y'])) # take the amax (max) of the array, data
        # add a print statement below to print different subsets of data, e.g., data[-1]['X'] in the for loop
    labels = ["Sox2", "Klf4", "D0_H3K27ac", "D2_H3K27ac"] # make the y axis labels (based on the things you're reading in)
    #make a list of the labels that I want
    fig, ax = plt.subplots(4) # initialize your fix,ax
    for i in range(len(data)):
        ax[i].set_ylim((0, maxval))
        ax[i].fill_between(data[i]["X"], data[i]["Y"], color = "black") #if this doesn't work separate the two slack
        ax[i].set_ylabel(labels[i])
        
    # write some script that goes through each of the 4files you've read in, and name their axis labels and tick parks 
    
    # set layout (e.g., tight layout) and save fig 
    plt.suptitle("ChIP-Seq Data")
    plt.show()
    plt.tight_layout()
    plt.savefig("ChIP_Seq_Data.png")


# outside the function, call main (so the function will be executed)

main()
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    