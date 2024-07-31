import random

def validate_input(user_guess):
    if not user_guess.isdigit():
        print('Invalid input! Please enter a number between 1 and 100.')
        return False
    user_guess = int(user_guess)
    if user_guess < 1 or user_guess > 100:
        print('Out of range! Please enter a valid number between 1 and 100.')
        return False
    return True

def main():
    rand_num = random.randint(1,100)
    score = 100
    attempts = 0

    while True:
        user_guess = input(f'Enter a number between 1 and 100 (or q to quit). Number of attempts so far: {attempts} ')


        if user_guess.lower() == 'q':
            print('You quitted the game. Goodbye!')
            break

        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if rand_num > user_guess:
            print('Your guess is lower than the answer. Please try agian!')
            attempts += 1
            score -= 10
            score = max(score, 0)
            if score == 0:
                print(f'You lost the game!😭😭 The answer was {rand_num}')
                wanna_play_again = input('Do you want to play again? (Answer with Y/N) ')
                if wanna_play_again.lower() == 'n':
                    print('GOODBYE!')
                    break
                elif wanna_play_again.lower() == 'y':
                    score = 100
                    rand_num = random.randint(1,100)
                    continue
        elif rand_num < user_guess:
            print('Your guess is higher than the answer. Please try again! ')
            attempts += 1
            score -=10
            score = max(score, 0)
            if score == 0:
                print(f'You lost the game!😭😭 The answer was {rand_num}')
                wanna_play_again = input('Do you want to play again? (Answer with Y/N) ')
                if wanna_play_again.lower() == 'n':
                    print('GOODBYE!')
                    break
                elif wanna_play_again.lower() == 'y':
                    score = 100
                    rand_num = random.randint(1,100)
                    continue

        elif rand_num == user_guess:
            print('😃😃 CONGRATULATION you guessed the correct number. 😃😃')
            print('Your score is:', score)
            wanna_play_again = input('Do you want to play again? (Answer with Y/N) ')
            if wanna_play_again.lower() == 'n':
                print('GOODBYE!')
                break
            elif wanna_play_again.lower() == 'y':
                score = 100
                rand_num = random.randint(1,100)
                continue

if __name__ == "__main__":
    main()