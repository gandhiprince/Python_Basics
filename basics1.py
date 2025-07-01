## Basic print, input and type functions and type conversion
# print('Welcome to the Basics of Python!')
# name = input('What is your name? ')
# age = 22.5
# print('Hello ' + name)
# print(type(age))
# a = int(age)
# print(type(a))

## Turning integers into binary and vice versa
# print(bin(5))
# print(int('101',2))

## Math operations with int and float
# print(1 + 1)
# print(1 - 1)
# print(2 * 3)
# print(4 / 2)
# print(2 ** 3)
# print(3 // 4)
# print(6 % 4)
# print((5 + 4) * 10 / 2)
# print(((5 + 4) * 10) / 2)
# print((5 + 4) * (10 / 2))
# print(5 + (4 * 10) / 2)
# print(5 + 4 * 10 // 2)
# print(round(3.4))
# print(round(3.4549999,2))
# print(abs(-20))

## Augmented Assignment Operator
# counter = 0
# counter += 1
# counter += 1
# counter += 1
# counter += 1
# counter -= 1
# counter *= 2
# print(counter)

## Boolean
# print(bool('True'))
# print(bool('False'))

## Strings
# a = 'Hello'
# b = "World"
# c = '''
# WOW
# 0 0
# ---
# '''
# print(a)
# print(b)
# print(c)

## String Concatenation
# first_name = input('Firt name: ')
# last_name = input('Last name: ')
# full_name = first_name + ' ' + last_name
# print(full_name)

## Escape Sequence
# weather = "\t It's \"kind of\" sunny \n Hope you are doing good"
# print(weather)

## Formatted strings
# print("Hello {}, your balance is {}.".format("Cindy", 50))
# print("Hello {0}, your balance is {1}.".format("Cindy", 50))
# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
##
# name = 'Cindy'
# amount = 50
# print(f'Hello {name}, your balance is {amount}.')

## String Indexes and Slicing
# python = 'I am PYHTON'
# print(python[1:4])
# print(python[1:])
# print(python[:])
# print(python[1:100])
# print(python[-1])
# print(python[-4])
# print(python[:-3])
# print(python[-3:])
# print(python[::-1])

## String Functions
# a = 'Hello'
# print(len(a))

## String methods
# quote = 'to BE or not to BE'
# print(quote.upper())
# print(quote.lower())
# print(quote.capitalize())
# print(quote.find('BE'))
# print(quote.replace('BE','ME'))
# print(quote)
# quote = quote.replace('BE','ME')
# print(quote)

## Exercise for Strings
# year = input('What year were you born? ')
# age = 2025 - int(year)
# print(f'Your age is {age}')

## Exercise for Strings
# name = input('What is your name? ')
# password = input('What is your password? ')
# pass_len = len(password)
# hidden_pass = '*' * pass_len
# print(f'Hey {name}, your password {hidden_pass} is {pass_len} characters long.')

## Exercise for Lists
# new_list = ['a', 'b', 'c']
# print(new_list[1])
# print(new_list[-2])
# print(new_list[1:3])
# new_list[0] = 'z'
# print(new_list)
##
# my_list = [1,2,3]
# bonus = my_list + [5]
# my_list[0] = 'z'
# print(my_list)
# print(bonus)
##
# amazon_cart = ['toys','pens','books']
# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart # new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

## Exercise for Matrix (Write a program to print oranges from the below list basket)
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# print(basket[1][1][0])

## List Functions
# basket = [1,2,3,4,5]
# print(len(basket))

## List Methods
## Adding methods. These methods do not return any value. They just modify the list.
# basket = [1,2,3,4,5]
# basket.append(10)
# basket.insert(3,100)
# basket.extend([11,12,13])   # .extent() takes and iterable
# print(basket)
##
# basket = [1,2,3]
# basket.extend('hello')
# print(basket)
## Removing methods. These methods do not return any value (except .pop()). They just modify the list.
# basket = [1,2,3,4,5]
# basket.pop()
# basket.pop(1)
# basket.remove(3)
# print(basket)
# basket.clear()
# print(basket)
##
# basket = [1,2,3,4,5,3]
# basket.remove(3)
# print(basket)
## index, count and in methods. These methods do not modify the list. They just return a value.
# basket = ['a','b','c','d','e','d']
# print(basket.index('c'))           # .index(value) - returns the index of the given value
# print(basket.index('e',1,5))       # .index(value,start,stop) - returns the index of the given value in given range of index
# print('a' in basket)               # in - returns a boolean value. Checks if the given value exists in the list or not
# print(basket.count('d'))           # .count(value) - returns the number of times the given value exists in the list
## sort, copy and reverse methods.
# basket = ['a','b','c','d','e','d']
# basket.sort()                      # .sort() - Modifies the list. Does not return any value. Works for a list with only string or integer as objects.
# print(basket)
# basket.reverse()                   # .reverse() - Modifies the list. Does not return any value. Reversing can be done using list slicing too (which does not modify the list).
# print(basket)
# new_basket = basket.copy()         # Returns value. Does not modify the list. Copying can be done using list slicing too.
## sorted function
# basket = ['a','b','c','d','e','d']
# print(sorted(basket))              # sorted() - returns a value  but does not modify the list.
# print(basket)
## join method
# space = ' '
# sentence = space.join(['hi','my','name','is','JOJO'])     # .join(iterable) - returns the iterable joined by the given string. Hence, it is a string method.
# print(sentence)
## range
# print(list(range(10)))     # range(stop)
# print(list(range(1,10)))   # range(start,stop)

