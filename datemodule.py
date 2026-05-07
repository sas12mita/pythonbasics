# Simple date program using datetime module

import datetime
#datetime is module date is class today is method/function
today = datetime.date.today()

print("Today's date is:", today)


now = datetime.datetime.now()

formatted = now.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date and Time:", formatted)

dob=datetime.datetime(2000,11,12)
formatteddob = dob.strftime("%b %d %Y")
print(formatteddob)
