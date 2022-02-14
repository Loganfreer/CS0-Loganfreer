'''
Name: Logan Freerksen
Date: 02/14/22

This program will ask the user for their name and show a few stages 
of the game Hangman.

Step 1: Prompt user to enter their name, and store the name in a variable
Step 2: Greet the player with their name
Step 3: Print to user what the program does
Step 4: Print out several stages of the game Hangman
'''
#Step 1
Name = input("Hey there, what's your name? \n")
#Step 2
print('Hey', Name,'1')
#Step 3
print('''The hangman game under construction, maybe you'll get to play it in a few weeks…
This is what various stages of the hangman game will look like…
''')
#Step 4
print('Stage 0')
print('''
    |__________________ 						
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
-------------
''')
print('Stage 1')
print('''
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
''')
print('Stage 2')
print('''
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
''')
print('Stage 3')
print('''
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
''')
print('Stage 4')
print('''
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
''')
print('Thank you for watching!')
