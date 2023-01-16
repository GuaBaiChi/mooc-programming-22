# Write your solution here
# word = input("Please type in a word: ")
# character = input("Please type in a character: ")
# index = 0

# while index < len(word)-2:
#   if word[index] == character:
#     print(word[index:index+3])
#     break
#   index = index + 1


# suggested solution
# print out three characters or nothing
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(word[index:index+3])
