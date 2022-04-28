'''
Name:; Logan Freerksen
Date: 04/28/22

'''
import random

def choose_word(words):
    game_word = random.choice(words)
    return game_word

def game(game_word):
    attempts = 0
    while (attempts <=6):
        guess = input("Guess a letter of the alpabet that you think is in the mystery word: ")
        if guess in game_word:
            print()


def main():
    words = []
    with open("Lectures/Assignments/Final/words.txt") as fin:
        data = fin.readlines()
        for line in data:
            words.append(line.strip())
    
        

if __name__ == "__main__":
    main()