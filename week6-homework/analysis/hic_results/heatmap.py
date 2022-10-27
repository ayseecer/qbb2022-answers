#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def filter(raw_data, start_bin, end_bin): 
    # Filter out data with one or both interaction ends falling outside the desired bin range. Filter raw data to be just the data you want to use which is 11170245-12070245(chr15) and save it in filter_data.
    filter_data = numpy.where(raw_data['F1'] >= start_bin, ['F2'] < end_bin)
    # set the minimum F1 value to 0 and minimum F2 value to 0
    # minus the smallest value of F1 from all values of F1 (the smallest possibel is start_bin)
    filter_data['F1'] -= start_bin # shift the data by subtracting the min value so the new min value is zero
    filter_data['F2'] -= start_bin # shift the data by subtracting the min value so the new min value is zero
    filter_data['score'] = numpy.log10(filter_data['score']) # Log-transform the scores and save it in log_data.
    filter_data['score'] -= numpy.amin(filter_data['score']) # shift the data again for score.
    return filter_data
    
def sparse_to_matrix(sparse, n): #n is the length of the genomic region (n = end_bin - start_bin)
    mat = numpy.zeros((n, n), dtype=float) # create mat (an empty matrix) 
    #fill in the matrix use sparse. ~2 lines of code.
    #mat[sparse['F1'][i], sparse['F2'][i]] = sparse['score'][i] # this is the line they gave you don't use this
    mat[sparse['F1'], sparse['F2']] = sparse['score'] #two inputs to find a quandrant and put score there.
    mat[sparse['F2'], sparse['F1']] = sparse['score'] #for mirror image
    return mat
    
# Plot the two matrices using the same maximum value (set vmax in imshow). 
# I suggest using the magma color map, although you need to flip your scores to mimic the paper figure

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2
    
def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

def main():
    # python heatmap.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed heatmap1.pdf
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
    n = end_bin - start_bin
    
    data1 = filter(data1, start_bin, end_bin)
    matrix_data1 = sparse_to_matrix(data1, n)
    removed_matrix_data1 = remove_dd_bg(matrix_data1)
    smooth_removed_matrix_data1 = smooth_matrix(removed_matrix_data1)
    
    data2 = filter(data2, start_bin, end_bin)
    matrix_data2 = sparse_to_matrix(data2, n)
    removed_matrix_data2 = remove_dd_bg(matrix_data2)
    smooth_removed_matrix_data2 = smooth_matrix(removed_matrix_data2) 
    
    matrix3 = smooth_removed_matrix_data2 - smooth_removed_matrix_data1
    
    vmin = max(numpy.amax(smooth_removed_matrix_data1), numpy.amax(smooth_removed_matrix_data2))
    vmax = 0
    
    fig, ax = plt.subplots(1,3) # initialize your fix,ax
    ax[0].imshow(-smooth_removed_matrix_data1, vmax=vmax, vmin=vmin, color='Magma')                           
    ax[0].axis('off')
    ax[1].imshow(-smooth_removed_matrix_data2, vmax=vmax, vmin=vmin, color='Magma')
    ax[1].axis('off')
    ax[2].imshow(matrix3, color='seismic', norm=colors.CenteredNorm) #removes the distance dependent signal and smooths the data first as there is noise.
    ax[2].axis('off')
    plt.savefig(out_fname)
    
main()