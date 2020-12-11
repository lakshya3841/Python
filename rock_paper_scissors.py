# WORKS WITH ONLY PYTHON 3
import random
print("PLEASE PLAY WITH CAPITAL LETTERS\n")
print("OR IT WILL ELSE PRINT YOU WON")

l1 = ["ROCK","PAPER","SCISSORS"]


# Basically I am lazy to add the win factor for User so i added it in else area 


times_play = int(input("ENTER THE NUMBER OF ROUNDS YOU WANNA PLAY "))
for i in range(times_play):
    x = random.choice(l1)
    y = str(input("R P S "))
    if y == "R" and x == "PAPER":
        print("YOU LOST\n")
        print("COMPUTER PLAYER CHOOSED ",x)
    elif y == "P" and x == "SCISSORS":
        print("YOU LOST")
        print("COMPUTER CHOOSED SCISSOR ")
    elif y == "S" and x == "ROCK":
        print("YOU LOST")
        print("COMPUTER CHOOSED ROCK")
    elif y == "S" and x == "SCISSORS":
        print("IT'S A TIE")
        print("COMPUTER SELECTED ",x)
    elif y == "R" and x == "ROCK":
        print("IT'S A TIE")
        print("COMPUTER SELECTED ",x)
    elif y == "P" and x == "PAPER":
        print("IT'S A TIE")
        print("COMPUTER SELECTED ",x)
    else:
        print("YOU WON")
        print("COMPUTER SELECTED ",x)
        
