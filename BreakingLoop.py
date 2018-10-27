print("Type anything to echo, done to break")

while True:
    line = input ("> ")
    if line[0] == '#' :
        continue
    if line == "done" :
        break
    print (line)

print ("Done!")