# -*- coding: utf-8 -*-
"""
    => did some minor changes from 'guess__the__number__win__or__lose'
      => instead of getting one time correct or not correct guess, let the user guess until he gets correct guess!
    1. import random module again
    2. guess the number
    3. guess the number until user get correct guess
      
        
"""
import random

random_number = random.randint(0, 20)
print(random_number)


while True:
    guessed_number = int(input('Guess The Number: '))
    
    if random_number > guessed_number:
        print('Little High!')
    
    elif random_number < guessed_number:
        print('Little Low!')
        
    else:
        print('You Win!')
        break
        
        
