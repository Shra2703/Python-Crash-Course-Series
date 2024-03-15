# Day 2(05-03-2024)
# operators, modules and pip, strings, user input

# modules are the fuctions which is the written by someone and that code we can use when we import it through pip.
import pandas  as pd # pandas module

num1 = 5
num2 = 10

# arithmetic
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)

# asignment 
a = 8
print(a)
a += 2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)

# comparison
print(num1 > num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)

# logical operator
print(num1 == num2 and num2 > num1)
print(num1 == num2 or num2 > num1)
print(not(False))

# Strings are imutable
# both are valid syntax
name = "Shraddha" #1
print(name)
name1 = 'vaibhav' #2
print(name1)
name3 = '''Aditya is the good boy''' #4
print(name3) 

# slicing
print(name[0:4])
print(name[3:4])

# inbuilt methods
print("Inbuit methods")
print(name.upper())
print(name.capitalize())
print(name.count('a'))
print(name.index('S'))

# user input (by default taking input in strings)
name2 = input("Enter your name: ")
print(name)
num =  input("Enter num: ")
print(num)
print(type(num))

# typcasting it
print(int(num) + 9)