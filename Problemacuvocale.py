wordWithoutVovels = ""
userWord = input("Enter a word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter in "AEIOU":
        continue
    wordWithoutVovels = wordWithoutVovels + letter

print(wordWithoutVovels)
