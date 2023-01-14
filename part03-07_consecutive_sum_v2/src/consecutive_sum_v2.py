# Write your solution here

limit = int(input("Limit: "))
sum = 1
counter = 1
consecutive = "1"

while sum < limit:
  counter = counter + 1
  sum = sum + counter
  consecutive = consecutive + f" + {counter}"
print(f"The consecutive sum: {consecutive} = {sum}")
