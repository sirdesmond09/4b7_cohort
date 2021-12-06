#make up class 1
# variable = 'dcd'
# print(type(variable))

# var = 5.0
# print(var)
# print(type(str(var)))






# End of make up class



# my_dict = {
#     "name":"Desmond",
#     "class":"Python",
#     "Country":"U.S.A"
# }


# my_class = my_dict["class"]

# my_dict["height"] = 100

# my_username = input('Enter your username:\n>')
# print(my_username)
# my_dict['username'] = my_username


# print(my_dict)


# details = {}

# name = input("Enter your name:\n>")
# school=input("Enter your school:\n>")
# class_input = input("Enter your class:\n>")
# state =input("Enter your state of residence:\n>")
# marital_status = input("Enter your marital status:\n>")

# details['name'] = name
# details['school'] = school
# details['class'] = class_input
# details['state'] = state
# details['marital_status']=marital_status


# print(details)
# All_details = {}
# detail={}

# firstname = input('Enter your firstname:\n>')
# lastname = input('Enter your lastname:\n')
# age = int(input('Enter your age:\n'))
# Yob =str(2021- age) 
# username=firstname[0:3] + lastname[0:2] + Yob[-2:]

# detail['Firstname'] = firstname
# detail['Lastname'] = lastname
# detail['Age'] = age
# detail['Year of birth'] = Yob

# All_details[username] = detail
# print(All_details)


my_dict = {"name":"Desmond",
           "occupation":"backend dev",
           "location":"silicon valey",
           "zone":"USA"}


# my_dict['country'] = my_dict.pop('zone')
# print(my_dict)

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# zipped = zip(first_list, second_list)
# dictionary = dict(zip(first_list, second_list))
# lists = list(zip(first_list, second_list))
# tuples = tuple(zip(first_list, second_list))
# sets = set(zip(first_list, second_list))

# print(zipped)
# print(dictionary)
# print(lists)
# print(tuples)
# print(sets)

# import random

# print(random.sample(['s','g','i','c','ab', 'ik', 'ify', 'e'], k=4))

# print(random.choice([1,2]))

# dict2 = dict(my_dict)
# my_dict.pop('zone')
# print(my_dict)
# print(dict2)

# dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("age")
# print(temp)

# print(dict())

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)