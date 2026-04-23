def display_grading_function(score):
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "F"
    
score=int(input("input your garde: "))
grade=display_grading_function(score)
print(f"Your grade is {grade}")