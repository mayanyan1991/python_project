#rock, paper, scissor
import random

def game():
    gamer = input ("'s' for 'scissor', 'r' for 'rock', 'p' for 'paper': ")
    computer = random.choice(['s','p','r'])
    if gamer == computer:
        print("even")
    elif is_win(gamer, computer):
        #call function
        print("you win!")
    else:
        print("you loose...")

def is_win(gamer, computer):
    #s>p,r>s,p>r
    if (gamer == "s" and computer == "p") or (gamer == "r" and computer == "s")\
         or (gamer == "p" and computer == "r"):
         return True

game()