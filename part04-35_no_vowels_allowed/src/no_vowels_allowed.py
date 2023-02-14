# Write your solution here
def no_vowels(my_string: str):
  vowels = "aeiou"
  result = ""

  for letter in my_string:
    if letter not in vowels:
      result = result + letter
  return result


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

