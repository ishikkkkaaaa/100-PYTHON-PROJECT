bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bidder = 0
    # {"ishika":123,"isha":421}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")


while not bidding_finished:
    name = input("What is your name??")
    price = int(input("What is your bid?? $"))
    bids[name] = price
    should_continue = input("Are there more bidders? type YES or NO \n")
    if should_continue == "NO":
        bidding_finished = True
        find_highest_bidder(bids)
