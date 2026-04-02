
length1=int(input("please enter value of length of first rectangle"))
width1=int(input("please enter value of width of first rectangle"))

length2=int(input("please enter value of length of second rectangle"))
width2=int(input('please enter value of with of seconbd recatnagle'))
area1=length1*width1
area2=length2*width2
if area1 > area2:
    print("first rectangle have greater area")
else:
    print("second rectangle have greater area")