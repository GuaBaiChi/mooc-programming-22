# Copy here code of line function from previous exercise

def box_of_hashes(height):
    # You should call function line here with proper parameters
    index = 1
    while index <= height:
        line(10, "#")
        index = index + 1

def line(size, character):
  if character == "":
    character = "*"
  print(character[0] * size)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
