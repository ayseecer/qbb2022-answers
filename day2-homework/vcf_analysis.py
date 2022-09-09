import sys

from vcfParser import parse_vcf

randomsnippet = parse_vcf("/Users/cmdb/data/vcf_files/random_snippet.vcf")
snpsnippet = parse_vcf("/Users/cmdb/cmdb-quantbio/assignments/bootcamp/annotating_and_writing_variants/extra_data/dbSNP_snippet.vcf")
SNP_dict = {}

for i, line in enumerate(snpsnippet):
    position = i[1]
    newkey = 
    
    
    

