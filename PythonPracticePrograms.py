import random
# Write a program having a list of employees' ages, count the ages of employees whose age is greater than 35

# emp_list = [35, 20, 30, 41, 34, 38]

# item = 35

# count = 0
# print('len',len(emp_list)-1)
# for i in emp_list:
#     print('i',i)
#     # print('emp', emp_list[i])
#     if i >= item:
#         print('cond', i>=item)
#         count = count + 1
#     else:
#         pass

# print('count', count)

# e = emp_list.count(35)
# print(e)

# count = sum(i >= 35 for i in emp_list)
# print(count)

# c = sum(map(lambda x : x>= 35, emp_list))
# print(c)


# calculator program where u'll take input as first operand, then operator and then second operator and what will be 
# the output will be further evaluated based on the output

# while True:
#     # operand1, operator, operand2 = input("Enter input").split()
#     operand1 = int(input("Enter operand1 "))
#     operator = input("Enter operator ")
#     operand2 = int(input("Enter operand2 "))
#     print('i', operand1, 'j', operator, 'k', operand2)
#     if input == '':
#         break

#     result = 0.0
#     print(' op', operator)
#     print('type'),type(operator)
#     print('cond', operator == '+')
#     if operator == '+':
#         result += operand1 + operand2
#     elif operator == '-':
#         result -= operand1 - operand2
#     elif operator == '*':
#         result *= operand1 * operand2
#     else:
#         result /= operand1 / operand2

    
#     print(result)


# Print triangle in python:

# n = 5
# for i in range(n):
#     for j in range(i):
#         if i == n*j:
#             print('*')


# def add(x, y):
#    return x + y

# # This function subtracts two numbers 
# def subtract(x, y):
#    return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#    return x * y

# # This function divides two numbers
# def divide(x, y):
#    return x / y

# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# # Take input from the user 
# choice = input("Enter choice(1/2/3/4): ")


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print(add(num1, num2))
# elif choice == '2':
#     print(subtract(num1, num2))
# elif choice == '3':
#     print(multiply(num1, num2))
# elif choice == '4':
#     print(divide(num1, num2))
# else:
#     print('Invalid')



# input_val = input("Enter input ")
# print(input_val)


# Exercises from Book Chapter 1:

# Q1

# def is_multiple(n, m):
#     if m % n == 0:
#         return True
#     else:
#         return False


# n = int(input())
# m = int(input())

# ans = is_multiple(n, m)
# print('ans',ans)


# Q2

# def is_even(k):
#     rem = k & 1
#     if rem == 1:
#         return False
#     else:
#         return True


# k = int(input())
# ans = is_even(k)
# print(ans)


# Q3

# def minmax(data):
#     print('data', data)
#     data.sort()
#     print('l', data)
#     minimum = data[0]
#     maximum = data[-1]
#     t = minimum, maximum
#     #t = small, large
#     return t

# data = [1, 5, 4, 9, 2]
# ans = minmax(data)
# print(ans)

# Q4

# def sum_of_squares(n):
#     sum = 0
#     for i in range(1, n+1):
#         print('i in start',i)
#         if i**2 >= n:
#             break
#         else:
#             sum += i ** 2
#             print('sum', sum)
        

#     return sum

# n = int(input())
# ans = sum_of_squares(n)
# print(ans)


# Q5

# def sum_compre(n):
#     ans_sum = 0
#     print('n', n)

#     ans_sum = [sum((i ** 2) for i in range(1, n+1) if (i ** 2 < n))]

#     return ans_sum

# n = int(input())
# ans = sum_compre(n)
# print(ans)


# Q6

# def sum_of_odd_squares(n):
#     sum = 0
#     for i in range(1, n+1, 2):
#         if i**2 >= n:
#             break
#         else:
#             sum += i ** 2
#     return sum

# n = int(input())
# ans = sum_of_odd_squares(n)
# print(ans)


# Q7

# def sum_odd_compre(n):
#     ans_sum = 0
#     print('n', n)

#     ans_sum = [sum((i ** 2) for i in range(1, n+1, 2) if (i ** 2 < n))]

#     return ans_sum

# n = int(input())
# ans = sum_odd_compre(n)
# print(ans)


# Q8

# s = "Hello"
# n = len(s)

# for k in range(-n, 0, 1):
#     print('k', k, 's of k', s[k])

# for j in range(n):
#     print('j', j, 's of j',s[j])


# Q9

# for i in range(50, 90, 10):
#     print(i)


# Q10

# for i in range(8, -9, -2):
#     print(i)

# Q11

# l1 = [(2 ** i) for i in range(0, 9)]
# print(l1)

# Q12


# l = [1, 8, 9, 6, 3, 12]

# # ans = random.choice(l)
# # for i in random.randrange(4):
# ans = random.randrange(0, len(l))
    
# print(ans)


# Q13

# l = [1, 2, 3, 4, 5]

# print('My Way')
# for j in range(len(l), 0, -1):
#     print(j)

# print('Inbuilt function')
# rev = reversed(l)

# for i in rev:
#     print(i)


# Q14

# def odd_product(l):

#     # ans_list = [(j % i != 0) for i in range(0, len(l)) for j in range(-1, -len(l)) if i == (len(l)/2)]
#     # ans_list = [(l[i] % 2 != 0 and l[j] % 2 != 0, l[i], l[j]) for i in range(0, len(l)) for j in range(-1, -len(l), -1) if l[i] != l[j]]
#     ans_list = [(l[i] % 2 != 0 and l[j] % 2 != 0, l[i], l[j]) for i in range(0, len(l)) for j in range(1, len(l)) if l[i] != l[j] and i < j]
#     return ans_list

# l = [1, 2, 3, 5, 7, 8]
# ans = odd_product(l)
# print(ans)


# Q15

# def distinct(l):

#     ans_list = [(l[i], i) for i in range(0, len(l)) for j in range(1, len(l)) if l[i] == l[j] and i < j]
#     return ans_list

# l = [1, 2, 3, 5, 5, 8]
# ans = distinct(l)
# print(ans)

# Q18


# ans = [2*i  for i in range(0, 92) ]

# sum = 0
# for i in range(0, 10):

#     sum += 2 * i 
#     print(sum)

# Not implemented using list comprehension

# Q19

# alpha = [chr(i) for i in range(97, 123)]
# print(alpha)

# Q20

# data = [1, 3, 5, 7, 9]
# # random.shuffle(data)
# ans = random.randint(1, 10)
# print(ans)


# Q21

# import sys

# while True:
#     try:
#         input_str = sys.stdin.readline()
#         print(input_str)
#         sys.stdout.write(input_str)
#         if input_str == '':
#             break
#     except EOFError:
#         print('error')


# Q22

# a = [1, 2, 3]
# b = [2, 3, 4]

# c = [(a[i] * b[j]) for i in range(0, len(a)) for j in range(0, len(b))]

# print(c)

# Q23

# n = []

# for i in range(0, 10):
#     try:
#         n = int(input())
#     except:
#         print('dont try buffer oveload error')

# Q24

# def count_str(string):
#     count = 0
#     for i in string:
#         if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u') or (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#             count += 1

#     return count

# string = input("Enter some string ")
# ans = count_str(string)
# print(ans)

# Q25

