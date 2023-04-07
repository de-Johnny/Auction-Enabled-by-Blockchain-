import random
import time
import hashlib

# Land for auction
land_for_sale = "A land located in Clearway Bay"

# List of property developers
bidders = ["Developer A", "Developer B", "Developer C", "Developer D", "Developer E"]

starting_bid = 10
min_bid_increment = 1

# Define the blockchain
blockchain = [{"transaction": 
               "Genesis Block", 
               "previous_hash": None, 
               "hash": None}]

# Function to add a new block to the blockchain
def add_block(transaction):
    last_block = blockchain[-1]
    previous_hash = last_block["hash"]
    block = {"transaction": transaction, "previous_hash": previous_hash}
    block["hash"] = hashlib.sha256(str(block).encode()).hexdigest()
    blockchain.append(block)

# Define a function to print the current state of the auction
def print_auction_state(current_bidder, current_bid):
    print(f"Current highest bidder: {current_bidder}")
    print(f"Current highest bid: {current_bid} billion HKD")
    print("Blockchain:")
    for block in blockchain:
        print(block)
        print ("\n")

# Start the auction
print(f"Auction for {land_for_sale} has started!")
print_auction_state("", starting_bid)

# Loop until only one bidder remains or the auction ends
while len(bidders) > 1:
    # Pick a bidder at random
    current_bidder = random.choice(bidders)
    # Generate a random bid
    current_bid = starting_bid + min_bid_increment * random.randint(1, 10)
    # Check if the bid is higher than the current highest bid
    if current_bid > starting_bid:
        # Update the starting bid and print the new state of the auction
        starting_bid = current_bid
        add_block(f"{current_bidder} bid {current_bid} billion HKD")
        print(f"{current_bidder} bids {current_bid} billion HKD!")
        print_auction_state(current_bidder, current_bid)
        # If the bid is higher than the others, remove them from the list
        bidders = [bidder for bidder in bidders if bidder != current_bidder]
        time.sleep(1) # wait for 1 second before the next bid
    else:
        # If the bid is not higher, print a message
        print(f"{current_bidder} did not bid higher than {starting_bid} billion HKD.")
        time.sleep(0.5) # wait for 0.5 second before the next bidder

# Print the winner of the auction
print(f"Auction for {land_for_sale} has ended!")
print(f"The winner is {bidders[0]} with a bid of {starting_bid} billion HKD.")
print("Blockchain:")
for block in blockchain:
    print(block)
    print ("\n")
