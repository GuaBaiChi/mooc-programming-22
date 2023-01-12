# Write your solution here

# 1
# initial try and the "stock solution"
# name = input("Please type in your name: ")

# if name == "Morty" or name == "Ferdie":
#   print("I think you might be one of Mickey Mouse's nephews.")
# elif name == "Huey" or name == "Dewey" or name == "Louie":
#   print("I think you might be one of Donald Duck's nephews.")
# else:
#   print("You're not a nephew of any character I know of.")

# 2 
# first varient
# name = input("Please type in your name: ")

# if name in ["Morty", "Ferdie"]:
#   print("I think you might be one of Mickey Mouse's nephews.")
# elif name in ["Huey", "Dewey", "Louie"]:
#   print("I think you might be one of Donald Duck's nephews.")
# else:
#   print("You're not a nephew of any character I know of.")

# 3
# last one
name = input("Please type in your name: ")
mickeys_nephews = ["Morty", "Ferdie"]
donalds_nephews = ["Huey", "Dewey", "Louie"]

if name in mickeys_nephews:
  print("I think you might be one of Mickey Mouse's nephews.")
elif name in donalds_nephews:
  print("I think you might be one of Donald Duck's nephews.")
else:
  print("You're not a nephew of any character I know of.")

  