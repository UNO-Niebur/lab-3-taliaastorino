#RPS.py
#Name: Talia Astorino
#Date: 02/08/2026
#Purpose: Using boolean logic, conditional statements, loops, and program flow control.
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  while play_again.lower() == "y":
    #User can play as many games as they wish.
    
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "S"])
    #Prompt the user for their RPS selection
    user = input("Enter R, P, or S. ").upper()
    #Determine winner and state what happened to the user
    if user == computer:
      print("Tie! Both chose", user)
      ties += 1
    elif(user == "R" and computer == "S") or \
        (user == "P" and computer == "R") or \
        (user == "S" and computer == "P"):
      print("You win! :) Computer chose", computer)
      wins += 1
    else:
       print("You lose! :( Computer chose", computer)
       losses += 1
    #Ask the user if they would like to play again.
    play_again = input("Do you want to play again? (y/n): ")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
