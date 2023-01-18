# Write your solution here

number = int(input("Please type in a number: "))
index = 1

while index <= number:
  if index+1 <= number:
    print(index+1)
  print(index)
  index = index + 2


# Suggested answer
number = int(input("Please type in a number: "))
index = 1

while index+1 <= number:
    print(index+1)
    print(index)
    index += 2

if index <= number:
    print(index)