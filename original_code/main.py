from art import logo
bids = {}
new_bid = 'y'
highest_bid = 0
winner = ''
while new_bid == 'y':
    # Ask the user for input
    name = input('Please write down your name: \n')
    bid = int(input('Please write down your bid: \n'))
    # Compare bids in dictionary
    if bid > highest_bid:
        highest_bid = bid
        winner = name
    # Save data into dictionary {name: price}
    bids[name] = bid

    # print(bids)
    # Whether if new bids need to be added
    new_bid = input('Are there any other bidders? "Y/N" \n').lower()
    if new_bid == 'y':
        print('\n' * 100)

print(f'The winner is {winner} with a bid of {highest_bid}!')
