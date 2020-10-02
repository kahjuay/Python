name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()

for line in handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print (words)

    
    if len(words) > 1 and words[0] == "From":
        # print (words)
        time = words[5]
        # print(time)

        hour = time.split(":")[0]
        # print(hour)

        di[hour] = di.get(hour,0)+1
            
# print(di)

# print( sorted([(k,v) for k,v in di.items()]) )
lst =  sorted([(k,v) for k,v in di.items()]) 

for k,v in lst:
    print(k,v)

# Less fancy second attempt
name = input("Enter file:")
if len(name) < 1 : name = "D:\OneDrive\Documents\Python\py4e\mbox-short.txt"
try:
    handle = open(name)
except:
    print(name,"is an invalid file, please try again!")
    quit()

timedict = dict()

for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        #print(line)
        words = line.split()
        #print(words)
        #print(words[5])
        time = words[5].split(":")
        hrs = time[0]
        #print(hrs)
        timedict[hrs]= timedict.get(hrs,0)+1

#print(timedict)
timelist = list()
for k,v in timedict.items():
    timelist.append((k,v))

timelist.sort()
#print(timelist)
for k,v in timelist:
    print(k,v)
