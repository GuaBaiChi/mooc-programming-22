# Write your solution here
phrase = input("Please type in a string: ")
phraselength = len(phrase)

starphrase = (20 - phraselength) * "*"
print(starphrase+phrase)