#sum=0
#initialization 
#while num!=0
#prompt the user to input a number
#sum =sum+number
num=int(input("enter a number to sum 0r zero to stop"))
sum=0
i=0
while num!=0:
        i=i+1
        sum=sum+num
        num=int(input("enter a number to sum"))
        print("Sum of number",sum)
        if i !=0:
         print("Average of user enttered number",sum/i)

