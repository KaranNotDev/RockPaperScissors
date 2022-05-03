import random


rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

lst=[rock, paper, scissors]

print("WELCOME TO MY ROCK PAPER SCISSORS GAME \n MADE BY THE WORST PROGRAMMER @KARANNOTDEV\n")

UserChoice=str(input("(R) for Rock, (P) for Paper, (S) for Scissors\n"))

if (UserChoice=="R" or UserChoice=="r"):
    UserChoice=rock
    print("Ya choose: \n", UserChoice)
    
elif (UserChoice=="P" or UserChoice=="p"):
    UserChoice=paper
    print("Ya choose: \n", UserChoice)
        
elif (UserChoice=="S" or UserChoice=="s"):
    UserChoice=scissors
    print("Ya choose: \n", UserChoice)
    
else:
    print("I SAID PRESS R, P OR S I DIDNT TELL YA TO PRESS ANYTHIN' ELSE")
        
RoboChoice=random.choice(lst)
print("Robo choose: \n", RoboChoice)
    
print("And da winner is:")
    
if (RoboChoice==UserChoice):
    print("No winner. That is a tie")
        
elif (RoboChoice==rock and UserChoice==scissors):
    print("Hah, take that! My program is better then you!")
    
elif (RoboChoice==paper and UserChoice==rock):
    print("Hah, take that! My program is better then you!")
        
elif (RoboChoice==scissors and UserChoice==paper):
    print("Hah, take that! My program is better then you!")
        
elif (UserChoice==rock and RoboChoice==scissors):
    print("Ah, okey you might be better then my program")
        
elif (UserChoice==paper and RoboChoice==rock):
    print("Ah, okey you might be better then my program")
    
elif (UserChoice==scissors and RoboChoice==paper):
    print("Ah, okey you might be better then my program")
