import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
while True:
    print("\n--- Rock, Paper, Scissors ---")
    print(f"Score - player: {player_score} | computer: {computer_score}")
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to stop: ").lower()

    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
        