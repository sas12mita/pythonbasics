#dictionary = {key:value for item in iterable if condition}
d={x:x*x for x in range(0,10) if x %2==0}
print(d)

#temp in fah
celcius=[34,35,36,37]
fah={i:(i*9/5)+32 for i in celcius}
print(fah)

#zip function
names = ["Asha", "Ravi", "John"]
marks = [80, 90, 85]

result = zip(names, marks)

print(list(result))

student = {"name": "John", "age": 20, "grade": "A"}

# 1. Keys only
for key in student:
    print(key)

print("------")

# 2. Keys using keys()
for key in student.keys():
    print(key)

print("------")

# 3. Values only
for value in student.values():
    print(value)

print("------")

# 4. Key and value (best method)
for key, value in student.items():
    print(key, value)

print("------")

# 5. Key and value with formatting
for key, value in student.items():
    print(key + ":", value)

print("------")

# 6. With index using enumerate
for i, (key, value) in enumerate(student.items()):
    print(i, key, value)

print("------")

# 7. Modify dictionary values
for key in student:
    student[key] = str(student[key]) + " updated"

print(student)

print("------")

# 8. Nested dictionary example
data = {
    "student1": {"name": "Asha", "age": 20},
    "student2": {"name": "Ravi", "age": 22}
}

for outer_key, inner_dict in data.items():
    for key, value in inner_dict.items():
        print(outer_key, key, value)