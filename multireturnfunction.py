#multiplereturn
def  calculate(x,y):
    sum=x+y
    difference=x-y
    mult=x*y
    division=x/y
    return sum,difference,mult,division
result=calculate(9,3)
print(result)#give output as a tuple
sum,diff,mult,divi=calculate(7,8)
print(sum,diff,mult,divi)
