# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
math = input("Operation: ")

if math == "add":
  print(f"{num1} + {num2} = {num1+num2}")

if math == "multiply":
  print(f"{num1} * {num2} = {num1*num2}")

if math == "subtract":
  print(f"{num1} - {num2} = {num1-num2}")