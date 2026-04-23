def time_table(number):
    for i in range(1,11):
        print(f"{number}*{i}={number*i}")
while True:
    number= input("Enter a number to print rhe time_table: ")
    if(number=="exit"):
        print("exiting program........")
        break
    time_table(int(number))
    