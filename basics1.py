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

## String Index. String Slicing
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

## String methods
# quote = 'to be or not to be'
# print(quote.upper())
# print(quote.lower())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be','me'))
# print(quote)
# quote = quote.replace('be','me')
# print(quote)

## Exercise
# year = int(input ('What year were you born? '))
# age = 2025 - year
# print(f'Your age is {age}')

## Exercise
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
# new_cart = amazon_cart 
# #OR new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)
## Write a program to print oranges from the below list basket
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# print(basket[1][1][0])

# basket = [1,2,3,4,5,3]
# basket.remove(3)
# print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# print(basket)
# print(basket.count('Apples'))
# basket.clear()
# print(basket)

## Exercise (print a sorted list of all of our friends)
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
## Solution 1
# friends.append('Stanley')
# friends.sort()
# print(friends)
## Solution 2
# new_friend = ['Stanley']
# friends.extend(new_friend)
# print(sorted(friends))

## Exercise
# user_profile = {
#     'age' : 25,
#     'username' : 'King',
#     'weapons' : 10,
#     'is_active' : True,
#     'clan' : 'Tiger'
#     }
# print(user_profile.keys())
# user_profile['weapons'] += 1
# user_profile.get('is_banned', False)
# user_profile.update({'is_banned':True})
# user_2 = user_profile.copy()
# user_2.update({'username':'Queen'})
# user_2.update({'age':24})
# print(user_profile)
# print(user_2)