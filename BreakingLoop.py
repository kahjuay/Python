print("Type anything to echo, done to break")

while True:
    line = input ("> ")
    if line == "done" :
        break
    print (line)

print ("Done!")