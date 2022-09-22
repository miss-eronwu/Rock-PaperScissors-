#Make computer go against user
#make random generator for computer
import random

#for random number generator only two numbers can be placed
#computer will pick a number 1-3
computer = random.randint(1,3)



user = int(input("Welcome to Rock, Paper, Scissors game, 1 is for Rock, 2 is for Paper, 3 is for Scissors\n "
      "Please enter a number:  "))

#if rock vs rock then its a tie

if computer == 1 and user == 1:
 print("Both players picked rock, it's a tie")
elif computer == 1 and user == 2:
     print("Paper beats rock the user wins")
elif computer == 1 and user == 3:
    print("Rock beats Scissors, the computer wins")
elif computer == 2 and user == 1:
    print("Paper beats rock the computer wins")
elif computer == 2 and user == 2:
    print("Both players picked paper, the game is a tie")
elif computer == 2 and user == 3:
    print("Scissors beats paper the user wins")
elif computer == 3 and user == 1:
    print("Rock beats scissors, the user wins")
elif computer == 3 and user == 2:
    print("Scissors beats paper, the computer wins")
elif computer == 3 and user ==  3:
    print("Both players picked scissors, its a tie")
else:
    print("That is not a valid entry, try again")

#if rock vs paper then paper wins

#if rock vs scissors then rock wins