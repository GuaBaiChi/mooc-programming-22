# Copy here code of line function from previous exercise

def square_of_hashes(size):
    # You should call function line here with proper parameters
    index = 1
    while index <= size:
        line(size, "#")
        index = index + 1

def line(size, character):
  if character == "":
    character = "*"
  print(character[0] * size)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)