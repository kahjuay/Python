# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print(fname, "is an invalid file, please try again")
    quit()

intinstance = 0
flttotal = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    intinstance += 1
    flttotal += float(line[line.find(":")+1:].rstrip())
print("Average spam confidence:",flttotal/intinstance)