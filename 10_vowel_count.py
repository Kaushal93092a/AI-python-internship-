# Program 10: Count vowels in a text
text = input("Enter a word or sentence: ").lower()
vowels = "aeiou"
count = 0
for character in text:
    if character in vowels:
        count += 1
print("Number of vowels:", count)
