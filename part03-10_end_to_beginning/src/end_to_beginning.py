# Write your solution here


word = input("Please type in a string: ")
counter = len(word)-1
# remember array index starts at 0.
# so for abc, length is '2'

while counter >= 0:
  print(word[counter])
  counter = counter - 1
  # counter will go from
  # word[2]
  # word[1]
  # word[0]



# alternate try 1
# word = input("Please type in a string: ")
# drow = word[::-1]
# for i in drow:
#   print(i)

# suggested answer
# word = input("Please type in a string: ")
# index = -1
# while index >= -len(word):
#     print(word[index])
#     index -= 1

# attempt 1
# word = input("Please type in a string: ")
# counter = len(word)-1
# while counter >= 0:
#   print(word[counter])
#   counter = counter - 1