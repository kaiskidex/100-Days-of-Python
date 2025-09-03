import random

# Easy level: 10 attempts
#Hard Level: 5 attempts

# random number
def to_guess():
    chosen_number = 0
    number = random.randint(1, 100)
    chosen_number += number
    return chosen_number


# difficulty
def attempts():
    attempts = [10,5]
    user_attempts = 0
    difficulty = ''
    choice = input('Choose difficulty (Easy or Hard): ').lower()
    if choice == 'easy':
        user_attempts += attempts[0]
        difficulty = 'Easy'
    elif choice == 'hard':
        user_attempts += attempts[1]
        difficulty = 'Hard'
    else:
        print('Enter valid choice.')

    return user_attempts, difficulty


# higher or lower
def higher_lower(to_guess, user_guess):
    if to_guess > user_guess:
        return "Higher"
    elif to_guess < user_guess:
        return "Lower"
    elif to_guess == user_guess:
        return 'Correct!'
    else:
        return "Enter valid number from 1-100"


# guesses
def attempts_left(attempts, user_guess, chosen_number):
    if user_guess != chosen_number:
        attempts -= 1
        return attempts


# user guess 
def user_guess():
    guess = int(input("Enter your guess from 1-100: "))
    return guess



# main loop
while True:
    start = input('Play game? Press [S] to start. Press [E] to exit: ').upper()
    if start == 'S':
        available_attempts, difficulty = attempts()
        print(f"You set the difficulty to {difficulty}.  You have {available_attempts} attempts.")
        print(f"I'm thinking of a number. Take a guess!")
        secret_number = to_guess()
        while available_attempts > 0:
            number_guess = user_guess()
            print(higher_lower(secret_number, number_guess))
                
            if number_guess != secret_number:
                available_attempts -= 1
                print(f"You have {available_attempts} attempts left.")
                if available_attempts == 0:
                    print("Game over.")
                    break
            elif number_guess == secret_number:
                print("You got it right!")
                break
            else:
                print("Enter a valid number.")


    elif start == 'E':
        break
    else:
        print("Invalid input. Try again")
