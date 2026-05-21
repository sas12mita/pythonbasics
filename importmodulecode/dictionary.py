# Practice using dictionaries to create key-value
# pairs, add and remove items, and perform basic
# operations like iterating through a dictionary
# 2. Solve the problem of counting the frequency of
# words in a list using dictionaries
# 3. Share your solution with the class and explain
# how you used dictionaries to solve the problem
# 4. Reflect on what you learned about using
# dictionaries and how they can be used in realworld programming

student={"name":"Sasmita",
         "address":"Perth WA",
         "age" : 84,
         }
#add new key and value
student["grade"]="HD"
print(student)

#update age key
student["age"] = 21

# Remove item
del student["course"]

# Iterate through dictionary
for key, value in student.items():
    print(key, value)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)