import random

def get_choices():
  options = ["rock","paper","scissors"]
  player_choice = input("Enter a choice (rock, paper, scissors):")
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"Player chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock" and computer =="scissors":
    return "You win!"
  elif player == "paper" and computer == "rock":
    return "You win!"
  elif player == "scissors" and computer == "paper":
    return "You win!"
  else:
    return "You lose!"
        

results = get_choices()
print(check_win(results["player"], results["computer"]))
  