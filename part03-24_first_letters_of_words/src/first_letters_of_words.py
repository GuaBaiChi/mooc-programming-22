# Write your solution here

# attempt 1
# phrase = input("Please type in a sentence: ")
# phraselength = len(phrase)
# index = 0

# if phraselength != 0:
#   print(phrase[0])
#   while index < phraselength:
#     if phrase[index] == " ":
#       print(phrase[index+1])
#     index = index + 1



# model solution
sentence = input("Please type in a sentence: ")
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence

# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1