# def remove_punctuation(string):
#     copy_str = ''

#     for i in string:
#         if i == "." or i == "'" or i == ",":
#             pass
#         else:
#             copy_str += i

#     return copy_str

# string = input("Enter any string ")
# ans = remove_punctuation(string)
# print(ans)


# Q26

# a = int(input())
# b = int(input())
# c = int(input())

# if c == a + b:
#     print('sum True')
# else:
#     print('sum False')

# if a == b - c:
#     print('sub True')
# else:
#     print('sub False')

# if c == a * b:
#     print('Mult True')
# else:
#     print('Mult False')


# Q29

# characters = ['c', 'a', 't', 'd', 'o', 'g']
# random.shuffle(characters)
# print(''.join(characters))

# Q30

# n = int(input())  # Enter integer val greater than 2

# count = 0

# while n > 2:
#     n = n / 2
#     print('inside ', n)
#     if n > 2:
#         count += 1

# print(count)


# Q32

# class Calci(object):

#     def add(self, x, y):
#         return x + y

#     def subt(self, x, y):
#         return x - y

#     def mult(self, x, y):
#         return x * y

#     def div(self, x, y):
#         return x / y

# x = int(input())
# y = int(input())

# op = input("Enter operator ")

# cal1 = Calci()

# if op == '+':
#     print(cal1.add(x, y))
    

# elif op == '-':
#     print(cal1.subt(x, y))

# elif op == '*':
#     print(cal1.mult(x, y))

# elif op == '/':
#     print(cal1.div(x, y))


## needs to reconsider 
# print star pattern representing letter 'A'

'''
        *

    *   *   *

*               *
'''

# for i in range(1, 5):
#     for j in range(1, 5):
#         # if (i == 0 and j == 2) or (i == 1 and j >= 1 and j <= 3) or (i == 2 and (j == 0 or j == 4)):
#         if j <= i:  
#             print('*', end=' ')
#     print(' ')


# Exercises from Book Chapter - 2

# Q4

# class Flower:

#     def __init__(self, name, num_of_patels, price):
#         self.name = name
#         self.num_of_patels = num_of_patels
#         self.price = price

#     def set_name(self, name):
#         self.name = name

#     def set_patels(self, num_of_patels):
#         self.num_of_patels = num_of_patels

#     def set_price(self, price):
#         self.price = price

#     def get_name(self):
#         return self.name

#     def get_petals(self):
#         return self.num_of_patels
    
#     def get_price(self):
#         return self.price

# flower = Flower('Rose', 100, 50)
# flower.set_name('Jasmine')
# flower.set_patels(20)
# flower.set_price(30)

# print(flower.get_name(), flower.get_petals(), flower.get_price())


# Q5

# class CreditCard:

#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = 0

#     def get_customer(self):
#         return self._customer

#     def get_bank(self):
#         return self._bank

#     def get_account(self):
#         return self._acnt

#     def get_limit(self):
#         return self._limit

#     def get_balance(self):
#         return self._balance

#     def charge(self, price):

#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price 
#             return True

#     def make_payment(self, amount):
#         self._balance -= amount 

# credit_card = CreditCard("Vishakha", "SBI", "Savings", 1000)
# print('Balance : ', credit_card.get_balance())
# print('Charge :', credit_card.charge(1000))
# print('make payment :', credit_card.make_payment(3000))
# print('Balance : ', credit_card.get_balance())


# Q6

# class CreditCard:

#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = 0

#     def get_customer(self):
#         return self._customer

#     def get_bank(self):
#         return self._bank

#     def get_account(self):
#         return self._acnt

#     def get_limit(self):
#         return self._limit

#     def get_balance(self):
#         return self._balance

#     def charge(self, price):

#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price 
#             return True

#     def make_payment(self, amount):
#         if amount <= 0:
#             raise ValueError('Amount cannot be negative')
#         else:
#             self._balance -= amount 
    
# credit_card = CreditCard("Vishakha", "SBI", "Savings", 1000)
# print('Balance : ', credit_card.get_balance())
# print('Charge :', credit_card.charge(1000))
# print('make payment :', credit_card.make_payment(3000))
# print('Balance : ', credit_card.get_balance())


# Q7

# class CreditCard:

#     def __init__(self, customer, bank, acnt, limit, balance=None):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = balance if balance is not None else 0

#     def get_customer(self):
#         return self._customer

#     def get_bank(self):
#         return self._bank

#     def get_account(self):
#         return self._acnt

#     def get_limit(self):
#         return self._limit

#     def get_balance(self):
#         return self._balance

#     def charge(self, price):

#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price 
#             return True

#     def make_payment(self, amount):
#         if amount <= 0:
#             raise ValueError('Amount cannot be negative')
#         else:
#             self._balance -= amount 
    
# credit_card = CreditCard("Vishakha", "SBI", "Savings", 1000)
# print('Balance : ', credit_card.get_balance())
# print('Charge :', credit_card.charge(1000))
# print('make payment :', credit_card.make_payment(3000))
# print('Balance : ', credit_card.get_balance())

# credit_card1 = CreditCard("Vishakha", "SBI", "Savings", 1000, 50000)
# print('Balance : ', credit_card1.get_balance())
# print('Charge :', credit_card1.charge(1000))
# print('make payment :', credit_card1.make_payment(3000))
# print('Balance : ', credit_card1.get_balance())

# credit_card2 = CreditCard("Vishakha", "SBI", "Savings", 1000)
# print('Balance : ', credit_card2.get_balance())
# print('Charge :', credit_card2.charge(1000))
# print('make payment :', credit_card2.make_payment(3000))
# print('Balance : ', credit_card2.get_balance())


# Q8

# class CreditCard:

#     def __init__(self, customer, bank, acnt, limit, balance=None):
#         self._customer = customer
#         self._bank = bank
#         self._acnt = acnt
#         self._limit = limit
#         self._balance = balance if balance is not None else 0

#     def get_customer(self):
#         return self._customer

#     def get_bank(self):
#         return self._bank

#     def get_account(self):
#         return self._acnt

#     def get_limit(self):
#         return self._limit

#     def get_balance(self):
#         return self._balance

#     def charge(self, price):

#         if price + self._balance > self._limit:
#             return False
#         else:
#             self._balance += price 
#             return True

#     def make_payment(self, amount):
#         if amount <= 0:
#             raise ValueError('Amount cannot be negative')
#         else:
#             self._balance -= amount 
    
# wallet = []

# wallet.append(CreditCard('Suraj', 'SBI', 'Savings', 1000, 2000))
# wallet.append(CreditCard('Vishakha', 'SBI', 'Savings', 2000))
# wallet.append(CreditCard('vish_kanya', 'SBI', 'Savings', 500))

# for val in range(5000, 8000):
#     wallet[0].charge(val)
#     wallet[1].charge(2*val)
#     wallet[2].charge(3*val)

# for c in range(3):

#     print('Customer = ', wallet[c].get_customer( ))
#     print('Bank = ', wallet[c].get_bank( ))
#     print('Account = ' , wallet[c].get_account( ))
#     print('Limit = ', wallet[c].get_limit( ))
#     print('Balance = ', wallet[c].get_balance( ))

