# to convert float to whole number
# import math
# apply math method to code what to use it on
import math
# color green is a good sign - it means the import is successful
# white dashed line under math means it has not yet been used

# commenting out previous code to avoid having to go through each input to get to the current exercise

# # for loop
# for name in ["Max", "Al", "Jenn", "Stella", "Nate", "Cynt", "John", "Zell", "Sam"]:
#     print("Good Code Day, " + name + "!")

# # FOR LOOP = fixed amount of iterations
# # WHILE LOOP = nonfixed iterations AND when output depends on user input

# # while loop
# more_people = input("\nWho else? y or n ")

# more_people = more_people.lower()
# while (more_people == "y"):
#     name = input("Name? ")
#     print("Hey " + name + "!")
#     # more_people = input("Name? ")
#     # more_people = more_people.lower()
#     print("Have a code-filled great day!")

# # the bug here is that it is still reading for a new input
# # when a name is entered
# # that's what we told it to do
# # it is a while loop
# # while it is true, which it is now, it will always continue to accept input....


# # basic python input
# num1 = int(input("\nEnter num1: "))
# num2 = int(input("Enter num2: "))
# sum = num1 + num2
# print(sum)

# num0 = int(input("\nEnter num0: "))
# num00 = int(input("Enter num00: "))
# product = num0 * num00
# print(product)

# num3 = int(input("\nEnter a number: "))
# num5 = int(input("Enter another number: "))
# divisor = num3 / num5
# print(divisor)

# note you can call your variable what you like
# best practice is to be brief as possible while descriptive of what it does/is
# you can enter any input prompt you like
# best practice is to be brief as possible while helpfully descriptive

# output returned as a float ... meaning with a decimal
# there are ways - easy ways to tell the program to only return the number
# ... meaning to return only the number as a whole number (w/o the decimal)

# how to convert float number to whole number in python
num11 = int(input("Enter Number 11: "))
num13 = int(input("Enter Number 13: "))
output = num11 / num13
print(math.ceil(output))
# we can round, round up, round down .. . let us round up

