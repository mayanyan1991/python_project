# while loop, if statement
import random
def guess(x):
    a = random.randint(1,x)
    b = int(input("guess a number between 1 and "+ str(x) +": "))
    # alternative for input (f"guess....{x}")
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

def guess_2(x):
    a = random.randint(1,x)
    b = 0
    # alternative for input (f"guess....{x}")
    min_limi = 1
    max_limi = x
    while a != b:
        b = int(input("guess a number between " + str(min_limi) + "  and " + str(max_limi) +": ")) 
        if b > a and b <= max_limi:
            max_limi = b 
        elif b < a and b >= min_limi:
            min_limi = b
        elif b < min_limi or b > max_limi:
            b = int(input("please type in correct number: "))           
    print("correct")

guess_2(10)

