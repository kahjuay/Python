name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for line in handle:
    line = line.rstrip()   
    #print(line)
    wds = line.split()
    #print(wds)

    if len(wds) > 1 and wds[0] == "From":
        # print(wds[1])
        di[wds[1]] = di.get(wds[1],0) + 1

bigcount = None
bigemail = None

for email,count in di.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email

# print(di)
print (bigemail,bigcount)
