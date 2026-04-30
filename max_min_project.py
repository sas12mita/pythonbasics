#write function that return the 
#maximum number from the list
#minimum number form the list
#find the tota of all the element
number=[1,23,545,13,56,67]
total=0
def max_min(li):
    max_number=li[0]
    min_number=li[0]
    for i in li:
        if(max_number<i):
            max_number=i
        if(min_number>i):
            min_number=i
        
        total=total+i
    print("The maximum number is ", max_number)
    print("The minimum number is ",min_number)
    print("The total ", total)
    