score=int(input("Enter score"))
def assign_grade(score,extra_credit=0):
    extra_credit=5
    final_score=score+extra_credit
    if final_score < 50:
        grade = "F"
    elif final_score < 65:
        grade = "P"
    elif final_score < 75:
        grade = "C"
    elif final_score < 85:
        grade = "D"
    else:
        grade = "HD"
    print(f"The student scored {score} + {extra_credit} extra credit = {final_score}, which is a grade {grade}.")
assign_grade(score)

