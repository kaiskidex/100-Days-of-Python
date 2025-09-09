'''🎮 Project Theme: “Dragon Dice Quest”

You’re an adventurer rolling dice to fight a dragon.
Each roll adds to your attack power, and you must reach at least 20 power to slay the dragon.'''

'''📝 Guided To-Do List (Step by Step Quests)
Quest 1: The Dice of Fate

Write a function roll_die() that returns a random number from 1–6.

Test it by rolling 5 times and printing results.'''

import random


def roll_die():
    return random.randint(1,6)


# for i in range(1,6):
#     result = roll_die()
#     print(result)


'''Quest 2: The Adventurer’s Journey

Write a function gather_power(limit):

Keep rolling the die until your total ≥ limit (e.g., 20).

Return the total and how many rolls it took.

Print the rolls step by step.'''


def gather_power(limit):
    total = 0
    roll = 0

    while total < limit:
        num = roll_die()
        total += num
        roll += 1
        print(f"Roll {roll}: You rolled {num}, total = {total}")
    return total, roll


'''Quest 3: The Hero’s Chronicle

Store adventurers’ scores in a dictionary {name: score}.

If a name already exists, update it with the new score.'''



def record_score(scores, name, score):
    scores[name] = score
    return scores
    

'''Quest 4: The Hall of Heroes

Write a function to find the adventurer with the highest score from the dictionary.'''


def highest(scores):
    highest_adventurer = None
    highest_score = -1

    for name, score in scores.items():
        if score > highest_score:
            highest_score = score
            highest_adventurer = name
    
    return highest_adventurer, highest_score


'''Quest 5: The Guild’s Choice

Write a menu with [1] Fight Dragon and [2] Exit.

If the player fights, run gather_power(20) and store their score.

If they exit, show the highest scorer.

Final Boss Quest: Full Game

Combine everything into a loop:

Menu

Dice rolls (fight dragon)

Store scores

Show highest scorer on exit'''

def dragon_dice_game():
    scores = {}

    while True:
        print("\n === 🐲 Dragon Dice Quest ===")
        print("[1] Fight Dragon")
        print("[2] Flee!")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your adventurer name: ")
            print(f"\n🤺 {name} enter the battle!")
            total, rolls = gather_power(20)

            if total >= 20:
                print(f"🎉 {name} slays the dragon with {total} power in {rolls} rolls!")
            else:
                print(f"💀 {name} was defeated...")

            record_score(scores, name, total)

        elif choice == "2":
            if scores:
                champion, top_score = highest(scores)
                print(f"\n🏆 The Hall of Heroes: {champion} reigns supreme with {top_score} power!")
            else:
                print("\nNo heroes fought today.")
            break

        else:
            print("Invalid choice, try again!")

# run the game

dragon_dice_game()