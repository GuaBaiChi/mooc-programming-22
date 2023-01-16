# Write your solution here
word = input("Please type in a string: ")
second = word[1]
secondtolast = word[-2]


if second == secondtolast:
  print(f"The second and the second to last characters are {second}")
else:
  print("The second and the second to last characters are different")
