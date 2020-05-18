import random

ip = random.randrange(1,100)
n = int(input("Enter number of attempts: "))
for j in range(n):
    x = int(input("Guess a number between 1 and 100: "))
    if x == ip :
        print("Correct!!")
    if x < ip :
        print("Number is greater than", x)
    if x > ip :
        print("Number is less than", x)
if j == n-1 :
    print("The correct number is", ip)
