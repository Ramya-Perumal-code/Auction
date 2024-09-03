from art import logo

print(logo)
bid_dict = {}
loop = True
high = 0
winner = ''
while loop:
    # Ask the user for input
    name = input("What is your name?: ").lower()
    amt = int(input("What is your bid?: $"))

    # Save data into dictionary {name: price}
    bid_dict[name] = amt

    # Whether if new bids need to be added
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if next_bidder == 'no':
        loop = False
    else:
        print("\n " * 25)

# Compare bids in dictionary
for key in bid_dict:
    if bid_dict[key] > high:
        high = bid_dict[key]
        winner = key

print(f"The winner is {winner} with a bid of ${high}")
