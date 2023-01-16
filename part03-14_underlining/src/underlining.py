# Write your solution here


while True:
  phrase = input("Please type in a string: ")
  if phrase == "":
    break
  else:
    print()
    print(phrase)
    print(len(phrase)*"-")


# suggested solution
# while True:
#     string = input("Please type in a string: ")
#     if string == "":
#         break
#     print(string)
#     print(len(string) * "-")