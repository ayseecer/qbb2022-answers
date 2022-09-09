import bed_parser
bed_file = bed_parser.parse_bed("hg38_gencodev41_chr21.bed") #myfilename.(functionname) 
#print(bed_file[0])

number_of_exons = [] #creates an empty list 

for i in bed_file:
    number_of_exons.append(i[9]) #appends the empty list by adding the nineth (indexed) column integers and storing it as a list.

number_of_exons.sort() #sorts the number_of_exons list of exon numbers in ascending order.

print(number_of_exons[len(number_of_exons)//2])


 