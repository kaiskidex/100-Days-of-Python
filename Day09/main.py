bids = {}

def bidding():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $ "))
    bids[name] = bid

def find_winner():
    highest_bid = 0
    winner = ""

    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid} congratulations!")

while True:
    bidding()
    new = input("Are there other bidders? (Y or N)").upper()
    if new == 'Y':
        print("\n" * 100)
    else:
        find_winner()
        break