currentBid = 0
bidding = True

while bidding == True:
    userinput = input("Would you like to place a bid?")

    if userinput == "Yes":
        newBid = input("How much would you like to bid for?")
    else:
        bidding = False
    if int(newBid) > int(currentBid):
        currentBid = newBid
    else:
        print("Invalid bid! You must place a higher bid!")
    print("Current Bid:" + currentBid)
    print("End of bidding. Final Bid:" + currentBid)
currentBid = 0
bidding = True







































