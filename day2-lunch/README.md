QBB2022 - Day 2 - Lunch Exercises Submission

Exercise 1: 

Line 57 appears malformed
Line 185 appears malformed
Line 193 appears malformed

Edited script:

#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, int, int, int, int] #create a list of appropriate file types that you can later refer to
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if not (fieldN >= 3 or fieldN <= 9 or fieldN == 12):
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        try:
            for j in range(min(len(field_types), len(fields))): #len(field_types) = 12, = range(9) = range(0,9) -> 0,1,2,3,4,5,6,7,8 - telling j to go number by number in this range 
                if j == 8 or j == 10 or j ==11:
                    h = fields[j].strip(",")
                    x = h.split(",")
                    intlist = [int(n) for n in x] 
                    fields[j] = intlist
                    
                else: 
                    fields[j] = field_types[j](fields[j])

            assert(len(fields[10]) == fields[9])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
             
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)


Exercise 2: Median number of exons was outputted to be 4.

import bed_parser
bed_file = bed_parser.parse_bed("hg38_gencodev41_chr21.bed") #myfilename.(functionname) 
#print(bed_file[0])

number_of_exons = [] #creates an empty list 

for i in bed_file:
    number_of_exons.append(i[9]) #appends the empty list by adding the nineth (indexed) column integers and storing it as a list.

number_of_exons.sort() #sorts the number_of_exons list of exon numbers in ascending order.

print(number_of_exons[len(number_of_exons)//2])


 