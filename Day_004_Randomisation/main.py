import random

# Heads/Tails
# random_num = random.randint(0,1)
# if random_num == 0:
#     print('Heads')
# else:
#     print('Tails')

# Random pick
# # 1st option
# friends = ["Alice", "Bob", "Charlie", "David","Emanuel"]
# r = random.randint(0,(len(friends)-1))
# print(friends[r])
#
# # 2nd option
# print(random.choice(friends))
#
# # 3rd option
# random.shuffle(friends)
# print(friends[0])

# Rock, Paper and Scissor Game
import random
import art

# 1. Get Input
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# 2. Check for invalid numbers FIRST (Before accessing the list)
if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
else:
    # Only run the game logic if the number is valid
    game_images = [art.rock, art.paper, art.scissors]

    # Generate computer choice
    computer_choice = random.randint(0, 2)

    print(f"You chose:\n{game_images[choice]}")
    print(f"Computer chose:\n{game_images[computer_choice]}")

    # 3. Game Logic
    if choice == computer_choice:
        print("It's a draw")
    elif (choice == 0 and computer_choice == 2) or \
            (choice == 1 and computer_choice == 0) or \
            (choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        # No need to write out the losing conditions
        print("You lose")