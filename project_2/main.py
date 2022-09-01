import random
def guess(x):
    a = random.randint(1,x)
    b = int(input("guess a number between 1 and "+ str(x) +": "))
    min_limi = 1
    max_limi = x
    while a > 1:
        if b > a:
            b = int(input("guess a new number between 1 and and " + str(b) +": "))
        elif b < a and b > 1:
            b = int(input("guess a new number between "+ str(b) + " and " + str(x) + ": "))
        elif b == a:
            print("correct")
            break
        else:
            b = int(input("please type in correct number: "))
            
 
guess(10)

