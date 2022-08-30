Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = 100-int(sys.argv[2]) #SET the desired number of lines which is the total lines -100- minus the user-specified value
else: #OTHERWISE
  n_lines = 90 #SET the desired number of lines to a default. Default is 10 from the end since 100 minus 90 is 10.
for i, line in enumerate(open(filename)): #FOR every line in the open file
  if i > n_lines: #IF a desired line by its numerical position. changed this to greater than so it would print the values at the end.
    print(line.strip('\r\n')) #PRINT the line

# This script is pretty good. It appears to work for the given input file.
# However, what happens when we run a different file as the input? You need
# to make it more flexible but setting n_lines to the number of lines you
# want to print and then figuring out how to print those lines from the end.
# The simplest solution is to create a list and load the whole file into that
# list line by line. Then you can go through the last n_lines lines of the list.
# You're definitely on the right track and seem to be on good footing.
# Keep it up! - Mike