bookPurchased=int(input("enter the number of book pucrchased each month "))
if bookPurchased==0:
    print("You earn 0 point")
elif bookPurchased==1:
    print("You earn 5 points")
elif bookPurchased==2:
    print("You earn 15 points")
elif bookPurchased==3:
    print("You earn 30 points")
else:
    print("you earn 60 points")