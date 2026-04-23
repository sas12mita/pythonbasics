user_in=input("do you wamt to do sum press y or N")
sum=0
while user_in.lower()=="y":
    num=int(input("enter a num"))
    sum=sum+num
    print("sum is",sum)
    user_in=input("do you want to stop press y or N")