# Write your solution here

num = print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
mean = 0
positive = 0
negative = 0

while True:
  num = int(input("Number: "))
  if num == 0:
    break
  else:
    count = count + 1
    sum = sum + num
    mean =  sum/count
    if num > 0:
      positive = positive + 1
    if num < 0:
      negative = negative + 1

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")