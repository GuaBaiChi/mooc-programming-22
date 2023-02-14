# Write your solution here

def sum_of_positives(a_list):
  sum = 0
  for i in a_list:
    if i > 0:
      sum = sum + i
  return sum


if __name__ == "__main__":
  sum_of_positives([0, 1, 2, 3])