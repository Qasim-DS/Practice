# Activity 1:
# Problem Statement:
# Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).

# Questions:
# Modulus Operator [%]


for num in range(1,101):
    if num % 3 == 0 or num % 5 == 0 or num % 15 == 0:
        print('Fizz')
    else:
        print(num)    

# Activity 2: Swap Cases
# Problem Statement:
# How to swap all uppercase characters to lowercase and vice versa?

# Questions:
# isupper() to check input are in upper case
# islower() to check input are in lower case

# upper() to convert input into upper case
# lower() to convert input into lower case

user_input = input("Enter your input in either Lower or Upper case: ")
if user_input.isupper():
    print("Input is in upper case.")
    print(user_input.lower())
else:
    print("Input is in Lower case.")
    print(user_input.upper())

# Activity 3: Swap Numbers
# Problem Statement:
# Swap the numbers with and without the 3rd Variable.

# Questions:
# - How you will create and store the value in 3rd variable?
# - How you will do it without the 3rd Variable?

a, b = 2, 4
a, b = b, a
print(a, b)

a = 2
b = 4
temp = a
a = b
b = temp
print ('a = ', a)
print ('b = ', b)

def add(*x):
    res = 0
    for i in x:
        res = res + i
    return res
    
# print(add(2,5,3))

# Activity 4:  Fibonacci Series
# Problem Statement: Write a code in python which will give you a Fibonacci series to a number when you enter it.

# Questions:
# How you will you deal when a user inputs ‘0’: Using if-elif-else condition to check the input value.
# How the user will deal when a user inputs ‘1’: Using if-elif-else condition to check the input value.
# Which loops and statements do you use for the iterations: Using while loop for iterations.
n = int(input("Enter a number: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:

    print("Fibonacci sequence:")
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
print()

# Activity 5: Number Guessing Game
# Problem Statement: Create a game in which user guesses a random number in python.
# Questions:  How will generate random number and how will you set the range? By using random module then setting the range by using randint function.
# How to add attempts in your code, that user can have only 5 attempts to play? By using while loop and setting the condition for attempts.
# How will you subtract a attempt when user plays it one time? By using increment operator.
# How will you show the ‘YOU WON!’ and ‘YOU LOST’ message? By using if-else condition.
import random

ran = random.randint(1, 10)
i = 1
while i <= 5:
    user_guess = int(input("Enter your guess (1-10): "))
    if user_guess == ran:
        print("You've guessed the correct number:", ran)
        break
    else:
        print("Incorrect guess. Try again.", user_guess)
    i += 1


# Activity 6: Basic Calculator
# Problem Statement: Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.
# Questions:
# How to create Choices for the user? By using input function to take input from user.
# How the user input two numbers? By using input function to take input from user.
# How can you add your define functions inside your If-else statements? By performing the operations inside the if-else statements.
# How do stop the calculations at a certain part? By using if-else statements to check for valid operations.
# How do you cope with this when a user will type a invalid input? By using else statement to handle invalid inputs.

user_choice = int(input("Choose an operation (1: Add, 2: Subtract, 3: Multiply, 4: Divide): "))
if user_choice in [1, 2, 3, 4]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if user_choice == 1:
        operation = "Addition"
        result = num1 + num2
        
    elif user_choice == 2:
        result = num1 - num2
        operation = "Subtraction"

    elif user_choice == 3:
        result = num1 * num2
        operation = "Multiplication"
        
    elif user_choice == 4:
        if num2 != 0:
            result = num1 / num2
            operation = "Division"
        else:
            result = "Error! Division by zero."
    
    print(f"{operation} Result: {result}")
else:
    print("Invalid choice. Please select a valid operation number (1-4).")