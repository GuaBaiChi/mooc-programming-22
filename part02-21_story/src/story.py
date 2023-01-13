# Write your solution here

story = ""
lastword = ""

while True:
  word = input("Please type in a word: ")
  if word == "end" or word == lastword:
    print(story)
    break
  else:
    lastword = word
    story = story + word + " "


# suggested solution
# story = ""
# previous = ""

# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word == previous:
#         break
#     story += word + " "
#     previous = word
# print(story)