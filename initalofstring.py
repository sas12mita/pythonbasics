#wrte a function initials(firstname,lastname)
#and returns a string with then initials
#of that person
#expmple :initial of a person john smit would be js

firstname=input("input first name")
lastname=input("input last name")
def initial(firstname,lastname):
    initialname=firstname[0] +lastname[0]
    return initialname

inital_name=initial(firstname,lastname)