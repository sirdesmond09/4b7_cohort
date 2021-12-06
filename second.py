# a_list = ['This', 'is', 'a', 'list', 'and', 'I', 'am', 'happy', 'about', 'this', 'list']

# # print(a_list.pop(4))
# # print(a_list.remove('This'))
# # print(a_list)

# # a = input('Enter your word: ')
# # a_list.remove(a)


# # popped = a_list.pop(a_list.index('about'))
# # print(popped)

# # a_list[0], a_list[4] = 'and', 'This'

# # print(a_list)

# a_list.sort()
# # c_list = a_list.copy()


# # a_list[0] = 'Changed'

# # print(a_list)
# # print(b_list)
# # print(c_list)


# list1 = [54,44,27,79,91,41]
# l1 = {54,44,27,79,91,41}
# # index_4 = list1.pop(4)

# # list1.insert(1, index_4)
# # list1.append(index_4)
# # list1[0] = 1
# l1.pop(2)
# print(l1)


a = {1, 5, 7, 2}
b = {5, 2, 9, 6}

# c = a.union(b)
# print(a)
# print(c)


# a.update(b)
# print(a)


# c = a.intersection(b)
# print(c)
# a.intersection_update(b)
# print(a)


# c = a.difference(b)
# print(c)
# a.difference_update(b)
# print(a)

# c = a.symmetric_difference(b)
# print(c)
# a.symmetric_difference_update(b)
# print(a)


# english = input("English students: \n>")
# french = input("French students: \n>")
# english_set = set(english.split())
# french_set = set(french.split())

# both = english_set.union(french_set)

# print(len(both))


# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# print("Original list", sample_list)

# sample_list = list(set(sample_list))
# print("unique list", sample_list)

# t = tuple(sample_list)
# print("tuple ", t)

# print("Minimum number is: ", min(t))
# print("Maximum number is: ", max(t))


# my_dict = {}
a_dict = {"key":2, "hey":0, "bey":6, "jay":2}

# my_dict['new_key'] = 9 # add new key, value pair

# print(my_dict)

# username = input("Enter username\n>")
# password = input("Enter password\n>")

# my_dict[username]=password

# print(a_dict['ksjdfsnfvun'])


# print(a_dict.get('keys', 6))

# print(a_dict.keys())
# print(a_dict.values())
# print(a_dict.items())

# str = "My salary is 7000"
# print(str.isalnum())

# strOne = str("pynative")
# strTwo = "pynative"
# print(strOne == strTwo)
# print(strOne is strTwo)

# print("John" > "Jhon")
# print("Emma" < "Emm")

# str1 = "my isname isisis jameis isis bond";
# sub = "is";
# print(str1.count(sub, 4))

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)