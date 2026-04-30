# Variable example
x = 10
print("Value of x:", x)
print("Memory address of x:", id(x))
x=30
print("Value of x:", x)
print("Memory address of x:", id(x))

# List example
my_list = [1, 2, 3]
print("Value of my_list:", my_list)
print("Memory address of my_list:", id(my_list))
my_list.append(2)

print("Value of my_list:", my_list)
print("Memory address of my_list:", id(my_list))
#"learning "Python" Programming"
print('leaning "python" programming')
#escape characters #\
print("learning\"python\"Programming")
#\n
print("Python\nprogramming")
#\t 
print("python \t programming")
#\r moving cursor to beginning of the line
print("python\r python")
#b
print("python\b programming")
word="python"
for i in word:
    print(i)
#what is the occurnce of a word in string

def word_occurance(st):
    count=0
    letter=input("Enter the letter to count")
    for i in st:
        if "a" in i:
            count=count+1
    print(f"The letter occur {count} time")
st=input("enter the string: ")   
word_occurance(st)