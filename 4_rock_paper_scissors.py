import random

# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game = [rock,paper,scissors]
choice = int(input("\nWhat is your choice? \n(0 - Rock | 1 - Paper | 2 - Scissor) \n--> "))
human = choice
index = len(game)-1
computer = random.randint(0,index)
if human <= index:
    print("You Had -->\n",game[human])
    print("Computer Had -->\n",game[computer])
    if human==computer:
        print("Go Again!")
    elif (human==0 and computer==1) or (human==1 and computer==2) or (human==2 and computer==0):
        print("\n\t!! Computer Won !!\n")
    else:
        print("\n\t!! You Won !!\n")
else:
    print("Wrong Choice!")
