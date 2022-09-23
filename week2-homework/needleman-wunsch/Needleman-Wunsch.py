#!/usr/bin/env python3

import sys
from fasta import readFASTA
import numpy as np

#HOXD70 is the DNA, BLOSUM62 is the aminoacid sequences

fasta_file = sys.argv[1]
blosum_matrix = sys.argv[2]
gap_penalty = float(sys.argv[3]) #should be negative 
alignment_outfile = sys.argv[4]

# reading in actual sequences (mouse vs human)
input_sequences = readFASTA(open(fasta_file))

sequence1 = input_sequences[0][1] #human
sequence2 = input_sequences[1][1]#mouse

#read the scoring matrix into a numpy array

aa_dict = {}
scoring_list = []

for i, line in enumerate(open(blosum_matrix)):
    fields = line.strip().split()
    if i == 0:
        for position, aa in enumerate(fields):
            aa_dict[aa] = position
        continue
    scoring_list.append([float(string) for string in fields[1:]])

scoring_matrix = np.array(scoring_list)
        
    
F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))  
T_matrix = np.empty((len(sequence1)+1, len(sequence2)+1), dtype=str) #trace back matrix to look back at what score was chosen as the maximum essentially

for i in range(len(sequence1)+1): #initialize the F_matrix
    F_matrix[i,0] = i * gap_penalty
    
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty

for i in range(len(sequence1)+1): #initialize the T_matrix 
    T_matrix[i,0] = 'h'
    
for j in range(len(sequence2)+1):
    T_matrix[0,j] = 'v'

for i in range(1, len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
        d = F_matrix[i-1,j-1] + scoring_matrix[aa_dict[sequence1[i-1]], aa_dict[sequence2[j-1]]]
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        
        F_matrix[i,j] = max(d,h,v)
        if d == F_matrix[i,j]:
            T_matrix[i,j] = "d"
        elif h == F_matrix[i,j]:
            T_matrix[i,j] = "v"
        else:
            T_matrix[i,j] = "h"

#alignment_outfile = sys.argv[4] I have this above

i = len(sequence1)
j = len(sequence2)
alignment1 = ""
alignment2 = ""
while (i!=0 or j!=0):
    if T_matrix[i, j] == "d":
        alignment1 += sequence1[i-1]
        alignment2 += sequence2[j-1]
        i = i-1
        j = j-1
        continue
    if T_matrix[i,j] == "h":
        alignment1 += "-"
        alignment2 += sequence2[j-1]
        j = j - 1
        continue
    if T_matrix[len(sequence1), len(sequence2)] == "v":
        alignment1 += sequence1[i-1]
        alignment2 += "-"
        i = i - 1
        continue

#MAKE SURE TO SWITCH THE ALIGNMENT ORDER BECAUSE IT IS BACKWARDS RIGHT NOW!





        


    
