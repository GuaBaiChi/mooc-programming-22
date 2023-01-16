# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = 0

while index < len(word) - 2:
  if word[index] == character:
    print(word[index:index+3])
  index = index + 1


# suggested solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = 0

while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1


# while index < len(word) - 2:
# while index + 3 <= len(word):