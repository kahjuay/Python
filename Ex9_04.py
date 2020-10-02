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


# New attempt
name = input("Enter file:")
if len(name) < 1 : name = "D:\OneDrive\Documents\Python\py4e\mbox-short.txt"
try:
    handle = open(name)
except:
    print(name,"is an invalid file, please try again!")
    quit()

count = dict()
bigname = ""
bigcount = 0

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        email = line[1]
        #print(email)
        count[email] = count.get(email,0)+1
        if count[email] > bigcount:
            bigcount = count[email]
            bigname = email

print(bigname,bigcount)