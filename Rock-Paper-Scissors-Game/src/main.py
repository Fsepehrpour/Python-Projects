import random


class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_user_choice(self):
        user_choice = input(f'Select one of these  three choises: {self.choices} ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()

        print(f'Your choice("{user_choice}") is not valid. Please try again with one of these choices: {self.choices} !')
        return self.get_user_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def select_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie. Play again!"

        winner_combinations = [('rock', 'scissors'), ('paper', 'rock'),('scissors', 'paper')]
        for win_com in winner_combinations:
            if (user_choice == win_com[0]) & (computer_choice == win_com[1]):
                return "Congratulations!!! You won."

        return "Oh no! You lost the game to computer.😢"

    def play(self):
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
