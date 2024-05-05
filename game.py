import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    while True:
        user_score = 0
        computer_score = 0

        while True:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"\nYour choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "Computer wins!":
                computer_score += 1

            print(f"Score - You: {user_score}, Computer: {computer_score}\n")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break  # Exit the inner loop if user doesn't want to play again

        # Check if user wants to play another round
        play_again_outer = input("Do you want to play another round? (yes/no): ").lower()
        if play_again_outer != 'yes':
            print("Thanks for playing!")
            break  # Exit the outer loop if user doesn't want to play another round

if __name__ == "__main__":
    main()
