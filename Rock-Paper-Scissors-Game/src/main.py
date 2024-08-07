"""
Author: fsepehrpour
Date Created: 07/08/2024
Description: Rock Paper Scissors Game
"""


import random


class RockPaperScissors:
    """Main class for Rock Paper Scissors game. """
    def __init__(self, name:str):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_user_choice(self):
        """Method to get user choice."""
        user_choice = input(f'Select one of these  three choises: {self.choices} ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()

        print(f'Your choice("{user_choice}") is not valid. Please try again with one of these choices: {self.choices} !')
        return self.get_user_choice()

    def get_computer_choice(self):
        """Get computer choice randomly from choices: rock, paper, scissors."""
        return random.choice(self.choices)

    def select_winner(self, user_choice:str, computer_choice: str) -> str :
        """Decide the winner of the game between user and computer based on  rules of the game.


        :param user_choice = The choice of the user.
        :param computer_choice = The choice of the computer.
        :return: The result of the game.
        """
        if user_choice == computer_choice:
            return "It's a tie. Play again!"

        winner_combinations = [('rock', 'scissors'), ('paper', 'rock'),('scissors', 'paper')]
        for win_com in winner_combinations:
            if (user_choice == win_com[0]) & (computer_choice == win_com[1]):
                return "Congratulations!!! You won."

        return "Oh no! You lost the game to computer.😢"

    def play(self):
        """Play the game.
        - Get user choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f'computer choice: {computer_choice} vs your choice: {user_choice}')
        print(self.select_winner(user_choice, computer_choice))

if __name__ == "__main__":
    game = RockPaperScissors('Fatemeh')

    while True:
        game.play()

        continue_game = input('Do you want to continue the game? If yes, press any key. If no, enter "q". ')
        if continue_game.lower() == 'q':
            print('Goodbye!')
            break
