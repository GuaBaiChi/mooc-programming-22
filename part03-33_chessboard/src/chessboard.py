# # Write your solution here\

# suggested solution
def chessboard(size):
  i = 0

  while i < size:
    if i % 2 == 0:
        row = "10"*size
    else:
      row = "01"*size
    # Remove extra characters at the end of the row
    print(row[0:size])
    i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)