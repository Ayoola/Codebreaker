###########################
### --- CODEBREAKER --- ###
## --Nope--Close--Match--##
###########################


# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

import random

def generate_digits():
    digits = list(range(10))
    random.shuffle(digits)
    return (digits[:3])

def str_to_list(str):
    list = []
    [list.append(int(i)) for i in str]
    return list

def is_close(digits,guess):
    for i in guess:
        if i in digits:
            return True
    return False

def is_match(digits,guess):
    for i in range(len(guess)):
        if guess[i]==digits[i]:
            return True
    return False

def is_exact(digits,guess):
    if guess == digits:
        return True
    return False

def play():
    digits = generate_digits()
    print(digits)

    while True:
        guess = str(input("What is your guess? "))
        guess = str_to_list(guess)
        print(guess)

        if is_exact(digits,guess):
            print "Congrats, YOU BROKE IN!"
            break
        elif is_match(digits,guess):
            print "Match"
        elif is_close(digits,guess):
            print "Close"
        else:
            print "Nope"

play()
