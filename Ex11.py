import re

filename = input("Enter filename: ")
if len(filename) < 1:
    filename = "regex_sum_146678.txt"

# di = dict()
numlist = list()
filehand = open(filename)

for line in filehand:
    line = line.rstrip()
    # print(line)
    lst = re.findall('[0-9]+',line)
    # if len(lst)<1: 
    #     continue
    print(lst,len(lst))
    
    
