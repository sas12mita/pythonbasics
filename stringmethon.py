# Python String Methods - Full Example

text = "  hello world  "

print("Original String:", text)

# strip() - Remove spaces from both sides
print("strip():", text.strip())

# lstrip() - Remove spaces from left side
print("lstrip():", text.lstrip())

# rstrip() - Remove spaces from right side
print("rstrip():", text.rstrip())

# upper() - Convert to uppercase
print("upper():", text.upper())

# lower() - Convert to lowercase
print("lower():", text.lower())

# title() - Capitalize first letter of each word
print("title():", text.title())

# capitalize() - Capitalize first letter only
print("capitalize():", text.capitalize())

# replace() - Replace word
print("replace():", text.replace("world", "Python"))

# split() - Split into list
print("split():", text.split())

# find() - Find position of word
print("find('world'):", text.find("world"))

# startswith() - Check starting character
print("startswith(' '):", text.startswith(" "))

# endswith() - Check ending character
print("endswith(' '):", text.endswith(" "))

# count() - Count occurrences
print("count('l'):", text.count("l"))

# len() - Length of string
print("Length:", len(text))
#calculate percentange form the marks input by user
#assume marks_input is strinfg having marks seoerated by comma
marks=input("Enter marks of student ")
marks_list=marks.split(",")
marks = [int(mark.strip()) for mark in marks_list]
total_obtained = sum(marks)
total_marks = len(marks) * 100
percentage = (total_obtained / total_marks) * 100
print("Marks:", marks)
print("Total Obtained:", total_obtained)
print("Percentage:", percentage, "%")