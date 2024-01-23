# list=[1,2,4,4,5,8]
# print(max(list))
# print(min(list))
# print(set(list))


thisdic = (
    "brand": "koeniggsegg",
    "Model": "Jesko",
    "year": "2024"
)

print(thisdic["brand"])
# import random

# user_action = input("Enter a choice (rock, paper, scissors); ")
# possible_actions = ["rock", "paper", "scrissors"]
# computer_action = random.choice(possible_actions)

# print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# if user_action == computer_action:
#     print("It's a tie!")
# elif (
#     (user_action == "rock" and computer_action == "scissors") or
#     (user_action == "paper" and computer_action == "rock") or
#     (user_action == "scissors" and computer_action == "paper")
# ):
#     print("You win!")
# else:
#     print("Computer wins!")

# def And(input1, input2):
#     # Using if statement for AND operation
#     if input1 == 1 and input2 == 1:
#         output = 1
#     else:
#         output = 0
#     return output

# # Example usage
# input1 = int(input("Enter the first input (0 or 1): "))
# input2 = int(input("Enter the second input (0 or 1): "))

# if input1 not in [0, 1] or input2 not in [0, 1]:
#     print("Invalid input. Please enter 0 or 1 for inputs.")
# else:
#     result = And(input1, input2)
#     print(f"The result of the AND gate for inputs {input1} and {input2} is: {result}")

# def OR(input1, input2):
#     if input1 == 0 and input2 == 0:
#         output = 0
#     else:
#         output = 1
#     return output

# input1 = int(input("Enter the first input (0 or 1): "))
# input2 = int(input("Enter the second input (0 or 1): "))

# if input1 not in [0, 1] or input2 not in [0, 1]:
#     print("Invalid input. Please enter 0 or 1 for inputs.")
# else:
#     result = OR(input1, input2)
#     print(f"The result of the Or gate for inputs {input1} and {input2} is: {result}")

# def Not(input1):
#     if input1 == 1:
#             output = 0
#     if input1 == 2:
#         output = 1
#     return output

# input1 = int(input("Enter your input (0 or 1): "))

# if input1 not in [0, 1]:
#     print("Invalid input. Please enter 0 or 1 for inputs.")
# else:
#     result = Not(input1)
#     print(f"The result of the Not gate for your input {input1} is: {result}")
