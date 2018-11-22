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
    # print (type(lst))
    if len(lst)>0: 
        # print(lst,len(lst))
        for i in lst:
            numlist.append(int(i))

print(numlist)
print(len(numlist))    
print(sum(numlist))
    
    
