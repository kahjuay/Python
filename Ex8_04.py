fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line.rstrip())
    line = line.rstrip()
    sentence = line.split()

    for word in sentence:
        if word not in lst:
            lst.append(word)
            #print(lst)

lst.sort()
print(lst)

    
