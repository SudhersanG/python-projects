#SILENT AUCTION PROGRAM
import os
print("*******AUCTION PROGRAM********")
def bidWinner(bidderDetails):
    
    bidWinName=""
    bidWinPrice=0
    
    for bidder in bidderDetails:
        biddingPrice=bidderDetails[bidder]
        
        if biddingPrice>bidWinPrice:
            bidWinPrice=biddingPrice
            bidWinName=bidder
            
    print(bidWinName,"\n")
    print(bidWinPrice)
    
    print(f"AUCTION PROGRAM WINNER IS:{bidWinName}\n")
    
    print(f"Bidder details are:{bidderDetails}")
                                       

bidderDetails={}

end=False

while not end:
    name=input("enter the name of the bidder:")
    bidPrice=int(input("enter bidding price:"))
    bidderDetails[name]=bidPrice
                 
    moreBidder=input("want to add more bidder details (yes/no):").lower()
    
    if moreBidder=="yes":
       os.system('cls')
       
    elif moreBidder=="no":
        end=True
        bidWinner(bidderDetails)
        

             
            
