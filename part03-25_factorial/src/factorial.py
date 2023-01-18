# Write your solution here

factorial = 1

while True:
  number = int(input("Please type in a number: "))
  if number <= 0:
    print("Thanks and bye!")
    break
  index = 1
  while index <= number:
    factorial = factorial * index
    index = index + 1
  print(f"The factorial of the number {number} is {factorial}")
  factorial = 1
