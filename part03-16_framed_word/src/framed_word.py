# Write your solution here

word = input("Word: ")
line = 30*"*"
wordlength = len(word)

before = (28 - wordlength) // 2
after = before

if wordlength % 2 != 0:
  after = before + 1

center = (f"*{(before * ' ')}{word}{(after * ' ')}*")
# remember inside an f-string don't use "", must use ''


print(line)
print(center)
print(line)


# # suggested solution
# word = input("Word: ")
# spaces_at_start = (28 - len(word)) // 2
# spaces_at_end = spaces_at_start

# if len(word) % 2 != 0:
#     spaces_at_end += 1

# print("*" * 30)
# print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
# print("*" * 30)

 