# Write your solution here
# You can test your function by calling it within the following block
# printing trees like in the java one

def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i = i + 1
    print(" " * (height - 1) + "*")

if __name__ == "__main__":
    spruce(5)