print("Enter the word to verify:")
word = input()
print(f"Checking if {word} is palindrome")
print("-------------------------------------------------------------------------------")
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")