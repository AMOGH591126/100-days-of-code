# fruits = ['Apple','Peach','Pear']
# for fruit in fruits:
#     print(fruit)
from typing import List, Any

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 200, -1, -29]

# task 1:- Sum
# total_score = sum(student_scores)
# total_score = 0
# for score in student_scores:
#     total_score += score
# print(total_score)

# task 2:- Max
# maximum = max(student_scores)
# maximum = student_scores[0]
# for num in student_scores:
#     if num > maximum:
#         maximum = num
# print(maximum)

# task 3:- Min
# minimum = min(student_scores)
# minimum = student_scores[0]
# for num in student_scores:
#     if num < minimum:
#         minimum = num
# print(minimum)

# RANGE Function

# task 1 sum the numbers from 1 to 100
# total = 0
# for num in range(1,101):
#     total += num
# print(total)

# task 2 FizzBuzz challenge
# for i in range(1,101):
#     if i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')
#     elif i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# task 3 Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Since you never actually use the variable i inside the loop (you just need the loop to run X times),
# Python developers often use an underscore _ instead.
# This tells other programmers: "I don't care about this variable, I just need to loop."

password = ''
for _ in range(0, nr_letters):
    password += random.choice(letters)
for _ in range(0, nr_symbols):
    password += random.choice(symbols)
for _ in range(0, nr_numbers):
    password += random.choice(numbers)
password = "".join(random.sample(password, len(password)))
print(password)
