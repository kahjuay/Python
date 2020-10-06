import re

fname = input("Enter filename for regex:")

if len(fname)<1:
    fname = "D:\OneDrive\Documents\Python\py4e\\regex_sum_997664.txt"
    #print(fname)

try:
    fhand = open(fname)
except:
    print(fname, "is an invalid file, please try again!")
    quit()

numlist = list()

for line in fhand:
    line = line.rstrip()
    tmplist = re.findall('[0-9]+' ,line)
    #print(tmplist)
    if len(tmplist)>0:
        #print
        for i in tmplist:
            numlist.append(int(i))



print(numlist)
print(sum(numlist))
#print("Program end")
quit()