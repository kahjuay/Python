def computepay(hrs,rate):
    #return 42.37
    return hrs*rate + hrsmore*rate*1.5

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

hrsmore = 0

if hrs > 40:
    hrsmore = hrs - 40
    hrs = 40



p = computepay(hrs, rate)
#print("Pay",p)
print(p)