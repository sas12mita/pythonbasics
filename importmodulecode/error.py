try:
    num = int(input("Enter number: "))
    if num <0:
        raise ValueError
    print(num)
except ValueError as e:
    print("Invalid input",e)
except NameError as e:
    print(e)
