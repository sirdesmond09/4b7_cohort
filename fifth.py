import random
import time
from datetime import datetime

# dice = [1,2,3,4,5,6]
# print("Shuffling......")
# time.sleep(3)
# random.shuffle(dice)

# print('shuffle complete. Computer selecting.....Please wait')

# time.sleep(3)

# computer_choice = random.choice(dice)
# # pop_sample = random.sample(dice, 3)


# print(f'Computer selected {computer_choice}')
# # print(pop_sample)

# date = datetime.now()

# print(date)

# string_format = datetime.strftime(date, '%A, %d of %B, %Y')

# print(string_format)

#CONDITIONALS

# user_input = input("Enter your age\n>")


# if user_input.isdigit():
#     user_input = int(user_input)
#     if user_input < 18:
#         print("You cannot vote at this time")
        
#     elif user_input <= 50:
#         print("You are eligible to vote")
        
#     else:
#         print("You are overaged")
        
# else:
#     print("Invalid Input")
    
    
    
    
print("Welcome to this game")
print("Enter H for help or any other key to continue")
user_input = input('>').lower()

help_ = """
This is a simple terminal game where you have to guess a word and if your word is equal to the computer's choice, then you win!!!

Select from the given list of words.
"""
if user_input == 'h': 
    print(help_)
    
    
my_list = ['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
random.shuffle(my_list)
print(my_list)
user_choice = input("Guess the word:\n>").lower()
computer = random.choice(my_list)

if user_choice in my_list:
    if user_choice==computer:
        print("You win")
    else:
        print(f"Computer selected {computer}")
        print("Try again")
else:
    print("Invaid input. Game over!!!")