## Exercise for Lists
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# print(basket)
# print(basket.count('Apples'))
# basket.clear()
# print(basket)

## Exercise for Lists (add Stanley and print a sorted list of all of our friends)
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
## Solution 1
# friends.append('Stanley')
# friends.sort()
# print(friends)
## Solution 2
# new_friend = ['Stanley']
# friends.extend(new_friend)
# print(sorted(friends))
## Solution 3
# new_friend = 'Stanley'
# friends.append(new_friend)
# friends.sort()
# print(friends)

## List unpacking
# a,b,c,*d,e,f = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

## Dictionary
# user = dict(age=30,username='King')
# print(user)

## Dictionary Methods
# user = {
#   'age':30,
#   'username':'King',
#   'weapons':None,
#   'is_active':True,
#   'clan':'Tigers'
# }
# print(user['age'])
# print(user.get('password'))
# print(user.get('password','secret'))
# print('King' in user)
# print('age' in user.keys())
# print('King' in user.values())
# print(user.items())
# user_2 = user.copy()
# user.clear()
# print(user)
# print(user_2.pop('age'))   # returns value of the key and pops it out
# print(user_2)
# print(user_2.popitem())    # returns the last item (both key and value) and pops it out
# print(user_2)
# user_2.update({'outfit':'black','weapons':'gun'})
# print(user_2)

## Exercise for dictionary
# user = {
#   'age':30,
#   'username':'King',
#   'weapons':None,
#   'is_active':True,
#   'clan':'Tigers'
# }
## SOLUTION 1
# print(user.keys())
# user.update({'weapons':'gun'})
# user.update({'is_banned':False})
# user.update({'is_banned':True})
# user_2 = user.copy()
# user_2.update({'username':'Queen','age':20})
# print(user)
# print(user_2)
## SOLUTION 2
# print(user.keys())
# user['weapons'] = 'gun'
# user.update({'is_banned': False})
# user['is_banned'] = True
# user2 = user.copy()
# user2.update({'username':'Queen','age':20})
# print(user)
# print(user2)

## Tuples
# my_tuple = (1,2,3,4)
# print(my_tuple[1])
# print(5 in my_tuple)
# new_tuple = my_tuple[1:3]
# print(new_tuple)

## Tuple Methods
# my_tuple = (1,2,3,4,3)
# print(my_tuple.count(3))
# print(my_tuple.index(2))

## Tuple functions
# my_tuple = (1,2,3,4,3)
# print(len(my_tuple))

## Sets
# my_set = {1,2,3,4,5,3}
# print(my_set)

## Set Methods
# my_set = {1,2,3,4,5,3}
# my_set.add(10)
# print(my_set)
# print(2 in my_set)
# new_set = my_set.copy()
# my_set.clear()
# print(my_set)
# print(new_set)
## Union, intersection, difference, difference update, discard
# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.union(your_set))            # print(my_set | your_set)
# print(my_set.intersection(your_set))
# print(my_set.difference(your_set))       # print(my_set & your_set)
# print(my_set)
# my_set.difference_update(your_set)
# print(my_set)
# my_set.discard(3)
# print(my_set)
## Disjoint
# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.isdisjoint(your_set))       # checks if the two sets are unique
## Subset and Superset
# my_set = {4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.issubset(your_set))
# print(my_set.issuperset(your_set))
# print(your_set.issuperset(my_set))

## Set Functions
# my_set = {1,2,3,4,5,3}
# print(len(my_set))

## Exercise for sets (print a list of students who are absent)
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
# print(school.difference(attendance_list))                  # attendance_list automatically gets converted into a set