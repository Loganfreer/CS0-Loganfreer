'''
Name: Logan Freerksen
Date: 03/31/22

This program will greet a player using their name, and ask the user to guess a random
number between 1 and 20. The player will recive 6 tries to guess the number, while after
each guess telling the player whether they are too high or too low

Step 1: Define a function that asks the user for their name
Step 2: Define a function that greets the user
Step 3: Print out directions of the game
Step 4: Define a function that picks a random number between 1 and 20
    Step 4a: Import random library
Step 5: Define function using a loop that asks the player what they think the number is
    Step 5a: If number is to high, print out that the guess is too high
    Step 5b: If number is to low, print out that guess is too low
    Step 5c: Increase attempt counter after each attempt
    Step 5d: After 6 tries tell the user they lose/win


'''
import random

def ask_name():
    name = input("Hello there! What's your name? ")
    return name

def greet_user(user_name):
    print(f'Welcome the the guess the number game {user_name}!')
    print(f'In this game you will be trying to guess a number between 1 and 20.\nYou will get six tries, if you dont guess the number after six tries you loose\nGood luck!')

def choose_number():
    num = random.randrange(1,21)
    return num

user = ask_name()
greet_user(user)      
def main():
    game_num = choose_number()
    attempt = 1

    while(attempt <= 6):
        guess = int(input('Please enter an integer between 1 and 20: '))
        if attempt == 6:
            print(f'Sorry, looks like you ran out of tries, the game number was {game_num}')
            print('Better luck next time')
            break
        elif guess == game_num:
            print(f'Congradulations! you guessed the number {user}')
            print(f'The game number was {game_num}')
            print(f'It took you {attempt} tries to get it')
            break
        elif guess > game_num:
            print('Oops, looks like your guess was to high')
            attempt += 1
            continue
        elif guess < game_num:
            print('Oops, looks like your guess was too low')
            attempt += 1
            continue

        
main()

play_again = True
while (play_again):
    answer = input('Would you like to play again [y/n]? ')
    if answer == 'y':
        main()
    elif answer == 'yes':
        main()
    else:
        print('Goodbye!')
        play_again = False

    