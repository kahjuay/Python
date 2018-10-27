score = input("Enter Score between 0 and 1: ")
try:
    floatscr = float(score)
except:
    floatscr = -0.1

if floatscr >= 0.9 :
    print("A")
elif floatscr >= 0.8 :
    print("B")
elif floatscr >= 0.7 :
    print("C")
elif floatscr >= 0.6 :
    print("D")
elif floatscr > 0 :
    print("F")
else :
    print ("This is not a valid grade")

