line = input()
for char in line:
    if not char.isalpha():
        break
    print("vowel" if char in "aeiou" else "consonant")
