smallest = None
print ("Before")
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print ("After")



largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        intnum = int(num)
    except:
        print ("Invalid input")
        continue
    
    if smallest is None:
        smallest = intnum
    elif smallest > intnum:
        smallest = intnum
    
    if largest is None:
        largest = intnum
    elif largest < intnum:
        largest = intnum

    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)