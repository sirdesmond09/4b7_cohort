# def new_line():
#     print('.')
    

# def three_lines():
#     new_line()
#     new_line()
#     new_line()
    
    
# def nine_lines():
#     three_lines()
#     three_lines()
#     three_lines()
    
# def twenty_five():
#     nine_lines()
#     nine_lines()
#     three_lines()
#     three_lines()
#     new_line()
    
    
# twenty_five()

# def add_value(func):
#     def wrapper():
#         original_result = func()
#         modified =original_result.split("!")[0] + " world!" 
#         return modified
#     return wrapper


# @add_value
# def greet():
#     return 'Hello!'

# print(greet())


user = {}

def authenticate(func):
    def inner():
        username = input("Username:\n>")
        password = input("Password:\n>")
        
        if user.get(username) != None and user.get(username)['password'] == password:
            return save_payment
        else:
            print("Invalid login")
            return
    return inner




@authenticate
def save_payment():
    print("Your payments has been saved!")
    
    
save_payment()