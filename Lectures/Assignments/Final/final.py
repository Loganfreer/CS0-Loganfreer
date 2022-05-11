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
         

def play_again():
    response = input("It looks like your game is over, would you like to play again? [y/n] ")
    if response.lower()  == 'y' or response.lower() == 'yes':
        print("Alright! Lets play again")
        return True
    else:
        print("Goodbye")
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
    letters_guessed = []
    print(f"{word_list}")
    
    print(f"{stages[0]}")

    for k in range(len(word_list)):
        blank_word.append("_")

    print(f"{blank_word}")
    
    while (attempts <= 6):
        guess = input("Guess a letter of the alpabet that you think is in the mystery word: ")
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha(): 
            if guess in letters_guessed:
                print(f"You already guessed the letter {guess}")
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
            elif guess not in game_word:
                print(f"{guess} is not in the mystery word sorry")
                attempts += 1
                letters_guessed.append(guess)
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
            else:
                print(f"Good job! {guess} is in the mystery word")
                for i in range(len(word_list)):
                    if guess in word_list[i]:
                        blank_word[i] = guess
                letters_guessed.append(guess)
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
        elif len(guess) == len(game_word) and guess.isalpha():
            if guess != game_word:
                print(f'{guess} is not the mystery word')
                attempts += 1
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
            else:
                print(f"Congratualations! The mystery word was indeed {guess}")
                break
        else:
            print("Not a valid input")
        if attempts == 6:
            print("Sorry you seem to have lost the game")
            break
        if blank_word == word_list:
            print(f"Conratualtions! you found the secret word {game_word}")
            break

            

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
    while play_again():
        game_word = choose_word(words)
        print(game_word)
        game(game_word)
    
    

        

if __name__ == "__main__":
    main()