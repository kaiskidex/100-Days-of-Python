import random
import ascii

# randomly chooses a card 
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#calculates score of hand 
def calculate_score(hand):
    # Blackjack
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    #If sum > 21 and there's an Ace (11), turn it into 1.
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

# if player decides to hit, which means they get a new card
def play_turn(hand):
    updated_hand = hand.copy()
    new_card = deal_card()
    updated_hand.append(new_card)
    new_score = calculate_score(updated_hand)
    return updated_hand, new_score

# returns intial 2 cards 
def deal_hand():
    hand = []
    for _ in range(2):
        hand.append(deal_card())
    return hand

# only shows computer's first card and the player's hand
def initial_card():
    computer_hand = deal_hand()
    user_hand = deal_hand()
    return computer_hand, user_hand

# comparing scores
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Scores went over"
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "Lose, you went over"
    elif computer_score > 21:
        return "Win, Opponent went over."  
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
# continue
def game_continue():
    while True:
        new_game = input("Press [N] for new game or [E] to exit: ").upper()
        if new_game == 'N':
            return True
        elif new_game == 'E':
            return False
        else:
            print("Invalid input. Try again.")

continue_playing = True

# main loop
while continue_playing:
    print(ascii.black_jack)

    computer_hand, user_hand = initial_card()
    current_score = calculate_score(user_hand)
    print(f"Your cards: {user_hand}")
    print(f"Current score: {current_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    if current_score == 0:
        print("You win at first deal!")
        print(ascii.win)

        continue_playing = game_continue()
    else:
        # Player's turn - can hit multiple times
        game_over = False
        while not game_over:
            choice2 = input(" [H] Hit - Take another card \n [S] Stand - Keep current hand \n [Q] Quit game \n").upper()
            
            if choice2 == 'H':
                updated_hand, new_score = play_turn(user_hand)
                user_hand = updated_hand
                current_score = new_score
                print(f"Your cards: {user_hand}")
                print(f"Your score: {current_score}")
                
                if current_score > 21:
                    print("You busted!")
                    game_over = True
                elif current_score == 21:
                    print("You got 21!")
                    game_over = True

            elif choice2 == 'S':
                print("You chose to stand.")
                game_over = True

            elif choice2 == 'Q':
                continue_playing = False
                game_over = True

            else:
                print("Invalid input. Try again.")

        # If player didn't quit, dealer plays and show results
        if continue_playing:
            # Dealer plays - must draw until 17 or higher
            while calculate_score(computer_hand) < 17:
                computer_hand.append(deal_card())
            
            computer_score = calculate_score(computer_hand)
            print(f"\n--- FINAL RESULTS ---")
            print(f"Your final cards: {user_hand}")
            print(f"Your final score: {current_score}")
            print(f"Computer cards: {computer_hand}")
            print(f"Computer score: {computer_score}")

            print(compare(current_score, computer_score))

            continue_playing = game_continue()