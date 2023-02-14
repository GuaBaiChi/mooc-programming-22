# Write your solution here

numlist = []

while True:
  num = int(input("New item: "))
  if num == 0:
    break
  numlist.append(num)
  print(f"The list now: {numlist}")
  print(f"The list in order: {sorted(numlist)}")
print("Bye!")