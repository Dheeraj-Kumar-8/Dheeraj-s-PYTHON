A = int(input("Enter 1st Number: "))
B = int(input("Enter 2nd Number: "))

a = A
b = B

while A!=B: 
    if A>B:
        A = A-B
    else:
        B = B-A

print("GCD of given number:",a,"and",b," is: ",A)
