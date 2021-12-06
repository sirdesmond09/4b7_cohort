# password = input("Enter password to be validated:\n>")

# if password.isnumeric():
#     print('Your password is entirely numeric and not strong enough')
# elif password.isalpha():
#     print("Your password is entirely numeric and not strong enough")
# else:
#     print('You have a strong pasword')
    
    
# # WEEK 2 ASSIGNMENT
# my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
# final_list =" ".join(my_list)
# print(final_list)
# new_list = ['this', "brown", 55, "oxen", True, 0.85]
# new_list[4] = False
# print(new_list)


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# print(list1[2][2][0] + list1[2][3])


# #WEEK 3 ASSIGNMENT

# import math

# r =   int(input("Enter radius:\n>"))
# print(math.pi * (r**2))

# seq  = input("Enter numbers seperated by comma\n>")
# to_list = seq.split(',')
# to_tuple = tuple(to_list)

# print(to_list)
# print(to_tuple)


# name = input("Enter your name\n>")
# names = name.split()
# print(names[1] + " " + names[0])

# elements = ["This", "boy", "is", 2]
# elements = list(map(str, elements))
# print(" ".join(elements))


# num = int(input("Enter a number\n>"))
# prime = True
# if num <= 1:
#     prime = False
    
# if num == 2:
#     prime = True
    
# for factor in range(2,num):
#     if num%factor == 0:
#         prime = False
#         break
    
# if prime:
#     print("Prime Number")
# else:
#     print('Not prime')



# password = input("enter password\n>")
# if password.isnumeric():
#     print("not valid")
# elif password.isalpha():
#     print("not valid")
# elif password.islower():
#     print("not valid")
# elif password.isalnum():
#     print("not valid")
# elif (len(password)<8):
#     print("not valid")
# else:
#     print("you have a valid password")        
    
    
    
# or


# capital_list = []
# small_list = []
# password = input("Enter your password. Password must contain: \r\nat least an integer, \r\na capital letter,\r\na capital letter,\r\na small letter,\r\na specialcharacter\r\nand must be more than 8 characters\r\n> ")
# if not(password.isalnum()) and not password.isdigit() and not password.isalpha() and len(password)>=8:
    
#     if any(password.lower()) and any(password.upper()):
#         print("Password is strong and valid")        
#     else:
#         print("Password must contain: \r\nat least an integer, \r\na capital letter,\r\na capital letter,\r\na small letter,\r\na specialcharacter\r\nand must be more than 8 characters")
# else:
#     print("Password must contain: \r\nat least an integer, \r\na capital letter,\r\na capital letter,\r\na small letter,\r\na specialcharacter\r\nand must be more than 8 characters")            



password = input("Enter your password. Password must contain: \r\nat least an integer, \r\na capital letter,\r\na capital letter,\r\na small letter,\r\na specialcharacter\r\nand must be more than 8 characters\r\n> ")

special_char = ['@', '$', '#']
isValid = True

if len(password) < 6:
    print("Password length should not be less than 6")
    isValid = False
if len(password) > 16:
    print("Password length should not be more than 16")
    isValid = False
if not any(char.isdigit() for char in password):
    print("Password should contain at least a number")
    isValid = False
if not any(char.islower() for char in password):
    print("Password should contain at least a lowercase letter [a-z]")
    isValid = False
if not any(char.isupper() for char in password):
    print("Password should contain at least a uppercase letter [A-Z]")
    isValid = False
if not any(char in special_char for char in password):
    print("Password should contain at least a special character [@$#]")
    isValid = False
    
if isValid:
    print("Password is valid")
else:
    print("Invalid Password")