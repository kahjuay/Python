for i in [5,4,3,2,1]:
    print (i)
print ("Blast Off!")


line = input ("How many iterations? ")
for i in range(1,int(line)+1,1):
    print (i)

friends = ["Joseph", "Glenn", "Sally"]

for friend in friends:
    print ("Happy New Year: ", friend)

for i in range(len(friends)):
    friend = friends[i]
    print ("Wonderful New Year: ", friend)

print ("Done!")