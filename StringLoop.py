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


mytext = input("Type something: ")
index = 0

while index < len(mytext):
    letter = mytext[index]
    print(index, letter)
    index = index +1

