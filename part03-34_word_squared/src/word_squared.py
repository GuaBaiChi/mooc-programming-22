# Write your solution here
def squared(word, size):
    index = 0
    row = ""
    while index < size * size:
        if index > 0 and index % size == 0:
            print(row)
            row = ""
        row += word[index % len(word)]
        index = index + 1
    print(row)

# Testing the function
if __name__ == "__main__":
    squared("word", 3)