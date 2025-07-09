## Conditional logic
# condition_1 = True
# condition_2 = True
# if condition_1 and condition_2:
#     print('Both conditions are True')
# elif condition_1:
#     print('Condition 1 is True')
# elif condition_2:
#     print('Condition 2 is True')
# else:
#     print('Both conditions are False')

## Ternary Operators (if_true if condition else if_false)
# is_friend = True
# can_message = 'DM allowed' if is_friend else 'DM not allowed'
# print(can_message)

## Short Circuiting
# a = True
# b = False
# if a or c:              # The error is intentional
#     print('Hello')
##
# a = False
# b = True
# if a and c:             # The error is intentional
#     print('Hello')

## Logical Operators
# print(4 < 5)
# print('a' > 'A')
# print(3 == 3)
# print(1 < 2 < 3 < 4)
# print(1 >= 0)
# print(5 <= 5)
# print(5 != 6)
# print(1 and 2)      # errors.py
# print(0 or 1)       # errors.py
# print(not 5)

## Exercise for conditional programming
# is_magician = False
# is_expert = True
## SOLUTION 1
# if is_magician and is_expert:
#     print('You are a master magician')
# elif is_magician:
#     print('At least you are getting there')
# else:
#     print('You need magical powers')
## SOLUTION 2
# if is_magician and is_expert:
#     print('You are a master magician')
# elif is_magician and not is_expert:                 # errors.py
#     print('At least you are getting there')
# elif not is_magician:                               # errors.py
#     print('You need magical powers')

## is vs ==
# print(True == 1)
# print('1' == 1)
# print(2 == 1)
# print(10 == 10.0)
# print([] == [])
##
# print('1' is '1')
# print(2 is 2)
# print(10 is 10.0)
# print([] is [])
# print([1,2,3] is [1,2,3])

## For Loops
# for item in [1,2,3]:
#     for number in 'Hello':
#         print(number,item)
##
# user = {
#     'name':'Golem',
#     'age':100,
#     'can_swim':False
# }
# for item in user:
#     print(item)
# for item in user.items():
#     print(item)
# for item in user.keys():
#     print(item)
# for item in user.values():
#     print(item)
# for key,value in user.items():
#     print(key,value)

## Exercise for For Loops (Print the sum of all the numbers in the given list.)
# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for item in my_list:
#     counter = counter + item
# print(counter)

## Use of range() in loops
# for number in range(10):
#     print(number)
# for _ in range(2):
#     print(list(range(5)))

## Enumerate
# for index,char in enumerate('Hello'):
#     print(index,char)
## Exercise for enumerate (print the index of number 5)
# for index,char in enumerate(list(range(10))):
#     if char == 5:
#         print(index)

## While loops
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
#     break
# else:
#     print('The End')

## Exercise
# my_list = [1,2,3]
## For loop
# for item in my_list:
#     print(item)
## While loop
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i = i + 1
##
# while True:
#     response = input('say something: ')
#     if response == 'bye':
#         break

## Exercise (GUI)
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for line in picture:
#     for pixel in line:
#         if pixel == 0:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print('')        

## Exercise (Print all the duplicates in a list)
# my_list = ['a','b','c','b','d','a']
# duplicate = []
# for item in my_list:
#     if my_list.count(item) > 1:
#         if item not in duplicate:
#             duplicate.append(item)
# print(duplicate)

## Functions
# def say_hello(name,age):
#     print(f'hello {name}. You are {age} years old.')
# say_hello('Jon',29)     # Positional arguments
# say_hello('Smith',30)

# def say_hello(name='Chris',age=20):                    # Default parameters
#     print(f'hello {name}. You are {age} years old.')
# say_hello(name='Jon',age=29)                   # Keyword arguments
# say_hello(age=30,name='Smith')
# say_hello()

# def my_sum(num1,num2):
#     return num1 + num2
# print(my_sum(10,5))

## Exercise
## SOLUTION 1
# def sum_1(num1,num2):
#     def sum_2(n1,n2):
#         return n1 + n2
#     return sum_2(num1,num2)
# print(sum_1(10,20))
## SOLUTION 2
# def sum_1(num1,num2):
#     def sum_2(n1,n2):
#         return n1 + n2
#     return sum_2                 # sum_2(num1,num2)
# total = sum_1(0,0)               # sum_1(num1,num2)
# print(total(10,20))              # total(n1,n2)

## Docstrings
# def my_func(name):
#     '''
#     info: This function prints the name
#     '''
#     print(name)
# help(my_func)
# print(my_func.__doc__)

## *args and **kwargs
# def my_func(*args,**kwargs):
#     total = 0
#     for items in kwargs.values():
#         total = total + items
#     return sum(args) + total
# print(my_func(1,2,3,4,5,num1=5,num2=10))

## Exercise (Print the highest even from a list of numbers given as an argument while calling the function)
# def highest_even(li):
#     evens = []
#     for items in li:
#         if items % 2 == 0:
#             evens.append(items)
#     return max(evens)
# print(highest_even([10,2,3,4,8,11]))

## Walrus Operator
# a = 'helloooooooooo'
# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")

# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
# print(a)
