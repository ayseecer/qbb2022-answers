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
