#!/usr/bin/env python
import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def sparse_to_matrix(sparse, n):
    mat = numpy.zeros((n, n), dtype=float)
    mat[sparse['F1'], sparse['F2']] = sparse['score'] 
    mat[sparse['F2'], sparse['F1']] = sparse['score'] 
    return mat

def main():
# python plot_insulation_score.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/matrix/dCTCF_full.40000.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/matrix/40000_bins.bed insulation_score_plot.pdf

    in1_fname, bin_fname, out_fname = sys.argv[1:4]
    insulation_score1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
        
    insulation_score1['score'] = numpy.log10(insulation_score1['score']) 
    insulation_score1['score'] -= numpy.amin(insulation_score1['score']) 

    chrom = b'chr15'
    start_bin = 54878
    end_bin = 54951 
    start_bin = frags['start']
    end_bin = frags['end']
    n = end_bin - start_bin
    
    sparse_to_matrix(insulation_score1, n)
    numpy.mean(mat[(n - 5):n, n:(n + 5)])
    
    data1 = filter(data1, start_bin, end_bin) 
    matrix_data1 = sparse_to_matrix(data1, n)
    removed_matrix_data1 = remove_dd_bg(matrix_data1)
    smooth_removed_matrix_data1 = smooth_matrix(removed_matrix_data1)
    vmin = -1*max(numpy.amax(smooth_removed_matrix_data1), numpy.amax(smooth_removed_matrix_data2))
    vmax = 0
    
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    ax[0].imshow(-insulation_score1, vmax=vmax, vmin=vmin, cmap='magma')
    ax[1].plot('score')
    plt.margins(x=0)
    ax[1].set_xlim(10400000, 13400000)
    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0) 
                
main()



