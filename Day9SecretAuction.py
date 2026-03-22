import sys
# {key: value}
bidders = []

capture_more_bidders = 'yes'

print("Welcome to the secret auction program.")

while capture_more_bidders == 'yes':    
    name = input("What is your name?\n>")
    bid = input("What is your bid?\n>$")
    bidders.append({"name": name, "bid": float(bid)})
    capture_more_bidders = str.lower(input("Are there any other bidders? Type 'yes' or 'no'."))

highest_bidder = {'name': "", 'bid': 0}

for current_bidder in bidders:
    if current_bidder['bid'] > highest_bidder['bid']:
        highest_bidder = current_bidder

print(f"The winner is {highest_bidder['name']} with a bid of ${str(highest_bidder['bid'])}")