#     while wallet[c].get_balance( ) > 100:
#         wallet[c].make_payment(100)
#         print('New balance = ', wallet[c].get_balance( ))


# Q9

# class Vector:

#     def __init__(self, d):
#         self._coords = [0] * d

#     def __len__(self):
#         return len(self._coords)

#     def __getitem__(self, j):
#         return self._coords[j]
    
#     def __setitem__(self, j, val):
#         self._coords[j] = val

#     def __sub__(self, other):
        
#         if len(self) != len(other):
#             raise ValueError('dimensions must agree ')

#         result = Vector(len(self))
#         # start with vector of zeros

#         for j in range(len(self)):
#             result[j] = self[j] - other[j]

#         return result

#     def __eq__ (self, other):
#         return self._coords == other._coords

#     def __ne__ (self, other):
#         return not self == other

# vector = Vector(2)
# vector1 = Vector(2)
# print(vector.__sub__(vector1))


# Q10

# class Vector:

#     def __init__(self, d):
#         self._coords = [0] * d

#     def __len__(self):
#         return len(self._coords)

#     def __getitem__(self, j):
#         return self._coords[j]
    
#     def __setitem__(self, j, val):
#         self._coords[j] = val

#     def __sub__(self, other):
        
#         if len(self) != len(other):
#             raise ValueError('dimensions must agree ')

#         result = Vector(len(self))
#         # start with vector of zeros

#         for j in range(len(self)):
#             result[j] = self[j] - other[j]

#         return result

#     def __neg__ (self, other):
#         return self._coords == other._coords

#     def __ne__ (self, other):
#         return not self == other

# vector = Vector(2)
# vector1 = Vector(2)
# print(vector.__sub__(vector1))
        # Not able to understand this time, to be continued later on......


# Continued from
# Q17

# class Goat(object):

#     def __init__(self, tail):
#         self._tail = tail

#     def milk(self):
#         pass

#     def jump(self):
#         pass


# class Pig(object):

#     def __init__(self, nose):
#         self._nose = nose
    
#     def eat(self, food):
#         pass

#     def wallow(self):
#         pass


# class Horse(object):

#     def __init__(self, height, color):
#         self._height = height
#         self._color = color

#     def run(self):
#         pass

#     def jump(self):
#         pass


# class Racer(Horse):

#     def __init__(self, height, color):
#         super().__init__(self, height, color)

#     def race(self):
#         pass

# class Equestrian(Horse):

#     def __init__(self, height, color, weight):
#         super().__init__(self, height, color)
#         self._weight = weight

#     def trot(self):
#         pass

#     def is_trainec(self):
#         pass


# Practice of HackerRank Questions :

# Count the number of distinct words from input and no. of occurences for each distinct word acc to their appereance in the input

# n = input("Enter the value of n ")

# for i in n:
#     counts = {}
#     print('counts', counts)
#     words = input("Enter word ").split()
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1 

# print('word',counts)


# Count the no. of matching pair of socks where n is the no of socks and ar[n] represents the total no of socks with different colors,
# each ar[i] pos represents sock of some color represented as numbers...

# import math
# import os
# import random
# import re
# import sys

# # Complete the sockMerchant function below.
# def sockMerchant(n, ar):
   
#     count = 0
#     ar.sort()
#     i = 0 
#     while i < (n-1):  
#         if (ar[i] == ar[i + 1]): 
#             count += 1 
  
#             # Skip the elements of  
#             # the current pair  
#             i = i + 2
  
#         # Current elements doesn't make  
#         # a valid pair with any other element  
#         else: 
#             i += 1  
  
#     return count  


# # fptr = open(os.environ['OUTPUT_PATH'], 'w')

# n = int(input())

# ar = list(map(int, input().rstrip().split()))

# result = sockMerchant(n, ar)
# print('result', result)

# # fptr.write(str(result) + '\n')

# # fptr.close()


# Counting valleys Problem:

# n = int(input())

# s = input()
# level = 0
# count = 0
# prev = 0

# for i in range(n):
#     if s[i] == 'U':
#         print('U above level',level)
#         level += 1
#         print('U below level', level)
#     elif s[i] == 'D':
#         print('D above level',level)
#         level -=1
#         print('D below level',level)
        

#     if level == 0 and prev < 0:
#         print('level', level, 'prev',prev)
#         count += 1
#     prev = level
#     print('level', level, 'prev',prev)


# print('count',count)


# Jumping on the clouds :

# c = list()
# n = input("Enter value of n: ")

# # input the clouds 
# for i in range(int(n)):
#     val = input("value: ")
#     c.append(int(val))

# print('clouds :', c)
# steps = 0
# i=0
# while i < int(n) - 1:
#     if c[i] == 0:
#         print('c[i]',c[i])
#         print('c[i+1]',c[i+1])
#         if (i+2) >= int(n) or c[i+2] == 1:
#             print('i', i)
#             i += 1
#             steps += 1
#             print('steps', steps)
#         else: 
#             i += 2
#             steps += 1
#             print('steps', steps)
        
# print('steps',steps)


# Repeated String :

# My Logic :

# s = input()

# n = int(input())

# len_of_s = len(s)
# new_s = ""
# count = 0

# while len(new_s) < n:
#     new_s = new_s + s
    

# print('new string', new_s)

# for i in range(n):
#     if new_s[i] == 'a':
#         count += 1

# print('count',count) 


# Logic from editorial :

# s = input()
# n = int(input())

# t=0
# print('t in starting', t)
# t=s.count('a')
# print('t counting a in s', t)
# t*=n//len(s)
# print('quotient',t)
# t+=s[0:n%len(s)].count('a')
# print('rem', t)
# print('t at last', t)

# Some more problems:

# Time execution of a code block using Class Based Context Manager

# import time

# class TimeExecution:
#         def __init__(self):
#                 self.start_time = 0
#                 self.end_time = 0

#         def __enter__(self):
#                 self.start_time = time.time()
#                 return self

#         def __exit__(self, exc_type, exc_val, exc_tb):
#                 self.end_time = time.time()        

#         def print(self):
#                 print("Time elapsed: ", self.end_time - self.start_time)

# with TimeExecution() as t:
#         ans = [x for x in range(1)]
#         t.print()
# print('ans1', ans)

# # Time execution of a code block using Function Based Context Manager

# from contextlib import contextmanager

# @contextmanager
# def  time_execution():
#         start_time = time.time()

#         yield 
#         ellapsed_time = time.time() - start_time
        
#         print('ellapsed time: ', ellapsed_time)

# with time_execution():
#         ans = [x for x in range(1)]

# print('ans2', ans)
        
#  Practice Python Programs from LinkedInLearning :

# Find prime factors of a number:

# def get_prime_factors(num):
#         factors = list()
#         divisor = 2
#         while (divisor <= num):
#                 if (num % divisor) == 0:
#                         factors.append(divisor)
#                         num = num/divisor
#                 else:
#                         divisor += 1
#         return factors


# num = int(input())
# prime_factors = get_prime_factors(num)
# print('prime factors list : ', prime_factors)


# Identify a palindrome:

# def is_pallindrome(phrase):
#         copy_phrase = phrase.lower()
#         reversed_phrase = copy_phrase[::-1]
#         if reversed_phrase == copy_phrase:
#                 return True
#         else:
#                 return False
        

