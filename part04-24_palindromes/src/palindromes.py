# Write your solution here

def palindromes(word):
    return word == word[::-1]
    # this doesn't work
    # return word == reversed(word)

# suggested function
# def palindromes(word: str):
#     for i in range(len(word)//2):
#         if word[i] != word[len(word)-i-1]:
#             return False
#     return True


while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    print("that wasn't a palindrome")






# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
