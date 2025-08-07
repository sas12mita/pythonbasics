# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


#print odd and even number
numbers = [2, 5, 8, 11, 14, 17]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


# Count the number greater than 10
numbers = [3, 12, 7, 19, 4]
count = 0

for num in numbers:
    if num > 10:
        count += 1

print("Numbers greater than 10:", count)

# Average Calculator
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

nums = [10, 20, 30, 40, 50]
average = calculate_average(nums)
print("Average is:", average)