# phrase = input()
# print(is_pallindrome(phrase))


# Sort a string:

# def sort_string(str_data):
#         str_list = str_data.split(' ')
#         print('after splitence :', str_list)
#         sorted_list = sorted(str_list, key = lambda s: s.lower())
#         print('sorted list : ', sorted_list)
#         return ' '.join(sorted_list)

# str_data = input()
# print('after sort :', sort_string(str_data))


# Find all list items:

# def find_index(input_data, item):
#         indices = list()
#         print('inside input :', input_data)
#         for i in range(len(input_data)):
#                 print('after cond')
#                 print('see this is our input data item ',input_data[i])
#                 print('if cond', input_data[i] == item)
#                 print('else cond', isinstance(input_data[i], list))
#                 if input_data[i] == item:
#                         indices.append([i])
#                         print('indices', indices)
                       
#                 elif isinstance(input_data[i], list):
#                         print('are we in else part ')
#                         for index in find_index(input_data[i], item):
#                                 print('inside loop', indices)
#                                 indices.append([i]+index)
#                                 print(' rec indices', indices)

#         return indices                
        


# # input_data = [(input_data) for input_data in input().split(",")]
# # print(input_data)
# input_data = [[1,2,1],2,[1,3],[1,2,3]]
# print('ip ', input_data)
# item = int(input())
# index_list = find_index(input_data, item)
# print('ans : ', index_list)


# Play the waiting game:



# Save a dictionary
# Set an alarm
# Send an email
# Simulate dice 
# Count unique words
# Generate a password 
# Merge CSV files
# Solve a sudoku
# Build a zip archive
# Download sequential files

# HackerEarth Questions Solved :

# 

# input_char = input()
# dna = 'GCTA'
# rna = 'CGAU'
# try:
#         print(''.join([rna[dna.index(i)] for i in input_char]))
# except:
#         print('Invalid Input')

# 

# A, B, C = input().split()
# A, B = B, A
# A = int(A) * int(C)
# B = int(B) + int(C)

# print(A, B)

#


# str_data = input()

# test_cases = int(input())

# for _ in range(test_cases):
#     x, y, a, b = input().split()
#     x = int(x)
#     y = int(y)
#     a = int(a)
#     b = int(b)

#     if x*y == a+b:
#         print('Yes')
#     else:
#         print('No')


# Evaluating expressions using eval like by providing "print(2 + 3)" as input 

# var = input()
# eval(var)

# Check in a list if all the elements are positive and any one of them is palindromic number

# n = int(input())
# # num_list = []

# # for i in range(0, n): 
# #     i = int(input())
# #     num_list.append(i)


# num_list = map(int, input().split())

# print('num list : ', num_list)

# # ans1 = all()
# # print('ans 1 ', ans1)

# # print('lambda : ', (lambda i: i>0)(1)) # returns True because 2>0 
# # print('map : ', [all(map(lambda i: i>0, num_list))])

# # print('lambda 2 : ', any(map(lambda i: str(i) == str(i)[::-1], num_list)))

# # print([False, True][False])

# print([False, any(map(lambda i: str(i) == str(i)[::-1], num_list))][all(map(lambda i: i>0, num_list))])


# Use of map and lambda function for finding cubes of fibonacci series

# a = 0
# b = 1
# n = 5
# nums = []


# for _ in range(n):
#     nums.append(a)

#     c = a + b
#     a = b
#     b = c
# print('nums : ',nums)

# print('lambda : ', list(map(lambda x: x**3, nums)))


# Exceptions :

# t = int(input())

# for _ in range(t):

#     try:
#         a, b = input().split()
    
#         try:
#             print(int(a)//int(b))
#         except ZeroDivisionError as e:
#             print('Error Code:', e)

#     except ValueError as v:
#         print('Error Code:', v)



# Validate mobile no. of 10 digits starting with 7, 8 or 9 using regex:

# import re

# N = int(input())

# for _ in range(N):
#     str = input()
#     match = re.search(r'^(7{1}|8{1}|9{1})(\d{9})$', str)
#     # If-statement after search() tests if it succeeded
#     if match:
#         print('YES')
#     else:
#         print('NO')
        

# Validate email address and print name and email in a pattern followed by email.utils :

# import re
# import email.utils

# regex = '^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$' 
# t = int(input())

# for _ in range(t):
#     # name, email1 = input().split()
#     value = input()

    
#     name, email1 = email.utils.parseaddr(value)
#     print('name email :', name, email1)
#     if(re.search(regex,email1)):
#         print(email.utils.formataddr((name, email1)))


# Symmetric Difference between two sets i.e those elements which are present in either of two sets but not in both.

# m_list = []
# n_list = []
# op_set = set()
# M = int(input())
# for _ in range(M):
#     m_list = list(map(int, input().split()))
#     print('inside ;', m_list)  

# # m_list = [int(x) for x in input().split()]

# N = int(input())
# for _ in range(N):
#     n_list = list(map(int, input().split()))
#     print('inside ;', n_list)  

# # N = int(input())
# # n_list = [int(y) for y in input().split()]

# line = set(m_list).difference(set(n_list))
# op_set.add(line)
# line = set(n_list).difference(set(m_list))
# op_set.add(line)

# # for _ in range(M):
# #     m_list = list(map(int, input().split()))
# #     print('inside ;', m_list)  

# # N = int(input())
# # for _ in range(N):
# #     N_line = input().split(' ')

# print('op :', m_list, n_list)

# m_set = set()
# n_set = set()
# op_set = set()

# m = int(input())

# m_set = map(int, input().split()[:m])
# print('inside ;', set(m_set))  

# print('space ')

# n = int(input())
# n_set = map(int, input().split()[:n])
# print('inside ;', set(n_set))

# print(set(m_set).difference(set(n_set)))

# print(set(n_set).difference(set(m_set)))


# print('ans', op_set)


# m = int(input())

# m_set = set(map(int, input().split()[:m]))

# print(m_set)

# n = int(input())

# n_set = set(map(int, input().split()[:n]))

# print(n_set)

# ans = list((m_set.difference(n_set)).union(n_set.difference(m_set)))

# print('\n'.join(map(str, sorted(ans))))
# # print("\n".join(map(str, (m_set.difference(n_set)).union(n_set.difference(m_set)))))


# Average score of students:

# # n = no. of students
# # x = no. of subjects
# n, x = map(int, input().split())
# # marks = [[0]*cols]*rows
# # print('marks ', marks)

# # val = int(input())
# # marks = [val*n]*x
# # print('marks ', marks)

# # marks = [[0 for i in range(n)] for j in range(x)]
# marks = []

# for _ in range(x):
#         marks += [map(float, input().split()[:n])]

# # print('m',marks)

# for stu_marks in zip(*marks):
#         print(sum(stu_marks)/x)



# Input Format :
# Given x, k and P such that if P(x)=k, print True else False.

# x, k = list(map(int, input().split()))
# p = input()

# if eval(p) == k:
#         print(True)
# else:
#         print(False)


# Check whether a number is a valid floaing point number or not :

# import re

# regex = r"^[+-]?\d*\.\d+$"
# n = int(input())
# for _ in range(n):
#         line = input()
#         if (re.search(regex, line)):
#                 print(True)
#         else:
#                 print(False)



