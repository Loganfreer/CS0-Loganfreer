'''
Name: Logan Freerksen
Date: 04/07/22

This program will take in 5 strings of up to at most 11 characters with the characters being
either upper-case letters, digits 0-9 or '-'. The goal of the program is to look for instances in 
which the string has the characters FBI present. If FBI is found in any of the strings the program will
output which strings in which it was found. If FBI is not found the the program will print out, 'He got away'
'''




#Putting given input strings into a iterable list
def create_list(a,b,c,d,e):
    inp_uts = [a, b, c, d, e]
    return inp_uts

#Looking for the String FBI in the given strings
def FBI_test(inp_uts):
    b = ""
    for i in range(len(inp_uts)):
        if 'FBI' in inp_uts[i]: 
            b += str(i+1) + " "
    if b == "":
        return 'HE GOT AWAY!'
    else:
        return b

#Main running function  
def main():
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    inp_uts = create_list(a,b,c,d,e)
    check = FBI_test(inp_uts)
    print(check)
    
#Calling main function
if __name__ == "__main__":
    main()