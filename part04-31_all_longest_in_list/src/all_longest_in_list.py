# Write your solution here
# def all_the_longest(my_list):
#   longest = 0
#   newList = []

#   for i in my_list:
#     if len(i) > longest:
#       longest = len(i)
  
#   for i in my_list:
#     if len(i) == longest:
#       newList.append(i)
  
#   return newList

# suggested solution
def all_the_longest(names: list):  
  result = []

  for name in names:
    if result == [] or len(name) > len(result[0]):
        result = [name]
    elif len(name) == len(result[0]):
        result.append(name)

  return result

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)


# if __name__ == "__main__":
#   names = ["first", "second", "fourth", "eleventh"]

#   result = all_the_longest(names)
#   print(result) # ['eleventh']