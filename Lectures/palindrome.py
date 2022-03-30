'''
This program will determine if an inputed string is a palindrome (same forwards and backwords)
'''



def input_name():
    firstname = input('Please enter your first name: ')
    return firstname

def greet_player(first_name):
    print(f'Welcome {first_name} to my program')
    print(f'This will determine if a string is a plaendrome (same forwards as backwards)')

def input_string():
    inputed_string = input("Please enter a string to see if it is a palendrome: ")
    return inputed_string

def is_palendrome(in_string):
    for ch in range(len(in_string)):
        #print(f'ch = {in_string[ch]}')
        if (in_string[ch] != in_string[-ch-1]):
            print(f'{in_string} is not a palendrome!')
            break
        else:
            print(f'{in_string} is a palendrome!')


def main():
    first_name = input_name()
    greet_player(first_name) 
    
    in_string = input_string
    is_palendrome(in_string)

if __name__ == "__main__":
    main()