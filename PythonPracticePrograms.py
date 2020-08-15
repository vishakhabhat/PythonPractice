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

import re

# regex = r"[,.]"

# line = input()
# print("\n".join(map(str, (re.split(', | . ', line)))))
# ans = re.split(', | .', line)

# [print(i) for i in re.split('[.,]', input()) if i]

#

regex_pattern = r"[,.]"	# Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))