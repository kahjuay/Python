fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index + 1

count = 0
for letter in fruit:
    if letter == "a":
        count = count + 1
print("There are " + str(count) + " a in " + fruit)

print('n' in fruit) #True
print('m' in fruit) #False
print('nan' in fruit) #True

pos = fruit.find("na")
print(pos) #2

aa = fruit.find("z")
print(aa) #-1

mytext = input("Type something: ")
index = 0

while index < len(mytext):
    letter = mytext[index]
    print(index, letter)
    index = index +1

s = "Monty Python"
# Square brackets up to but not including
print(s[0:4]) #Mont
print(s[6:7]) #P
print(s[6:20]) #Python

print(s[:2]) #Mo
print(s[8:]) #thon
print(s[:]) #Monty Python
print(s) #Monty Python

greet = "Hello Bob!"
nnn = greet.upper()
print(nnn)

www = greet.lower()
print(www)

print(greet)

nstr = greet.replace("Bob", "Jane")
print(nstr)

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find (" ", atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)