# Write your solution here

wordlist = []

while True:
  wordlistlength = len(wordlist)
  word = input("Word: ")
  if word in wordlist:
    print(f"You typed in {wordlistlength} different words")
    break
  wordlist.append(word)