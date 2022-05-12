'''
Name:; Logan Freerksen
Date: 04/28/22

'''
import random
import os

def user_name():
    #Ask user what their namem is 
    user = input('Welcome to the Hangman game! What is your name? ')
    return user

def greet_user(user):
    #Greet the user using their name 
    print(f"Nice to meet you {user}, your goal is to guess the mystery word in less than 6 tries")

def choose_word(words):
    #Choose a random word from the  imported word file
    game_word = random.choice(words)
    return str(game_word)
         

def play_again():
    #Function asking the user if they want to play hangman again
    response = input("It looks like your game is over, would you like to play again? [y/n] ")
    if response.lower()  == 'y' or response.lower() == 'yes':
        print("Alright! Lets play again")
        return True
    else:
        print("Goodbye")
        return False
                    
def clearScreen():
    
    #function that clears the console/terminal
    
    if os.name == 'nt': # if os is windows
        os.system('cls') # run cls command
    else:
        os.system('clear')  # run clear command



def game(game_word):
    #The following are the stages of hangman
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
    #Initialize the number of wronng attempts to 0
    attempts = 0
    #Split the game word into a list of characters
    word_list = list(game_word)
    #Initialize a list that shows the amount of characters in game_word
    blank_word = []
    #Initialize list of the letters guessed by the user
    letters_guessed = []

    #Print the empty gallow of hangman to start it off
    print(f"{stages[0]}")

    #For the number of charachters in the game word add an underline to the blank word list
    for k in range(len(word_list)):
        blank_word.append("_")
    #Print out blank word list at the beginning of the game so user can see the number of characters in the word
    print(f"{blank_word}")
    
    #Main loop of the game
    while (attempts <= 6):
        #Asks the user for a guees of whats in the game word
        guess = input("Guess a letter of the alpabet that you think is in the mystery word: ")
        #converts the guess to lowercasee for examination
        guess = guess.lower()
        #Checks to see if the inputed guess is one letter
        if len(guess) == 1 and guess.isalpha():
            #Checks to see if the user already guesses that letter 
            if guess in letters_guessed:
                print(f"You already guessed the letter {guess}")
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
            elif guess not in game_word:
                #Checks to see it the guess is not in game word and increases the attempts counter
                print(f"{guess} is not in the mystery word sorry")
                attempts += 1
                letters_guessed.append(guess)
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
            else:
                #Checks to seee that the guess is in tha game word, and then adds it to the correct spot in the blank word list
                #andn appends tht guess to letters guessed
                print(f"Good job! {guess} is in the mystery word")
                for i in range(len(word_list)):
                    if guess in word_list[i]:
                        blank_word[i] = guess
                letters_guessed.append(guess)
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
        elif len(guess) == len(game_word) and guess.isalpha():
            #Checks to see if the user is trying to guess the game word
            if guess != game_word:
                #If guesss is not the game word then the atteempts counter is increased
                print(f'{guess} is not the mystery word')
                attempts += 1
                print(f"{stages[attempts]}")
                print(f"{letters_guessed}")
                print(f"{blank_word}")
            else:
                #If guess is the game word then the user is congratulated and the game function breaks out
                print(f"Congratualations! The mystery word was indeed {guess}")
                break
        else:
            #Cheks to see if the guess is any character other than a letter or the game word itself
            print("Not a valid input")
        if attempts == 6:
            #When the player has ran through all of the stages of hang man then they are notified of their loss and what 
            #the word was
            print("Sorry you seem to have lost the game")
            print(f"The mystery word was {game_word}")
            break
        if blank_word == word_list:
            #If the user guesses the game word letter by letter and wins, they are notified of their win
            #and the gme function breaks out
            print(f"Conratualtions! you found the mystery word {game_word}")
            break

            

def main():
    clearScreen()
    #Initializes list for the possible words
    words = []
    #Reads in words from the words.txt file
    with open("Lectures/Assignments/Final/words.txt") as fin:
        data = fin.readlines()
        for line in data:
            words.append(line.strip())
    #Runs through program
    user = user_name()
    greet_user(user)
    game_word = choose_word(words)
    game(game_word)
    #Once the game function is over runs the play again function 
    while play_again():
        game_word = choose_word(words)
        game(game_word)
    
    

        

if __name__ == "__main__":
    main()