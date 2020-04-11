# -*- coding: utf-8 -*-
"""
     1. Get the random number
     
     2. guess the number
     
     3. if random number equal to guessed number then 'You win!' and if not then 'You Lose!'

"""
import random

random_number = random.randint(0, 20)

guessed_number = int(input('Guess The Number : '))

if random_number == guessed_number:
    print('You Win!')
    
else:
    print('You Lose!')
    