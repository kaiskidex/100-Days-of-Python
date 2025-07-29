import random

print('''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"        
      ''')

# word list and random selection
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# hangman ascii

hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(hangman_ascii[0])

lives = 6

blank_length = []
for index, char in enumerate(chosen_word):
    blank_length.append("_")

blank_display = " ".join(blank_length)
print(blank_display)

def letter_guess():
    return input("\nEnter letter guess: ").lower()

        
while lives > 0:
    user_guess = letter_guess()


    if user_guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == user_guess:
                blank_length[index] = user_guess
        print("\nYou are correct!")
    else:
        print("\nYou are wrong!") 
        lives -= 1
        print(hangman_ascii[6-lives])
    
    print(" ".join(blank_length))
    print(f"Lives: {lives} out of 6")

    #win
    if "_" not in blank_length:
        print("You win")
        break

    #lose
    if lives == 0:
        print(f"Game over")
        print(f"The word was: {chosen_word}")

    