# Regression Pattern 

# import re

# # regex = r"[,.]"

# # line = input()
# # print("\n".join(map(str, (re.split(', | . ', line)))))
# # ans = re.split(', | .', line)

# # [print(i) for i in re.split('[.,]', input()) if i]

# #

# regex_pattern = r"[,.]"	# Do not delete 'r'.

# print("\n".join(re.split(regex_pattern, input())))


# Find the first occurence of an alphanumeric charactrs from a given string :

# import re
# s = input()

# regex = r"([A-Za-z0-9])\1+"
# m = re.search(regex, s)

# if m:
#         print(m.group(1))
# else:
#         print('-1')

# Find the pattern having 2 or more vowels between 2 consonants and print the vowels :


# regex = r"([AEIOUaeiou][AEIOUaeiou]+)"
# regex = r"[^aiueo]([aiueoAIUEO]{2,})[^aiueo]"


# import re

# VOWELS = 'aeiou'
# CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
# REGEX = '(?<=[' + CONSONANTS + '])([' + VOWELS + ']{2,})[' + CONSONANTS + ']'

# match = re.findall(REGEX, input(), re.IGNORECASE)
# if match:
#     print(*match, sep='\n')
# else:
#     print('-1')


# Indices of the start and end of the substring matched by the group :

# import re
# S = input()
# k = input()
# anymatch = 'No'
# for m in re.finditer(r'(?=('+k+'))',S):
#     anymatch = 'Yes'
#     print((m.start(1),m.end(1)-1))
# if anymatch == 'No':
#     print((-1, -1))


# Validate Roman Numerals using Regular Exression :

# regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

# import re
# print(str(bool(re.match(regex_pattern, input()))))

# Two ways to write the same logic :

# counts = {'ans':'one', 'black':'two', 'panther':'three'}

# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# print(lst)

# print('next way')

# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )



# Hex Color Code :

# import re
# n = int(input())
# lines = ""

# for _ in range(n):
#     lines += input()
#     lines += '\n'

# print('op', lines)
# regex1 = r"\{.*?\}"
# regex2 = r"#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b"

# inside_brackets = re.findall(regex1, lines, re.DOTALL)
# print('i b ', inside_brackets)


# for prop in inside_brackets:
#     match = re.findall(regex2, prop)
#     if match:
#         print('\n'.join(match))
    
# Note: re.S or re.DOTALL matches any character including a newline


# HTML Parser - Part 1 :
# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print("Start :", tag)
#         if attrs:
#             # print("attrs", attrs, 'type', type(attrs))
#             for i in attrs:
#                 data, value = i
#                 print("->", data, ">", value)

#     def handle_endtag(self, tag):
#         print("End   :", tag)

#     def handle_startendtag(self, tag, attrs):
#         print("Empty :", tag)
#         if attrs:
#             # print("attrs", attrs, 'type', type(attrs))
#             for i in attrs:
#                 data, value = i
#                 print("->", data, ">", value)


# n = int(input())
# html_code = ''

# for _ in range(n):
#     html_code += input()
# # html_code = map(str, input().split()[:n])

# print('ans', html_code)

# parser = MyHTMLParser()
# parser.feed(html_code)
# parser.close()


# HTML Parser - Part 2 :

# class MyHTMLParser(HTMLParser):

#     def handle_data(self, data):
#         if data.strip():
#             print(">>> Data")
#             print(data)

#     def handle_comment(self, data):
#         no_of_lines = len(data.split('\n'))
#         # print('inside comment1 ', no_of_lines)
#         if no_of_lines > 1:
#             print(">>> Multi-line Comment")
#         else:
#             print(">>> Single-line Comment")
#         if data.strip():
#             print(data)
            

# n = int(input())
# html_code = ''

# for _ in range(n):
#     html_code += input()+"\n"


# print('ans', html_code)

# parser = MyHTMLParser()
# parser.feed(html_code)
# parser.close()


# Detect HTML Tags, Attributes and Attribute Values :

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         if attrs:
#             for i in attrs:
#                 data, value = i
#                 print("->", data, ">", value)

#     def handle_startendtag(self, tag, attrs):
#         print(tag)
#         if attrs:
#             for i in attrs:
#                 data, value = i
#                 print("->", data, ">", value)

      
# n = int(input())
# html_code = ''

# for _ in range(n):
#     html_code += input()+"\n"

# parser = MyHTMLParser()
# parser.feed(html_code)
# parser.close()




# Validating UID :

# import re
# for _ in range(int(input())):
#     s = input()
#     result = (len(set(re.findall(r'[a-zA-Z0-9]', s))) == 10 and
#               len(re.findall(r'[A-Z]', s)) > 1 and
#               len(re.findall(r'[0-9]', s)) > 2)
#     print('res', result)
#     print('Valid' if result else 'Invalid')


# XML 1 - Find the score :

# import sys
# import xml.etree.ElementTree as etree

# def get_attr_number(node):
#     count = len(node.attrib)
#     for child in node:
#         count += get_attr_number(child)
#     return count
    
# # if __name__ == '__main__':
# # sys.stdin.readline()
# # print('readline')
# n = int(input())

# xml = ''
# for _ in range(n):
#     xml += input() + '\n'
# print('xml', xml)

# tree = etree.ElementTree(etree.fromstring(xml))
# print('tree', tree)
# root = tree.getroot()
# print('root', root)
# print(get_attr_number(root))


# Validating Credit Card Numbers :

# import re

# cons = re.compile(r"(\d)(\1){3}")
# # print('cons', cons)
# f = re.compile(r"\d{4}\-?\d{4}\-?\d{4}\-?\d{4}")

# n = int(input())

# for _ in range(n):
#     s = input()
    
#     # print('ans', bool(re.findall(r"^4|^5|^6", s)))
#     # print('ans1', re.findall(r"([0-9]-[0-9]){4}", s))
#     # print('ans2', len(re.findall(r"[0-9]", s)) == 16) 

#     if len(s) != 16 and len(s) != 19:
#         print("Invalid")
#         continue
#     if s[0] not in "456":
#         print("Invalid")
#         continue
#     if not f.match(s):
#         print("Invalid")
#         continue

#     s = s.replace("-", "")

#     if cons.search(s):
#         print("Invalid")
#         continue 

#     print("Valid")   


# XML2 - Find the Maximum Depth :

# import xml.etree.ElementTree as etree

# maxdepth = 0
# def depth(elem, level):
#     global maxdepth
#     level += 1
#     if (maxdepth < level):
#         maxdepth = level
#     for child in elem:
#         depth(child, level)

# # if __name__ == '__main__':
# n = int(input())
# xml = ""
# for i in range(n):
#         xml =  xml + input() + "\n"
# print('xml ', xml)
# tree = etree.ElementTree(etree.fromstring(xml))
# depth(tree.getroot(), -1)
# print(maxdepth)


# Standarize Mobile Number Using Decoators :

# def standerize(f):
#         print('args', f)
#         def fun(mob_num):
#                 print('mob num dec', mob_num)
#                 # mob_num = [n[-10:] for n in mob_num]
#                 mob_num = ["+91 %s %s" %(n[-10:-5],n[-5:]) for n in f(mob_num)]
#                 print('now mob', mob_num)
#                 return mob_num
#         return fun

