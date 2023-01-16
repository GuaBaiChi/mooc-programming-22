# Write your solution here

# attempt 1
# word = input("Please type in a string: ")
# wordlength = len(word)
# index = -1
# sum = ""

# while index >= -wordlength:
#     sum = word[index] + sum
#     print(sum)
#     index = index - 1


# suggested solution
string = input("Please type in a string: ")
start = len(string) - 1

while start >= 0:
    print(string[start:])
    start = start - 1
