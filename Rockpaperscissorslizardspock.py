import random
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
player_score = 0
computer_score = 0

# Win conditions based on your rules
win_conditions = {
    'scissors': ['paper', 'lizard'],
    'paper': ['rock', 'spock'],
    'rock': ['lizard', 'scissors'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

while True:
    print("\n--- Rock, Paper, Scissors, Lizard, Spock ---")
    print(f"Score - player: {player_score} | computer: {computer_score}")
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock) or 'quit' to stop: ").lower()

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
    elif computer_choice in win_conditions[user_choice]:
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1