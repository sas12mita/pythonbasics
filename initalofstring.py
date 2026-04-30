#wrte a function initials(firstname,lastname)
#and returns a string with then initials
#of that person
#expmple :initial of a person john smit would be js
firstname = input("input first name: ")
lastname = input("input last name: ")

def initial(firstname, lastname):
    return f"{firstname[0].upper()}.{lastname[0].upper()}."

result = initial(firstname, lastname)

print(result)

