** For documentation purposes I asked feedback on ChatGPT on what I can improve on my code**

---

### ✅ What you did well

1. **Modular code**: you broke things into functions (`to_guess`, `attempts`, `higher_lower`, etc.), which is exactly how clean code is structured.
2. **Difficulty system**: works correctly with `easy` and `hard` attempts.
3. **Higher/lower feedback**: nice clear messages for the user.
4. **Main game loop**: allows replaying (`S` to start, `E` to exit). That’s a great touch.

---

### ⚡ Improvements

1. **`to_guess()` is more complicated than needed**

   ```python
   def to_guess():
       chosen_number = 0
       number = random.randint(1, 100)
       chosen_number += number
       return chosen_number
   ```

   * `chosen_number = 0` is unnecessary.
   * Simpler:

     ```python
     def to_guess():
         return random.randint(1, 100)
     ```

2. **Variable/function name collision**
   You have:

   ```python
   def attempts():
   def user_guess():
   ```

   and then also use `attempts` and `user_guess` as variables in your loop.
   👉 This shadows your function names. Python lets you do it, but it can get confusing or cause bugs.
   ✅ Suggestion: rename functions more clearly:

   * `get_attempts()` instead of `attempts()`
   * `get_user_guess()` instead of `user_guess()`

3. **`higher_lower()` could be cleaner**
   Instead of this:

   ```python
   if to_guess > user_guess:
       return "Higher"
   elif to_guess < user_guess:
       return "Lower"
   elif to_guess == user_guess:
       return 'Correct!'
   else:
       return "Enter valid number from 1-100"
   ```

   You can just write:

   ```python
   if user_guess < to_guess:
       return "Higher"
   elif user_guess > to_guess:
       return "Lower"
   return "Correct!"
   ```

4. **`attempts_left()` is unused**
   You wrote a function for reducing attempts, but then directly subtracted inside the loop:

   ```python
   available_attempts -= 1
   ```

   👉 Either use the function or remove it to keep things clean.

5. **Input validation**
   If the user types something that’s not a number, your game will crash (`int(input(...))`).
   ✅ You could wrap it with `try/except ValueError`.

---

### ✨ Example cleaned-up version (same logic, simpler names)

```python
import random

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
                print("🎉 You got it right!")
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
```

---

