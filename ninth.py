import random

def play_game(trial, scores):
    
    while trial >0:
                    
        my_list = ['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
        random.shuffle(my_list)
        print('\n', my_list)
        user_choice = input("\nGuess the word:\n>").lower()
        computer = random.choice(my_list)

        if user_choice in my_list:
            
            if user_choice==computer:
                print("You win")
                trial +=1
                print(f"\n{trial} trial(s) left\n")
                
                scores+=3
                continue
            else:
                print(f"Computer selected {computer}")
                print("Try again")
        else:
            print("Invaid input. Try again.")
        trial -=1
        print(f"\n{trial} trial(s) left\n")
        
    answer = input("Do you want to play again y/n\n>").lower()
    if answer == 'y':
        new_trial = 3
        new_scores = 0
        return play_game(new_trial, new_scores) 
    else: 
        return scores

with open('guess_database.txt', 'r') as file:
    doc = file.read()
    users =eval(doc)
    

print("Welcome to this game")

while True:
    
    input_data = input("Enter l to login or s to signup.\nEnter any other key to quit.\n>").lower()

    if input_data == 'l':
        username = input("Username: ")
        password = input("Password: ")
        
        user = users.get(username)
        
        if user is not None and user['password'] == password:
            
            print("Enter H for help or any other key to continue")
            user_input = input('>').lower()

            help_ = """
            This is a simple terminal game where you have to guess a word and if your word is equal to the computer's choice, then you win!!!

            Select from the given list of words.
            """
            if user_input == 'h': 
                print(help_)
                    
            trial = 3
            scores = 0
            
            scores = play_game(trial, scores)
            
            if scores > user['high_score']:
                user['high_score'] = scores  
            
        else:
            print("Please enter a valid username and password")
    elif input_data == 's':
        print()
        username = input("Username: ")
        password = input("Password: ")
        
        users[username] = {
            'password':password,
            'high_score':0
        } 
    
    else:
        print('\nGood bye')
        break
        

with open('guess_database.txt', 'w') as file:
   file.write(f'{users}')