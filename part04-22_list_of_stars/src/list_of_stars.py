# Write your solution here

# def list_of_stars(your_list : list):
#   size = len(your_list)
#   i = 0
#   while i < size:
#     print("*" * your_list[i])
#     i = i + 1


def list_of_stars(your_list: list):
  for i in your_list:
    print("*" * i)

if __name__ == "__main__":
  list_of_stars([3, 7, 1, 1, 2])