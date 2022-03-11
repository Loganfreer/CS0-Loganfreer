'''Demonstrate loops'''

def main():
    while(keeprunnin):
        number = input('Please enter a whole number: ')
        if(number.isnumeric()):
            print('You entered a whole number!')
            keeprunnin = False
        else:
            print(f'you must enter a whole number, try again')
    print(f'your number was {number} ')


'''This program will count the number of digits in a whole number'''

def main():
    
    n = '550418535'
    orig_n = n
    five_counter = 0
    


    '''for i in n:
        if i in n:
            if i == str(5):
                print('we found a 5')
                five_counter += 1
            else:
                print(f'{i} is not a 5')
    else:
        print(f'There are {five_counter} fives in {n}')'''

    n = 1234567495
    orig_num = n
    num_digits = 0
    while(n > 0):
        #n_mod = n%10
        n, n_mod = divmod(n, 10)
        if(n_mod == 5):
            five_counter += 1

        #n = n//10
    else:
        print(f'There are {five_counter} fives in {orig_num}')
    
main()
    

