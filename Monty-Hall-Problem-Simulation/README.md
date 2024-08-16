![Monty Hall](images/banner.png)
# Monty Hall Game Simulation
Welcome to the Monty Hall Game Simulation repository! This project provides a Python implementation of the famous Monty Hall problem, allowing you to simulate the game and observe the outcomes of different strategies.

## Introduction
The Monty Hall problem is a probability puzzle based on a game show scenario. In the game, a contestant is presented with three doors: behind one door is a car (the prize), and behind the other two doors are goats. After the contestant makes an initial choice, the host, who knows what is behind each door, reveals a goat behind one of the remaining doors. The contestant then has the option to stick with their initial choice or switch to the other unopened door.
This simulation allows you to explore the probabilities of winning based on whether you choose to switch doors or not.

## Getting Started
To run this simulation, you need to have Python installed on your machine. The script is compatible with Python 3.x.

### Prerequisites
* Python 3.x
* Basic understanding of running Python scripts

## Installation
Clone this repository to your local machine and run the  simulation script:
```
python game_simulation.py
```

## How It Works
The simulation consists of two main functions:
* `monty_hall_game(switch_doors: bool)`: This function simulates a single game of Monty Hall. It takes a boolean parameter `switch_doors` to determine whether the contestant switches their choice after a door is revealed.
* `monty_hall_game_simulation(number_of_games: int)`: This function runs multiple simulations (default is 100 games) and returns the number of wins for both strategies: switching and not switching.

## Usage
To customize the number of games played, modify the `num_games` variable in the __main__ section of the script. For example, to run 1000 games, set:
```
num_games = 1000
```
Then, execute the script to see the results.

## Results
After running the simulation, the script will output the winning percentages for both strategies:
* Winning percentage without switching doors
* Winning percentage with switching doors
You will typically observe that switching doors significantly increases the chances of winning the car.

## License
This project is licensed under the MIT License. Thank you for checking out the Monty Hall Game Simulation! Enjoy exploring the probabilities and strategies involved in this classic problem!
