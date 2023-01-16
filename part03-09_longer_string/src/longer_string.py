# Write your solution here
word1 = input("Please type in string 1: ")
word2 = input("Please type in string 2: ")
word1len = len(word1)
word2len = len(word2)

if word1len > word2len:
  print(f"{word1} is longer")
elif word2len > word1len:
    print(f"{word2} is longer")
else:
  print("The strings are equally long")