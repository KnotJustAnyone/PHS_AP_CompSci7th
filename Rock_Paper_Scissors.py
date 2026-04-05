import random

user_round_score = 0
computer_round_score = 0
user_game_score = 0
computer_game_score = 0

while True:
  x = int(input("Would you like to play a best of 3 or a best of 5? Please enter 3 or 5 accordingly: "))
  while True:
    if x == 3 or x == 5:
      break
    else: 
      x = int(input("Invalid answer. Please enter 3 or 5: "))
  
  for i in range(x):
  
    options = ["rock", "paper", "scissors"]
  
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
      user_choice = input("Invalid answer. Enter rock, paper, or scissors: ").lower()

    computer_choice = random.choice(options)
  
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
  
    if user_choice == computer_choice:
        print("\nIt's a tie!")
        print("You've won", user_round_score, "rounds this game.")
        print("The computers won", computer_round_score, "rounds this game.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        user_round_score = user_round_score + 1
        print("\nYou win!")
        print("You've won", user_round_score, "rounds this game!")
        print("The computers won", computer_round_score, "rounds this game!")
  
    else:
        computer_round_score = computer_round_score + 1
        print("\nYou lose!")
        print("You've won", user_round_score, "rounds this game.")
        print("The computers won", computer_round_score, "rounds this game.")
  
  if x == 3 and user_round_score > computer_round_score:
    print("\nCongratulations! You won the best of 3.")
    user_game_score = user_game_score + 1 
    print("You've won", user_game_score, "games!")
    print("The computers won", computer_game_score, "games!")
  elif x == 3 and user_round_score < computer_round_score:
    print("\nYou lost the best of 3 :(")
    computer_game_score = computer_game_score + 1
    print("You've won", user_game_score, "games.")
    print("The computers won", computer_game_score, "games.")
  elif x == 5 and user_round_score > computer_round_score:
    print("\nCongratulations! You won the best of 5.")
    user_game_score = user_game_score + 1
    print("You've won", user_game_score, "games!")
    print("The computers won", computer_game_score, "games!")
  elif x == 5 and user_round_score < computer_round_score:
    print("\nYou lost the best of 5 :(")
    computer_game_score = computer_game_score + 1
    print("You've won", user_game_score, "games.")
    print("The computers won", computer_game_score, "games.")
  elif x == 3 and user_round_score == computer_round_score:
    print("\nYou tied the best of 3.")
    print("You've won", user_game_score, "games.")
    print("The computers won", computer_game_score, "games.")
  elif x == 5 and user_round_score == computer_round_score:
    print("\nYou tied the best of 5 :(")
    print("You've won", user_game_score, "games.")
    print("The computers won", computer_game_score, "games.")

  play_again = input("Would you like to play again? Enter yes or no: ").lower()
  
  while play_again != "yes" and play_again != "no":
    play_again = input("Invalid answer. Enter yes or no: ").lower()

  if play_again == "yes":
    user_round_score = 0
    computer_round_score = 0

  if play_again == "no":
    break


print("\nBye Bye!")
