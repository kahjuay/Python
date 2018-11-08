# Use the file name mbox-short.txt as the file name
#import sys

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ("Cannot open " + fname)
    quit()

numtotal = 0
numtotal = float(numtotal)
linecount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue

    line = line.rstrip()
    colpos = line.find(":")
    numfound = line[colpos+1:]
    numfound = float(numfound)
    numtotal = numtotal + numfound
    linecount = linecount + 1
    #print(line)
    #print(numtotal/linecount)
#print("Done")
print ("Average spam confidence: " + str(numtotal/linecount))