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

