#reading deflict is the difference between idea; and actual reading time
totalhr1=0
for i in range(1,8):
    readinghrs=int(input(f"Enter total reading hrs for {i} day: "))
    totalhr+=readinghrs
print(f"Total reading hrs is {totalhr}")
def totalreadinghrs(hours):
    if(hours<14):
        behindhrs=14-hours
        print(f"The student behind {behindhrs}  as compare to ideal hrs")
    else:
        print("There is nor deflict, they have good reading habit")

totalreadinghrs(totalhr)