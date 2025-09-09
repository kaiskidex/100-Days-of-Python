import random

# full refactor by ChatGPT for documentation purposes and for studying

def get_secret_number():
    return random.randint(1, 100)

def get_attempts():
    attempts = {"easy": 10, "hard": 5}
    choice = input("Choose difficulty (Easy or Hard): ").lower()
    return attempts.get(choice, 0), choice.capitalize() if choice in attempts else "Invalid"

def feedback(secret, guess):
    if guess < secret:
        return "Higher"
    elif guess > secret:
        return "Lower"
    return "Correct!"

def get_user_guess():
    while True:
        try:
            return int(input("Enter your guess from 1-100: "))
        except ValueError:
            print("Please enter a valid number.")

# main loop
while True:
    start = input("Play game? Press [S] to start. Press [E] to exit: ").upper()
    if start == "S":
        attempts, difficulty = get_attempts()
        if attempts == 0:
            print("Invalid difficulty choice.")
            continue

        print(f"You chose {difficulty} mode. You have {attempts} attempts.")
        secret_number = get_secret_number()

        while attempts > 0:
            guess = get_user_guess()
            result = feedback(secret_number, guess)
            print(result)

            if result == "Correct!":
                print(" You got it right!")
                break

            attempts -= 1
            print(f"Attempts left: {attempts}")

            if attempts == 0:
                print(f"Game over! The number was {secret_number}.")

    elif start == "E":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
