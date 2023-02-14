# Write your solution here
list = []

while True:
  listlength = len(list)
  
  print(f"The list is now {list}")
  selection = input("a(d)d, (r)emove or e(x)it:")
  if selection == "d":
      item = listlength + 1
      list.append(item)
  elif selection == "r":
      list.pop(listlength - 1)
  elif selection == "x":
      break
    
print("Bye!")