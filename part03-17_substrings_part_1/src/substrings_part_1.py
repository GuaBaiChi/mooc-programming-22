# Write your solution here

# suggested solution
# word = input("Please type in a string: ")
# index = 0
# wordlength = len(word)
# while index <= wordlength:
#   print(word[0:index])
#   index = index + 1


#2
# attempt 2, works
# word = input("Please type in a string: ")
# start = ""
# index = 0

# while index < len(word):
#   start = start + word[index]
#   print(start)
#   index = index + 1


# 1
# can a for loop work. yes
word = input("Please type in a string: ")
for i in range(1, len(word) + 1):
  print(word[0:i])
