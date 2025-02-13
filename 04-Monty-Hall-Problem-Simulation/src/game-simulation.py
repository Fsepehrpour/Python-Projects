import random


def monty_hall_game(switch_doors: bool) -> bool:
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))

    doors_to_reveal = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
    revealed_door = random.choice(doors_to_reveal)

    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != revealed_door][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'


def monty_hall_game_simulation(number_of_games: int = 100):
    num_wins_without_switching = sum(monty_hall_game(switch_doors=False) for _ in range(number_of_games))
    num_wins_with_switching = sum(monty_hall_game(switch_doors=True) for _ in range(number_of_games))

    return num_wins_without_switching, num_wins_with_switching


if __name__ == "__main__":
    num_games = 1000
    num_wins_without_switching, num_wins_with_switching =  monty_hall_game_simulation(num_games)
    print(f"Winning percentage without switching doors: {num_wins_without_switching/num_games*100}%")
    print(f"Winning percentage with switching doors: {num_wins_with_switching/num_games*100}%")
  
