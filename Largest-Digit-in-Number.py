# Write a Python program to find the largest digit in a given number using a loop. #

num = int(input("Enter Any number: "))
Number = num
big = 0

while num>0:
    R = num%10
    if(R>big):
        big = R
    num //= 10

print("Largest digit in ",Number," is: ",big)