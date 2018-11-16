fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    line = line.rstrip()
    sentence = line.split()

    if len(sentence) > 2 and sentence[0] == "From":
        #print(sentence)
        lst.append(sentence[1])
        count = count + 1

for email in lst:
    print(email)

print("There were", count, "lines in the file with From as the first word")
