'''
Name: Logan Freerksen
Date: 04/07/22

This program will take in 5 strings of up to at most 11 characters with the characters being
either upper-case letters, digits 0-9 or '-'. The goal of the program is to look for instances in 
which the string has the characters FBI present. If FBI is found in any of the strings the program will
output which strings in which it was found. If FBI is not found the the program will print out, 'He got away'
'''

def is_first_str(s1):
    for i in range(len(s1)):
        if s1[i] == 'F':
            if s1[i] + s1[i+1] + s1[i+2] == 'FBI':
                return True
            else:
                return False

def is_sec_str(s2):
    for i in range(len(s2)):
        if s2[i] == 'F':
            if s2[i] + s2[i+1] + s2[i+2] == 'FBI':
                return True
            else:
                return False

def is_third_str(s3):
    for i in range(len(s3)):
        if s3[i] == 'F':
            if s3[i] + s3[i+1] + s3[i+2] == 'FBI':
                return True
            else: 
                 return False

def is_fourth_str(s4):
    for i in range(len(s4)):
        if s4[i] == 'F':
            if s4[i] + s4[i+1] + s4[i+2] == 'FBI':
                return True
            else:
                return False

def is_fifth_str(s5):
    for i in range(len(s5)):
        if s5[i] == 'F':
            if s5[i] + s5[i+1] + s5[i+2] == 'FBI':
                return True
            else:
                return False

def output(i1, i2, i3, i4, i5):
    if(i1 == True):
        print("1")
    elif(i1 == True and i2 == True):
        print("1 2")
    elif(i1 == True and i2 == True and i3 == True):
        print("1 2 3")
    elif(i1 == True and i2 == True and i3 == True and i4 == True):
        print("1 2 3 4")
    elif(i1 == True and i2 == True and i3 == True and i4 == True and i5 == True):
        print('1 2 3 4 5')
    
    else:
        print("HE GOT AWAY")
        

def main():
    a = 'N321-CIAFB3'
    b = 'F3-FI12I'
    c = 'F-BI-12'
    d = 'OVO-JE-CIA'
    e = 'KRIJUMCAR1'
    i1 = is_first_str(a)
    i2 = is_sec_str(b)
    i3 = is_third_str(c)
    i4 = is_fourth_str(d)
    i5  = is_fifth_str(e)
    output(i1, i2, i3, i4, i5)
    

if __name__ == "__main__":
    main()