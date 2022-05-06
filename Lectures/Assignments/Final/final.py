'''
Name:; Logan Freerksen
Date: 04/28/22

'''
import random

def choose_word(words):
    game_word = random.choice(words)
    return str(game_word)

def game(game_word):
    letters = list(game_word)
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
    wrong_guessed = ''
    correct = []
    correct.append(letters)

    while (attempts <= 6):
        guess = input("Guess a letter of the alpabet that you think is in the mystery word: ")
        for k in range(len(game_word)):
            print('_ '*k, end= '')
        if guess in game_word:
            print("\nGood job!")
            for i in range(len(correct)):
                if guess == correct[i]:
                    print(correct[i])
            
                    
        else:
            print("oops that didnt seem quite right")
            attempts += 1
            print(stages[attempts])
            wrong_guessed = wrong_guessed +  '' + guess
            print(f'{wrong_guessed}')

        if attempts == 6:
            play_again = True
            while (play_again):
                response = input("It looks like you ran out of tries, would you like to give it another shot? [y/n] ")
                if not response.lower()  == 'y' or not response.lower() == 'yes':
                    break 

               
        


def main():
    words = []
    with open("Lectures/Assignments/Final/words.txt") as fin:
        data = fin.readlines()
        for line in data:
            words.append(line.strip())
    game_word = choose_word(words)
    print(game_word)
    game(game_word)
        

if __name__ == "__main__":
    main()