#Task 1
user_prompt = input("Enter the operation you want to perform (addition, subtraction, division, multiplication): ")

def calculator(user_prompt):
    if user_prompt == "addition":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1 + num2
    elif user_prompt == "subtraction":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1 - num2
    elif user_prompt == "division":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("You cannot divide by zero")
    elif user_prompt == "multiplication":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1 * num2

print(calculator(user_prompt))
