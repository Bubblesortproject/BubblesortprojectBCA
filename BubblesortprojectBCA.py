num = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(num)
for i in range(n-1):                      # Loop through passes 
  for j in range(n-i-1):                  # Compare adjacent elements
    if num[j] > num[j+1]:                 # If left > right, swap
      num[j], num[j+1] = num[j+1], num[j]

print(num)
