
import random
from gamedata import data 

# loop

# Game Title: Higher Lower Game, user guesses who has more followers

# Rules:
# Don't show the number of follower account
# first round, 2 random accounts from dictionary
# if wrong in first round, terminate program and show Game Over
# if right, add + 1 to score and keep game running, 
# the right account from first round will be compared to next random accounts
# make sure no duplicates
# keep going until player gets it wrong
# count all scores in total and display


#name, follower_count, description, country

# track the follower_count


# get account
def get_account():
    return random.choice(data)


# user guess and formatting ?
def user_choice(choice1, choice2):
    print(f"Choice A: {choice1['name']}, {choice1['description']}, from {choice1['country']}")
    print(f"Choice B: {choice2['name']}, {choice2['description']}, from {choice2['country']}")

    while True:
        choice = input("Choose A or B: ").upper()

        if choice == 'A':
            return choice1
        elif choice == 'B':
            return choice2
        else:
            print('Invalid choice!')


#compare accounts and return right answer
def compare(account1, account2):
    if account1['follower_count'] > account2['follower_count']:
        return account1
    else:
        return account2

# right or wrong
# check if the user choice is equal to the details on compare() function
def check_answer(user_answer, correct_answer, score):
    if user_answer == correct_answer:
        print('Right!')
        score += 1
        return score, True
    elif user_answer != correct_answer:
        print('Game Over!')
        return score, False
    
score = 0
continue_game = True
# main loop

print('Welcome to Higher Lower Game!')
print('Game Mechanics: Choose the letter of your answer (A or B) on which account has more followers: ')

choice1= get_account()

previous_choice2 = None

while continue_game:

    choice2 = get_account()
    while choice2 == choice1 or choice2 == previous_choice2: # avoid duplicate
        choice2 = get_account()

    # displays 2 accounts and asks to choose a or b
    user_answer = user_choice(choice1, choice2)

    # computer compares the two accounts and which is higher
    correct_answer = compare(choice1, choice2)

    # computer verifies user's answers and compares it to the correct account
    score, continue_game = check_answer(user_answer, correct_answer, score)

    # if right, game continues and we use the previous correct answer and compare it with new one
    if continue_game:
        print(f"Correct! Current Score: {score}")
        previous_choice2 = choice2 # track what was used last round
        choice1 = correct_answer 
    else:
        print(f"Final Score: {score}")

       


