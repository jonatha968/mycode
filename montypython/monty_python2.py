#!/usr/bin/env python3

round = 0

while True:

    round = round + 1 

    print('How does you know if she is a witch, "She ____ "')

    answer = input("Your guess--> ")

    if answer == 'She floats':
        print('Correct')
        break
    elif round ==3:
        print("Sorry, the answer was She Floats.")
        break
    else:
        print("Sorry! Try Again!")
        
