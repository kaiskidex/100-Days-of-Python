import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["Rock", "Paper", "Scissors"]

#player
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if player_choice == 0:
    print(f"You chose rock \n {rock}")
elif player_choice == 1:
    print(f"You chose paper \n {paper}")
elif player_choice == 2:
    print(f"You chose scissors \n {scissors}")

#computer
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(f"The computer chose rock \n {rock} ")
elif computer_choice == 1:
    print(f"The computer chose paper \n {paper}")
elif computer_choice == 2:
    print(f"The computer chose scissors \n {scissors}")

#logic
if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice - computer_choice) % 3 == 1:
    print("You win!")
else:
    print("You lose!")

