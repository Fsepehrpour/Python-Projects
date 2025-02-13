import random

def get_user_choice():
    """Get user choice and validate the input until the user enter a valid iput
    
    :return: user_choice
    :rtype: str
    """
    print("\nEnter one of choices below or 'q' to quit:\nRock\nPaper\nScissors")
    print()
    choices = ['rock', 'paper', 'scissors', 'q']
    while True:
        user_choice = input()
        user_choice = user_choice.lower()
        if user_choice in choices:
            return user_choice
        else:
            print('You entered invalid input! Try again')

def get_computer_choice():
    """Select a choice randomly for computer.

    :return: computer_choice
    :rtype: str
    """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner between the user and computer based on the winner conditions.

    :param user_choice: entered by the user
    :type user_choice: str
    :param computer_choice: randomly chosen by th ecomputer
    :type computer_choice: str
    """
    winner_conditions = {('rock', 'scissors'),('paper', 'rock'),('scissors', 'paper')}
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice, computer_choice) in winner_conditions:
        print(f"Congratulations! You won! ")
    else:
        print(f"Sorry you lost!")

def play():
    """Plays the game continuously until the user quits.
    """
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        if user_choice == 'q':
            print('You quit the game! Goodbye.')
            break
        print("User choice: ", user_choice)
        print("Computer choice: ", computer_choice)
        determine_winner(user_choice, computer_choice)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print('Goodbye!')
            break


if __name__ == "__main__":
    play()

