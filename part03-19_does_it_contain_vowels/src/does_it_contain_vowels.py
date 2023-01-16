# Write your solution here
# vowels = ['a', 'e', 'o']
# a string and a list of strings is treated the same in python
# below is preferable
vowels = "aeo"

word = input("Please type in a string: ")

for i in vowels:
  if i in word:
    print(f"{i} found")
  else:
    print(f"{i} not found")


# suggested answer
# string = input("Please type in a string: ")
# vowels = "aeo"
# index = 0

# while index < len(vowels):
#     vowel = vowels[index]
#     if vowel in string:
#         print(vowel, "found")
#     else:
#         print(vowel, "not found")
#     index += 1