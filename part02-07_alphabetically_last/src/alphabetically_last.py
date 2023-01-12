# Write your solution here

first = input("Please tpe in the 1st word: ")
second = input("Please type in the 2nd word: ")

if first > second:
  print(f"{first} comes alphabetically last")
elif first < second:
    print(f"{second} comes alphabetically last")
else:
  print("You gave the same word twice.")