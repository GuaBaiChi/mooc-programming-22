# Write your solution here

number = int(input("Pleae type in a number: "))

i = 1

while i <= number:
  j = 1
  while j <= number:
    print(f"{i} x {j} = {i*j}")
    j = j + 1
  i = i + 1


# suggested solution
# number = int(input("Please type in a number: "))
# counter1 = 1

# while counter1 <= number:
#     counter2 = 1
#     while counter2 <= number:
#         print(f"{counter1} x {counter2} = {counter1*counter2}")
#         counter2 += 1
#     counter1 += 1