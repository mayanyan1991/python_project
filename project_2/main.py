# while loop, if statement
import random
def guess(x):
    a = random.randint(1,x)
    b = int(input("guess a number between 1 and "+ str(x) +": "))
    min_limi = 1
    max_limi = x
    while a > 1:
        if b > a and b <= max_limi:
            max_limi = b
            b = int(input("guess a new number between " + str(min_limi) + "  and " + str(max_limi) +": "))    
        elif b < a and b >= min_limi:
            min_limi = b
            b = int(input("guess a new number between "+ str(min_limi) + " and " + str(max_limi) + ": "))
        elif b == a:
            print("correct")
            break
        else:
            b = int(input("please type in correct number: "))
            
 
guess(10)

