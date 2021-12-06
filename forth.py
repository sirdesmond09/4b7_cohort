# my_list = [34,223,11,23,5,34,57,8,22]
# print(f"The sum is {sum(my_list)}")
# print(f"The sum is {sum(my_list)}")



# general_equation = lambda a,b,c : (-b + (b**2 - (4*a*c))**0.5)/2*a


# print(general_equation(1,2,3))

# to_lower = lambda word : word.lower()

# print(to_lower("GDUDOUFDNFNDP"))



# unique_words = lambda sentence: list(set(sentence.lower().split()))


# word = "This is a sentence and this sentence is a good one"

# print(unique_words(word))


# my_func = lambda x: x**2

# my_list = [33,32,4,6,21,12]

# # mapped = map(my_func, my_list)

# # print(mapped)
            
# print(my_func(my_list[3]))




# students = input("Enter ages of students:\n>")
# ages = list(map(lambda x:int(x), students.split())) 
# print("The oldest person is {} years old".format(max(ages)))
# print("The youngest person is {} years old".format(min(ages)))
# print("The sum of student's age is {} years old".format(sum(ages)))
# print("The average age is {} years old".format(sum(ages)/len(ages)))
# print("There are {} students in the class".format(len(ages)))


#16. Write a Python program to convert a given list of strings into list of lists using map function. 


# a_list = ["RED", "BLUE", 'GREEN']

# result = list(map(list, a_list))

# print(result)


a = list(range(40,51))
# print(a)




even_numbers = filter(lambda x: x%2!=0, a)
print(list(even_numbers))


a = ['5', '2', 'boy', 'jide']

print(list(filter(lambda x: x.isnumeric(), a)))

