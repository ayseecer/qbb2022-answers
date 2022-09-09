#!/usr/bin/env python3

import sys # package that allows us to read in input from the command line (ex: vcf files)

def parse_vcf(fname): # defining a new function called parse_vcf and it takes an argument called "fname"
    vcf = [] #creates an empty list called "vcf" to store the VCF information
    info_description = {} #creates a dictionary
    info_type = {} #creates a dictionary
    format_description = {} #creates a dictionary
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
    } #allows us to use information from the header to tell python what data types to expect
    malformed = 0 #initialize the variable to count number of malformed VCF files
#trying to open the VCF files; if it doesn't work, tell the user
    try:
        fs = open(fname) #creating a variable called fs, which is storing the opened vcf file
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) #error message for user

    for h, line in enumerate(fs): #loop through every line in the VCF file, keeping track of the file number
        if line.startswith("#"): #for header lines only
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: # if we are not on the header line do this
            try: # try doing all of this below
                 # fields is a list that stores the info in one line of the VCF
                fields = line.rstrip().split("\t") # splits each line on a tab character, so that every column is an item in the list ("fields")
                fields[1] = int(fields[1]) # convert the SNP position into an integer (if this doesn't work, we'll automatically go to the "except" block)
                if fields[5] != ".": # if the QUAL column is not empty (i.e., it has a decimal in it that represents the SNP quality)
                    fields[5] = float(fields[5]) # then forcibly convert it into a decimal 
                info = {} # creating a dictionary to store the information in the INFO column - lines 77-84 are going to be about parsing the INFO column
                # we want the dictionary to look like this: {"AC" : 91, "AN" : 5096, ...,""NS" : 2548}
                for entry in fields[7].split(";"): # the list looks like: ["AC=91","AN=5096",...,"NS=2548"]
                    #The first entry we're working with is "AC=91".
                    temp = entry.split("=") # temp is a list. If we're working with "AC=91", temp = ["AC", "91"]
                    if len(temp) == 1: # if there's only one item in the temp list ("AC="), what we want to do is update the dictionary so we know that AC has no value for this SNP.
                        info[temp[0]] = None # we are adding AC to the dictionary.
                        # dictionaries are keys and values. You can add info to a dictionary by doing dict_name[new_key] = new_value. Ex. info["AC"] = "91"
                    else: # otherwise the INFO field is not empty and we're good
                        name, value = temp # temp = ["AC", "91"]. Name = "AC", Value = "91". Step's version: Name = temp[0]. Value = temp[1] 
                        # In these next two lines, we're converting the data in each entry to its correct data type. This data was specified in the header section that we parsed above.
                        Type = info_type[name] # here we're getting the name of the data type that the entry should be. 
                                     #Ex: Type = info_type["AC"]. info_type is a dictionary we made in the header parsing section that tells us what data type that entry should be
                        info[name] = type_map[Type](value) # here we're getting the python function for converting the entry to the correct data  type. Ex: For AC: info["AC"] = type_map["integer"]("91")
                fields[7] = info #replace the 8th item of the "fields" list (i.e. list of columns in this line)
                                 #with the the "info" dictionary that we just made
                                 #we turned the AC=1;AN=5096;,,,;NS=2548 list into a dictionary that looks like this: {"AC" : 91, "AN" : 5096, ...,""NS" : 2548}
                if len(fields) > 8: # if we still have more columns after the INFO column, then we still have more stuff to do:
                                    # example of fields[8] (the FORMAT column): "GT:DP:AF:BG:RU" -> ["GT","DP","AF","BG","RU"] 
                    fields[8] = fields[8].split(":") # We are splitting FORMAT column by colons
                    if len(fields[8]) > 1: #If there are multiple things in the FORMAT column, we have to deal with them individually:
                                           #FORMAT: GT:DP. HG00097: 0|0:0.3
                        for i in range(9, len(fields)): # this goes through all the genotype columns after the FORMAT column -> for us, this is range(9,2513)
                            fields[i] = fields[i].split(':') # split each genotype column along a ":"
                                                             # 0|0:0.3 -> ["0|0", "0.3"]
                                                             # our "fields" list turns into: ["0|0:0.3", "1|1:0.5"] -> 
                                                             #                               [["0|0","0.3"]],[["1|1", . "0.5"]]
                                                             # Ex: i = 9 and \the value in the column is "0|0:0.3"
                                                             # fields[9] = fields[9].split(":") 
                                                             # fields[9] = "0|0:0.3".split(":")
                                                             # fields[9] = ["0|0","0.3"]
                                                             # our "fields" list turns into: ["0|0:0.3", "1|1:0.5"] ->
                                                             #                               [["0|0","0.3"], ["1|1", . "0.5"]]
                     else: # if the genotypes don't have more than one value in them, then we're good
                        fields[8] = fields[8][0] # fields[8] is ["GT"]
                                                 # this code gets you fields[8] = "GT"
                                                 # we set the value of fields[8] to be "GT" (or, the first item in our fields[8] list)
                vcf.append(fields) # We've finished reformatting/cleaning all of the columns; now we add this line to our VCF list. The list is storing all the information from the VCF
                                   # file "fields" is a list that contains the information for the current line that we're working on
            except: # if anything in the try block fails, then:
                malformed += 1 # incremenet the "malformed" variable by 1
    # these next three lines are modifying the first line of the vcf list to match information from the header
    vcf[0][7] = info_description 
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    # if there were any malformed lines, we're going to print out the number of lines so the user knows
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    # at the very end of runing the function, return the vcf list. Give me the data back.
    return vcf
# ignore all of this below
if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
