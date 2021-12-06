# file = open('my_file.txt', 'w')
# file.writelines(
#     ["""This is a very good  file.
# This is another line.  But, I don't like this.
#     Welcome on board.
    
#         jfisnfvndsfiv. """, "\nTHIS IS ANOTHER STRING."]
# )

# file.close()

# file = open('my_file.txt', 'r')
# lines = file.readlines()

# for line in lines:
#     print(line)


# file = open('my_file.txt', 'a')

# file.write("\nI just got appended.")
# file.close()

# data = {
#     "name":"Desmond"
# }
# with open('my_file.txt', 'w') as file:
#     file.write(f'{data}')


# with open('my_file.txt', 'r') as file:
#     doc = file.read()
#     s =eval(doc)
    
# print(s.get("title"))
    
# a = "5"
# b = "['4', '3','45']"

# print(type(b))
# print(sum(map(int, eval(b))))

# import random

# with open('guess_database.txt', 'r') as file:
#     doc = file.read()
#     users =eval(doc)
    

# print("Welcome to this game")

# while True:
    
#     input_data = input("Enter l to login or s to signup.\nEnter any other key to quit.\n>").lower()

#     if input_data == 'l':
#         username = input("Username: ")
#         password = input("Password: ")
        
#         user = users.get(username)
        
#         if user is not None and user['password'] == password:
            
#             print("Enter H for help or any other key to continue")
#             user_input = input('>').lower()

#             help_ = """
#             This is a simple terminal game where you have to guess a word and if your word is equal to the computer's choice, then you win!!!

#             Select from the given list of words.
#             """
#             if user_input == 'h': 
#                 print(help_)
                    
#             trial = 3
#             scores = 0
#             while trial >0:
                    
#                 my_list = ['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
#                 random.shuffle(my_list)
#                 print('\n', my_list)
#                 user_choice = input("\nGuess the word:\n>").lower()
#                 computer = random.choice(my_list)

#                 if user_choice in my_list:
                   
#                     if user_choice==computer:
#                         print("You win")
#                         trial +=1
#                         print(f"\n{trial} trial(s) left\n")
                        
#                         scores+=3
#                         continue
#                     else:
#                         print(f"Computer selected {computer}")
#                         print("Try again")
#                 else:
#                     print("Invaid input. Try again.")
#                 trial -=1
#                 print(f"\n{trial} trial(s) left\n")
             
#             if scores > user['high_score']:
#                 user['high_score'] = scores  
            
#         else:
#             print("Please enter a valid username and password")
#     elif input_data == 's':
#         print()
#         username = input("Username: ")
#         password = input("Password: ")
        
#         users[username] = {
#             'password':password,
#             'high_score':0
#         } 
    
#     else:
#         print('\nGood bye')
#         break
        

# with open('guess_database.txt', 'w') as file:
#    file.write(f'{users}')

boy = 10

def is_prime(n):
    if n <= 1:
        return False
        
    if n == 2:
        return True
    
    for factor in range(2,n):
        if n%factor==0:
            return False
        
    return True



# print(is_prime(1))
   

def add_num(*args):
    return sum(args)


data = [1,2,4,3,5,4,2]
print(add_num(*data))



def adsss(**kwargs):
    print(kwargs)
    
def ads(a,b,c=3):
    return a*b+c
    
a = {'a': 3, 'b': 4, 'c': 2}
# adsss(**a)
print(ads(**a))

