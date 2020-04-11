# -*- coding: utf-8 -*-
"""
    This is simple basic bank system where amount can be deposited , withdraw and balance can be checked
    
    Algorithm follows:
        1. define class BankAccount
        2. set initial bank account to 0 and ask user how much they want to deposit
        3. withdraw amount if requested amount is less than or equal to balance
        4. return ifrequested amount is higher than balance 
        5. display the amount 
"""
class BankAccount:
    
    def __init__(self):
        self.balance = 0
        print('Welcome to Dummy Bank! ')
        
    def deposit(self):
        
        amount = float(input('Enter amount to be deposited: '))
        self.balance += amount
        print('You Deposited {}'.format(self.balance))
        
    def withdraw(self):
        
        amount = float(input('Enter amount to be withdraw: '))
        
        if self.balance >= amount:
            self.balance -= amount
            print('You withdraw {}'.format(self.balance))
            
        else:
            print('Insufficient Balance!')
             
        
    def display(self):
        print('\n')
        print('Your Balance: ',self.balance)
        
        

# Creating Bank Account in Dummy Bank for bankuser1
bankuser1 = BankAccount()

# bankuser1 depositing amount in his/her account BankAccount()
bankuser1.deposit()

# bankuser1 withdrawing amount from his/her BankAccount()
bankuser1.withdraw()

# bankuser1 requesting his/her net balance left
bankuser1.display()
