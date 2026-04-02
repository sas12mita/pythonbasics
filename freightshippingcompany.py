package_weight=int(input("enter your sized of package"))
if package_weight <= 2:
    rate=1.10* package_weight
elif package_weight <6:
    rate=2.20*package_weight
elif  package_weight<10:
    rate=3.70*package_weight
else:
    rate=3.80*package_weight
print("The rate is",rate)