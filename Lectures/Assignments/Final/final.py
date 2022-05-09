'''
Name:; Logan Freerksen
Date: 04/28/22

'''
import random

def user_name():
    user = input('Welcome to the Hangman game! What is your name? ')
    return user

def greet_user(user):
    print(f"Nice to meet you {user}, your goal is to guess the mystery word in less than 6 tries")

def choose_word(words):
    game_word = random.choice(words)
    return str(game_word)

def guess_check(word_list, guess, display_word):
    for i in range(len(word_list)):
        if word_list[i] == guess:
            display_word[i] = guess
            return True
        else:
            return False
    



def game(game_word):
    stages = ['''    |__________________ 						
    |/        	| 
    | 	        
    |
    | 
    |
    |
    |	
    |
    | 
    |				              
    -------------''', '''
    |__________________ 						
    |/        ___|___
    | 	     | X  X |
    |        | ____ |
    | 	     |______|
    |
    |
    |
    |
    | 	
    |			              
    -------------
    ''', '''
    |__________________ 						
    |/        ___|___
    | 	     | X  X |
    |        | ____ |
    | 	     |______|
    |           |
    |           |
    |           |
    |           |
    | 	
    |			              
    -------------
    ''', '''
    |__________________ 						
    |/        ___|___
    | 	     | X  X |
    |        | ____ |
    | 	     |______|
    |          /|
    |         / | 
    |        /  |  
    |           |
    | 	
    |			              
    -------------
    ''', '''
    |__________________ 						
    |/        ___|___
    | 	     | X  X |
    |        | ____ |
    | 	     |______|
    |          /|\\
    |         / | \\
    |        /  |  \\
    |           |
    | 	
    |			              
    -------------
    ''', '''
    |__________________ 						
    |/        ___|___
    | 	     | X  X |
    |        | ____ |
    | 	     |______|
    |          /|\\
    |         / | \\
    |        /  |  \\
    |           |
    | 	       / 
    |         /                
    -------------
    ''', '''
    |__________________ 						
    |/        ___|___
    | 	     | X  X |
    |        | ____ |
    | 	     |______|
    |          /|\\
    |         / | \\
    |        /  |  \\
    |           |
    | 	       / \\
    |         /   \\             
    -------------
    ''']
    attempts = 0
    word_list = list(game_word)
    blank_word = []
    print(f"{word_list}")
    
    print(f"{stages[0]}")

    for k in range(len(word_list)):
        blank_word = "_ "*(k+1)
    while (attempts <= 6):
        guess = input("Guess a letter of the alpabet that you think is in the mystery word: ")
        guess = guess.lower
        if guess_check(word_list, guess, blank_word):
            print("Great guess!")
            print(f"{stages[attempts]}")
            print(f"{blank_word}")
        else:
            print("That wasn't in there, sorry, try again")
            attempts += 1
            print({stages[attempts]})
            print(f"{blank_word}")



        if attempts == 6:
            play_again = True
            while (play_again):
                response = input("It looks like you ran out of tries, would you like to give it another shot? [y/n] ")
                if not response.lower()  == 'y' or not response.lower() == 'yes':
                    play_again = False

               
        


def main():
    words = []
    with open("Lectures/Assignments/Final/words.txt") as fin:
        data = fin.readlines()
        for line in data:
            words.append(line.strip())
    user = user_name()
    greet_user(user)
    game_word = choose_word(words)
    print(game_word)
    game(game_word)
        

if __name__ == "__main__":
    main()