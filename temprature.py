def convert_temp(value,unit):
    if unit=="C":
        return (9/5*value)+35
    if unit=="F":
        return  (value-32)*5/9

while True:
    value= float(input("Enter temprature for conversion: "))
    unit=input("Enter unit C or F: ")
    result=convert_temp(value,unit)
    print("Ther temprature afer conversion is ",result)
    user_choice=input("do you want to continue y or n: ")
    if user_choice=="n":
        break