# @standerize
# def sort_nums(mob_num):
#        return sorted(mob_num)

# n = int(input())

# mob_num = []
# for _ in range(n):
#         mob_num.append(input())

# print('mob ', mob_num)
# for num in sort_nums(mob_num):
#         print(num)

#    ---XXX---OR---XXX---

# def wrapper(f):
#     def fun(l):
#         f(["+91 "+i[-10:-5]+" "+i[-5:] for i in l])
#     return fun
    
# @wrapper
# def sort_phone(l):
#     print('inside sort l', l)
#     print(*sorted(l), sep='\n')

# l = [input() for _ in range(int(input()))]
# print('l outside',l)
# sort_phone(l)
 

# Decorators 2 - Name Directory :

# n = int(input())

# values = []
# line = []
# # for _ in range(n):
# #         values.append(input())
# for _ in range(n):
#         line = list(map(str, input().split()))
#         values.append(line)

# print('ans', values)

# from operator import itemgetter

# values.sort(key=itemgetter(2))
# print('after sort ', values)

# ans_list = []

# from itertools import groupby
# for elt, items in groupby(values, itemgetter(2)):
#         for i in items:
#                 if i[3] == 'M':
#                         print("Mr.", i[0], i[1])
#                 else:
#                         print("Ms.", i[0], i[1])

# or

# import operator

# def person_lister(f):
#     def inner(people):
#         print('in', people)
#         return map(f, sorted(people, key=lambda x: int(x[2])))      
#     return inner

# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# # if __name__ == '__main__':
# people = [input().split() for i in range(int(input()))]
# print(*name_format(people), sep='\n')


# Arrays :

# n, m = input().split()

# array = []
# for _ in range(int(n)):
#         array.append(list(map(int, input().split())))

# print(array)

# n = tuple(map(int, input().split()))
# print('n', n)

# This gives the output as n (3, 3, 3) if input = 3 3 3
# or output as n (2, 3) if input = 2 3



# n, m = input().split()

# A = []
# B = []
# for _ in range(int(n)):
#         A.append(list(map(int, input().split()[:int(m)])))
# for _ in range(int(n)):
#         B.append(list(map(int, input().split()[:int(m)])))

# print('a', A, 'b', B)


# The Collatz Sequence :

# def collatz(number):
#     if number % 2 == 0:
#         ans = number // 2
#         print(ans)
#         return ans
#     else:
#         ans = 3 * number + 1
#         print(ans)
#         return ans 

# while True:
#     try:
#         number = int(input())
#         ans = collatz(number)
#         if ans == 1:
#             break
#     except:
#         print("Only Integer value allowed")


# Comma Code :

# def comma_code(spam):
#     line = ''
#     for i in range(len(spam) - 1):
#         line += spam[i]
#         line += ', '
#     line += 'and ' + spam[(len(spam) - 1)]
#     return line 

# spam = []

# n = int(input())

# for _ in range(n):
#     spam.append(input())

# print('ans', spam)

# ans = comma_code(spam)
# print('result', ans)


# Character Picture Grid :

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', '0', '0', '.', '.', '.'],
#         ['0', '0', '0', '0', '.', '.'],
#         ['0', '0', '0', '0', '0', '.'],
#         ['.', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '.'],
#         ['0', '0', '0', '0', '.', '.'],
#         ['.', '0', '0', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# for j in range(6):
#     for i in range(9):
#         print(grid[i][j], end='')
#     print()


# Tic-tac-toe :

# the_board = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
#             'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
#             'low_L': ' ', 'low_M': ' ', 'low_R': ' '}

# def print_board(board):
#     print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
#     print('-+-+-')
#     print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
#     print('-+-+-')
#     print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])
    
# turn = 'X'
# for i in range(9):
#     print_board(the_board)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     the_board[move] = turn
#     if turn == 'X':
#         turn = '0'
#     else:
#         turn = 'X'
# print_board(the_board)

# Fantasy Game Inventory :

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in sorted(inventory.items()):
#         # FILL THIS PART IN
#         print(str(v) + " " + k)
#         item_total = item_total + inventory.get(k, 0)
#     print("Total number of items: " + str(item_total))

# displayInventory(stuff)

# def addToInventory(inventory, addedItems):

#     for i in addedItems:
#         inventory.setdefault(i, 0)
#         inventory[i] = inventory[i] + 1
#     return inventory
    

# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# print('in inv', inv)
# displayInventory(inv)


# Table Printer :

# def printTable(table):
#     max_len = 0
#     col_widths = [0] * len(table)
#     print('col widths ', col_widths) 
#     i = 0
#     for i, row in enumerate(table):
#         print(row)
#         max_len = len(row[0])
        
#         # for col in row and (i in range(len(row))):
#         for col in row:
            
#             if len(col) > max_len:
#                 max_len = len(col)
#             print('max len inside ', max_len)
#         print('max len outside ', max_len)

#         col_widths[i] = max_len
        
        
        
#         # print(str(row).rjust(col_widths[i]))
#         print('col width inside ', col_widths, 'i ', i)
        
    
#     print('col widths after', col_widths)

#     print('ans')
#     j = 0
 
#     for k in range(4):
#         for j in range(len(table)):
            
#             # print('j', j, k, k)
            
#             print(str(table[j][k]).rjust(8), end=' ')           
#         print(end='\n')
        
    

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# ['Alice', 'Bob', 'Carol', 'David'],
# ['dogs', 'cats', 'moose', 'goose']]

# printTable(tableData)


# Strong Password Detection :

# import re

# def check_strength(password):
#     regex = '''
#         ([a-zA-Z@%&]{8,})    # any 8 characters
#         ([0-9]{1,})          # atleast 1 digit
#     '''
#     match = re.search(regex, password, re.I | re.VERBOSE)
#     return match

# while True:
#     password = input("Enter password : ")
#     valid = check_strength(password)
#     if valid:
#         print('Great, Password is strong !!!')
#         break
#     else:
#         print('Password is weak, please set another password.')


# Regex Version of strip() :

# import re 

# def regex_strip(line, pos='both'):
#     match = ''
#     print('line', line)
#     if pos == 'right':
#         regex = re.compile(r'(\w*\s*\w*)*\S+', re.I)
#         print('regex ', regex)
#     elif pos == 'left':
#         regex = re.compile(r'\S+(\w*\s*\w*)*', re.I)
#         print('regex ', regex)
#     else:
#         regex = re.compile(r'\S+(\w*\s*\w*)*\S+', re.I)
#         print('regex ', regex)
#     match = regex.search(line)
#     print('match ', match)
#     print(' match gp ', match.group())
#     return match


# print(input('Trial string').strip())
# line = input("Enter the string : ")
# print('line out ', line)
# pos = input("Enter the postion : ")
# print('pos out ', pos)
# stripped = regex_strip(line, pos)
# print('stripped out ', stripped)
# print('ans', stripped.group())


# Building a multiple choice quiz :

# class Question:

#     def __init__(self, prompt, answer):
#         self.prompt = prompt
#         self.answer = answer

# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Oramge\n\n",
#     "What color are bananas?\n(a) Pink\n(b) Yellow\n(c) Blue\n\n"

# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "b"),
# ]

# def run_tests(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got "+ str(score) + "/" + str(len(questions)) + " correct")


# run_tests(questions)


# Mad Libs :
# import os, re

# my_path = "/home/vishakha/Documents/Practice/LearningProgramming/"

# my_words = [
#     # {
#     #     "ADJECTIVE": "", 
#     #     "ADVERB": "", 
#     #     "NOUN": "", 
#     #     "VERB": ""
#     # }
# ]

# if os.path.exists(my_path):
#     with open(my_path+"sample.txt") as f1:
#         lines = list(line.strip() for line in f1)

#         f_list = []
#         t_list = ''
        
#         for line in lines:
#             print('word', line)
#             # print('word i', word.split())
#             # for i in word.split() if i.isalpha() else " ":
#             splited = re.split(r'\s|\.', line)
#             print('ans of split', splited)
#             for i in splited:
#                 if i in ["ADJECTIVE", "ADVERB", "NOUN", "VERB"]:
#                     # print("Enter a/an %s: " % i)
#                     print("Enter a/an",  f"{i}", ": ")
#                     t_list += (str(splited).replace(f"{i}", input()))
#                     print('t list', t_list)
#                     val = t_list.split()
#                     print('val', val)    
#                     # my_words.append(input())
            
#         # print('last ', my_words)
#         # for line in lines:
#         #     print('in second line', line)
#         #     splited = re.split(r'\s|\.', line)
#         #     print('ans of split', splited)
#         #     for i in splited:
#         #         if i in ["ADJECTIVE", "ADVERB", "NOUN", "VERB"]:
#         #             splited.replace(i, my_words)
#         with open(my_path+"new_sample.txt", 'w') as f2:
#             f2.write(line)

# else:
#     print('No such path exists')


# Walking a directory tree - os.walk() :
# import os

# for foldername, subfolders, filenames in os.walk('/home/vishakha/Documents/Practice/LearningProgramming'):
#     print('The current folder is ' + foldername)

#     for subfolder in subfolders:
#         print('Subfolder of '+ foldername + ': ' + subfolder)

#     for filename in filenames:
#         print('File inside '+ foldername + ': '+ filename)

#     print('')

##

#!/usr/bin/python

# def displayPathtoPrincess(n,grid):
#     #print all the moves here
#     print("DOWN")
#     print("LEFT")
    
# m = int(input())
# grid = [] 
# for i in range(0, m): 
#     grid.append(input().strip())

# displayPathtoPrincess(m,grid)


# Regex Search :
# import re,os

# pattern = re.compile(r"\w*")

# for data in os.listdir('.'):
#     if data.endswith('.txt'):
#         with open(data) as obj:
#             line = obj.read()
#             mo = pattern.search(line)
#             if mo == None:
#                 continue

#         print('mo is ', mo.group())


# Selective Copy :
# import os, shutil

# for foldername, subfolders, filenames in os.walk('/home/vishakha/Documents/Practice/LearningProgramming/Example/exp1'):

#     print('current folder', foldername)
#     for filename in filenames:
#         # print('1 file name', filename)
#         # if filename.endswith(tuple(['.txt', ''])):
#         if filename.endswith('.pdf'):
#             print('filename', filename)
#             result = shutil.copy(filename, '/home/vishakha/Documents/Practice/LearningProgramming/Example/exp2')
#             print('result ', result)
#         print('i m out ')

# Deleting unneeded files :

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')

# for foldername, subfolders, filenames in os.walk('/home/vishakha/Documents/Practice/LearningProgramming'):
#     print('current folder', foldername)

#     for filename in filenames:
#         try:
#             size = os.path.getsize(filename)
#             print('size of file', filename, size)
#             if size > 100:
#                 print('The file with more than 100 MB of size are ', filename)
#         except FileNotFoundError:
#             print('File not found')

# logging.debug('End of program')


# Debugging Coin Toss :

# import random

# guess = ''

# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()

# toss = random.choice(['heads', 'tails'])
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')


import webbrowser, sys
# Launch webbrowser by giving address using command line :

# address = ''
# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])

# webbrowser.open('https://www.google.com/'+ address)

# Open all links on a page in separate browser tabs :

# link1 = 'https://facebook.com/'
# link2 = 'https://gmail.com/'
# link3 = 'https://python.org/'

# webbrowser.open_new_tab(link1)
# webbrowser.open_new_tab(link2)
# webbrowser.open_new_tab(link3)


# Downloading a web page with the requests.get() :

# import requests, bs4

# res = requests.get('http://nostarch.com')
# try:

#     print('result', res.raise_for_status())
#     print('type of res',type(res))
#     print('req code', requests.codes.ok)

#     if res.status_code == requests.codes.ok:
#         print('res status code')

# except Exception as e:
#     print('Some problem existed: %s' %(e))
# print('len of res text', len(res.text))
# print('res text char', res.text[:250])

# writing the data downloading from web page to a file on hard drive:
# my_file = open('temp_file.html', 'wb')
# for chunk in res.iter_content(100000):
#     my_file.write(chunk)
# my_file.close()

# using beautiful soup library:

# soup_obj = bs4.BeautifulSoup(res.text)
# print('bs4 obj type', type(soup_obj))
# elems = soup_obj.select('#main-content')
# print('elems', elems, 'type', type(elems), 'len of elems', len(elems))
# print('type of elems at 0', type(elems[0]))
# print('text at index 0', elems[0].getText())
# print('str version of elems at 0', str(elems[0]))
# print('attrs of elems at 0', elems[0].attrs)

# pull elements of <p> tag using beautiful soup library:

# p_elems = soup_obj.select('p')
# print('elems at 0', str(p_elems[0]))
# print('get text', p_elems[0].getText())
# print('elems at 1', str(p_elems[1]))
# print('get text', p_elems[1].getText())
# print('elems at 2', str(p_elems[2]))
# print('get text', p_elems[2].getText())

# Getting data from an element's attributes:

# span_elem = soup_obj.select('span')[0]
# print('str of span elem', str(span_elem)) 
# print('get id', span_elem.get('id'))
# print('get class', span_elem.get('class'))
# print('attrs', span_elem.attrs)


# Google Search Project :

# import requests, sys, webbrowser, bs4

# # Opens several Google search results.
# print('Googling.....') # display tet while downloading the Google page
# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
# print('res', res)
# res.raise_for_status()

# # Retrieve top search result links.
# soup = bs4.BeautifulSoup(res.text)
# # print('soup', soup)

# # # Open a browser tab for each result.
# link_elems = soup.select('a')
# print('link elems', link_elems)
# num_open = min(5, len(link_elems))
# print('num open', num_open)
# for i in range(num_open):
#     webbrowser.open('http://google.com' + link_elems[i].get('href'))
# print('exit')


# Working with PDFs :

import PyPDF2

# pdf_obj = open('Example/PDF_Program/sample.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
# print('is pdf enctrypted', pdf_reader.isEncrypted)
# print('no of pages in pdf', pdf_reader.numPages)
# page_obj = pdf_reader.getPage(0)
# print('page obj', page_obj)
# print('see text', page_obj.extractText())

# Copying pages

