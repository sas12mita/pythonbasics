import random

print(random.randint(2, 20))
print(random.randrange(100))
print(random.random())
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)