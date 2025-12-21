# city = input("In which city you grow!\n")
# pet = input("What is your pet name!\n")
# print("Your brand name is "+ city + " "+pet)

# print(int('12')+int('22'))
# print("Number of letters in your name: "+ str(len(input("Enter your name"))))

# print('Welocme to the tip calculator!')
# total_bill = float(input('What was the total bill?'))
# tip = float(input('How much tip would you like to give?'))
# split = float(input('How many people to split the bill?'))
# split_amt = round((total_bill+tip)/split,2)
# # print(type(total_bill),type(tip),type(split))
# print(f"Each person should pay: ${split_amt}")
#
# a = int(input('Give me a number to check.'))
# if a%2 == 0:
#     print(f'{a} is a even number!')
# else:
#     print(f'{a} is odd number!')


# h = int(input('What is your height?'))
# bill = 0
# if h >= 175:
#     print('You are eligible')
#     a = int(input('what is your age?'))
#     if a>=18:
#         print('Your ticket price is $12')
#         bill = 12
#     elif a>=12 and a<= 18:
#         print('Your ticket price is $7')
#         bill = 7
#     else:
#         print('Your ticket price is $5')
#         bill = 5
#     photo = input('If you want photo enter y else n')
#     if photo == 'y':
#         bill+=3
#         print(f'your bill is {bill}')
#     else:
#         print(f'your bill is {bill}')
# else:
#     print('You can\'t ride' )




#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
#
# # 1. Handle Base Price
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# elif size == 'L':
#     bill += 25
#
# # 2. Handle Pepperoni (Depends on size)
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         # Both M and L cost $3, so we can group them
#         bill += 3
#
# # 3. Handle Cheese (Independent of size)
# if extra_cheese == 'Y':
#     bill += 1
#
# # 4. Single Output
# print(f"Your final bill is ${bill}")


import  art
print(art.treasure_logo_1)

"""
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?
Type "left" or "right"
left
You've come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There is a house with 3 doors.
One One red one yellow and one blue. Which colour do you choose?
2x 1:23/21
"""



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

# Cleaned up input line
l_r = input("Type 'left' or 'right': ".center(40, " ")).lower()

if l_r == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")

    s_w = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

    if s_w == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()

        if door == 'yellow':
            print('You found the treasure! You Win!')
        elif door == 'red':
            print("Burned by fire.\n" + "Game Over.".center(20))
        elif door == 'blue':
            print("Eaten by beasts.\n" + "Game Over.".center(20))
        else:
            print("Game Over.".center(20))

    else:
        print("Attacked by trout.\n" + "Game Over.".center(20))
else:
    print("Fall into a hole.\n" + "Game Over.".center(20))





