# pdf1 = open('sample.pdf', 'rb')
# pdf2 = open('dummy.pdf', 'rb')

# pdf_reader1 = PyPDF2.PdfFileReader(pdf1)
# pdf_reader2 = PyPDF2.PdfFileReader(pdf2)

# pdf_writer = PyPDF2.PdfFileWriter()

# for p_num in range(pdf_reader1.numPages):
#     page_obj = pdf_reader1.getPage(p_num)
#     pdf_writer.addPage(page_obj)

# for p_num in range(pdf_reader2.numPages):
#     page_obj = pdf_reader2.getPage(p_num)
#     pdf_writer.addPage(page_obj)

# pdf_output_file = open('Example/PDF_Program/combined.pdf', 'wb')
# pdf_writer.write(pdf_output_file)

# pdf_output_file.close()
# pdf1.close()
# pdf2.close()

# Rotating pages :

# file_obj = open('Example/PDF_Program/sample.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(file_obj)
# # page = pdf_reader.getPage(0)
# # page.rotateClockwise(90)

# pdf_writer = PyPDF2.PdfFileWriter()
# # pdf_writer.addPage(page)
# # result_pdf = open('Example/PDF_Program/rotated.pdf', 'wb')
# # pdf_writer.write(result_pdf)

# # result_pdf.close()
# # file_obj.close()

# # Encrypting PDFs :

# for p_num in range(pdf_reader.numPages):
#     pdf_writer.addPage(pdf_reader.getPage(p_num))

# pdf_writer.encrypt('swordfish')
# result_pdf = open('Example/PDF_Program/encrypted.pdf', 'wb')
# pdf_writer.write(result_pdf)

# result_pdf.close()
# file_obj.close()


# PDF Paranoia :

import os

# For encrypting pdf's
# for foldername, subfolders, filenames in os.walk('Example/PDF_Program/'):

#     print('current folder', foldername)
#     for filename in filenames:
#         if filename.endswith('.pdf'):
#             print('I m in right place')
#             print('filename', filename)
            
#             file_obj = open(foldername+'/'+filename, 'rb')
#             pdf_reader = PyPDF2.PdfFileReader(file_obj)
#             print('pdf reader', pdf_reader.numPages)

#             pdf_writer = PyPDF2.PdfFileWriter()
 
#             for p_num in range(pdf_reader.numPages):
#                 pdf_writer.addPage(pdf_reader.getPage(p_num))


#             pdf_writer.encrypt('ABASE')

#             file_name = os.path.splitext(filename)[0]
#             result_pdf = open(foldername+'/'+file_name+'_encrypted.pdf', 'wb')
#             pdf_writer.write(result_pdf)

#             file_obj.close()
#             result_pdf.close()
            
# For decrypting encrypted pdf's
# for foldername, subfolders, filenames in os.walk('Example/PDF_Program/'):

#     print('current folder', foldername)
#     for filename in filenames:
#         if filename.endswith('_encrypted.pdf'):
#             file_obj = open(foldername+'/'+filename, 'rb')
#             pdf_reader = PyPDF2.PdfFileReader(file_obj)
            
#             if pdf_reader.isEncrypted:
#                 print('File is encrypted, please provide password to decrypt it...')
#                 password = input()
#                 ans = pdf_reader.decrypt(password)
#                 if ans:
#                     print('File decrypted successfully')

#                     pdf_writer = PyPDF2.PdfFileWriter()
 
#                     for p_num in range(pdf_reader.numPages):
#                         pdf_writer.addPage(pdf_reader.getPage(p_num))

                    
#                     file_name = os.path.splitext(filename)[0]
#                     name = file_name.split('_')[0]
#                     result_pdf = open(foldername+'/'+name+'_decrypted.pdf', 'wb')
#                     pdf_writer.write(result_pdf)

#                     file_obj.close()
#                     result_pdf.close()
                    
#                 else:
#                     print('File cannot be decrypted, u provided wrong password.')


# Brute Force PDF Password Breaker :

# words = []

# def file_to_list():
#     with open('Example/PDF_Program/BruteForcePasswordBreaker/dictionary.txt') as fh:
#         line = fh.read()

#         # line = 'HAIR IS DRY'
#         words = line.split() 
#         words.extend(line.lower().split())
#         # print('new words', words)
#     return words

# for foldername, subfolders, filenames in os.walk('Example/PDF_Program/'):

#     print('current folder', foldername)
#     for filename in filenames:
#         if filename.endswith('_encrypted.pdf'):
#             file_obj = open(foldername+'/'+filename, 'rb')
#             pdf_reader = PyPDF2.PdfFileReader(file_obj)
            
#             if pdf_reader.isEncrypted:
#                 words = file_to_list()
#                 for i in words:
#                     password = i
#                     print('pass', password)
#                     ans = pdf_reader.decrypt(password)
#                     print('ans', ans)
#                     if ans == 1:
#                         print('Hacked Password is:', password)
#                         break
#                     else:
#                         pass
                

# CSV Module :

import csv 

# Reader Objects
# example_file = open('Example/example.csv')
# reader = csv.reader(example_file)

# getting all data in a list
# data = list(reader)
# print('data', data)
                
# reading data from reader objects in a for loop 
# for row in reader:
#     print('Row no.' + str(reader.line_num) + ' ' + str(row))

# Writer Objects
# output_file = open('Example/output.csv', 'w')
# writer = csv.writer(output_file)
# writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
# writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# writer.writerow([1, 2, 3.141592, 4])

# output_file.close()


# JSON Module :

import json

# Reading JSON data
# string_of_json_data = '{ "name": "Zophie", "is_cat": true, "mice_caught": 0, "feline_IQ": null }'

# data = json.loads(string_of_json_data)
# print('JSON data as Python value :', data)

# Writing JSON data
# python_value = {
#     'is_cat': True,
#     'mice_caught': 0,
#     'name': 'Zophie',
#     'feline_IQ': None
# }

# data = json.dumps(python_value)
# print('String of JSON data :', data)


# Pretified Stopwatch Program :

# import time

# # Display the program's instructions
# print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
# input()    # Press Enter to begin
# print('Started.')

# start_time = time.time() # get the first lap's start time
# last_time = start_time
# lap_num = 1

# # Start tracking the lap times
# try:
#         while True:
#                 input()
#                 lap_time = round(time.time() - last_time, 2)
#                 total_time = round(time.time() - start_time, 2)
#                 print('Lap #%s: %s (%s)' % (str(lap_num).rjust(2), str(total_time).rjust(6), str(lap_time).rjust(6)), end='')
#                 lap_num += 1
#                 last_time = time.time()  # reset the last lap time
# except KeyboardInterrupt:
#         print('\nDone.')

# TODO
# Random Chore Assignment Emailer :

# import random, smtplib

# emails = ['vishakhabhat1995@gmail.com', 'vish12495@gmail.com']
# chores = ['dishes', 'bathroom']

# smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_obj.ehlo()
# smtp_obj.starttls()
# password = input('Enter your password')
# smtp_obj.login('vishakhabhat93@rediffmail.com', password)

# for i in emails:
#         random_chore = random.choice(chores)
#         smtp_obj.sendmail(i, 'Subject: This is the task assigned to you...', 'Task'+ random_chore)

# smtp_obj.quit()