#Project: Simple Calculator with History

# 📌 Project: Basic Arithmetic Calculator
# Goal: Build a calculator that:
# Performs basic math operations
# Tracks a history of calculations
# Lets the user review past results



# Do the operation
# Show and store the result


#history

history = []
count = 1


# ask for two numbers
def user_numbers():
    try:
        number1 = int(input("Input first number: "))
        number2 = int(input("Input second number: "))
        return number1, number2
    except ValueError:
        print("Invalid Input! Please enter numbers only.")


# add function
def add(x,y):
    result = x + y
    history.append(f"{x} + {y} = {result}")
    print(f"{x} + {y} = {result}") 
    return result

# subtract function
def subtract(x, y):
    result = x - y
    history.append(f"{x} - {y} = {result}")
    print(f"{x} - {y} = {result}")
    return result

# multiply 
def multiply(x, y):
    result = x * y
    history.append(f"{x} * {y} = {result}")
    print(f"{x} * {y} = {result}")
    return result

# divide
def divide(x, y):
    result = x / y
    history.append(f"{x} / {y} = {result}")
    print(f"{x} / {y} = {result}")
    return result

# define dictionary
operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide
}

# main loop
while True: 
    user_choice = input( '''  
        ---Simple Calculator---
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. View History
        6. Exit

    Your choice:    
    ''')

    if user_choice in operations: #checks if the user's choice is valid, operations is the dictionary of functions 
        nums = user_numbers() #calls function, the tuple now saved in variable "nums"
        if nums: #checks if nums is not None, protects code from crashing, continues only if user_numbers() returned actual numbers
            n1, n2 = nums #tuple unpacking, splits the numbers from the tuple you get from user_numbers()
            result = operations[user_choice](n1, n2) #operations give the actual function like "add", then call with n1 n2  the result get stored in result 
        if result is not None: #checks if user gave valid result, "None" will output to signal an error, prevents print() to print "None"
            print("Result: ", result)
    
    elif user_choice == "5":
            if not history:
                print("No history yet")
            else:
                for idx, item in enumerate(history, start=1):
                    print(f"{idx}. {item}")

    elif user_choice == "6":
        print("Bye Bye!")
        break 
    
    else:
        print("Invalid Input!")


 
    



    
    





