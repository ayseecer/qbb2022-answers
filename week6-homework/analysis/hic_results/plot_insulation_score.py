#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def main():
    # python heatmap.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap1.pdf
    
#read in the data
#log transform the data
#convert it into a matix
dCTCF_full.40000.matrix, 40000_bins.bed, 

    in1_fname, bin_fname, out_fname = sys.argv[1:3]
    insulation_score1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start_bin = 54878
    end_bin = 54951 
    frags(start bin end bin etc)
    #tell frags to keep the data between these bins. go to the file and grab these
    #define start and end here
    n = end_bin - start_bin
    
    data1 = filter(data1, start_bin, end_bin) #subset data1, log transform, do sparse_to_mat, use the 2 given functions from the hw assignment
    matrix_data1 = sparse_to_matrix(data1, n)
    removed_matrix_data1 = remove_dd_bg(matrix_data1)
    smooth_removed_matrix_data1 = smooth_matrix(removed_matrix_data1)
    #numpy.mean(mat[(i - 5):i, i:(i + 5)])
    vmin = max(numpy.amax(smooth_removed_matrix_data1), numpy.amax(smooth_removed_matrix_data2))
    vmax = 0
    
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    #ax[0].imshow(-smooth_removed_matrix_data1, vmax=vmax, vmin=vmin, color='Magma') something similar + set labels etc.
    #ax[1].plot (calculate the insulation score - should just be the score column from before)
    plt.margins(x=0)
    ax[1].set_xlim(10400000, 13400000)
    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0) 
                
main()



