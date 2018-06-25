# Please reference the included PDF for complete instructions.
#
# You can create your table (from the instructions) using a doc or spreadsheet.
#
# Advanced students should attempt to implement
# Rock, Paper, Scissors, Lizard, Spock using 3 or 4 players instead (This is much harder.)
# 1. Ask player 1 for their move.

# 2. Check if player 1's move is valid.

# 3. Ask player 2 for their move.

# 4. Check if player 1's move is valid.

# 5. Print out the winner or 'tie'


import random

##while(1==1):
      #  p1=input("p1, pick rock papers or scissors")
      #  p2=input("p2, pick rock papers or scissors")

       # if p1=="rock"or"paper"or"scissors" and p2=="rock"or"paper"or"scissors":
       #     if p1==p2:
       #         print("tie")
       #     elif p2=="paper" and p1=="rock":
        #        print("p2 wins")
       #     elif p2=="scissors" and p1=="paper":
      #          print("p2 wins")
       #     elif p2=="rock" and p1=="scissors":
       #         print("p2 wins")
       #     else:
        #        print("p1 wins")
     #   else :
  ##          print("I couldn't understand you")

p1=input("p1, pick rock, paper, or scissors")
p2=input("p2, pick rock, paper, or scissors")
if p1==p2:
    print("tie")
elif p1=="rock":
    if p2=="paper":
        print("p2")
    else :
        print("p1")
