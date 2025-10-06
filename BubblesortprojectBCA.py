# Ask user how many numbers they want
n = int(input("How many numbers do you want in the list? "))

# Create an empty list
num = []

# Take input from the user
for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    num.append(number)

# Bubble Sort
for i in range(n-1):
    for j in range(n-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

# Print the sorted list
print("Sorted list:", num)
