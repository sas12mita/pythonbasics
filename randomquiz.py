#store math quiz
#use random
#choice[+,-,*,/]
#shuffle operator
#ask the question
#allow the user to give the ans
#check the ans
 
import random
operator=['+','-','*','/']
random.shuffle(operator)
num1=random.randint(1,10)
num2=random.randint(1,10)
op=random.choice(operator)
user_answer= float(input(f"what is {num1} {op} {num2}: "))
if op=="+":
    correct_ans=num1+num2
elif op=="-":
    correct_ans=num1-num2
elif op=="*":
    correct_ans=num1*num2
elif op=="/":
    correct_ans=num1/num2
else:
    print("Something went to wrong")

if(user_answer==correct_ans):
    print("Your answer is correct:",correct_ans)
else:
    print("Your answer is wrong and correct answer is: ", correct_ans)

