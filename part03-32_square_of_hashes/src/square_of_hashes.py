# Write your solution here
def hash_square(number):
  index = 1
  while index <= number:
    print('#'*number)
    index = index + 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)