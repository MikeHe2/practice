# print simple text
print('"Programming is like building a multilingual puzzle')


# print var and text
number = 98
print(f"{number} Battery Street")

# print float with 2 digits
number = 3.141673234
print(f"Float: {number:.2f}")

# print 3 times a string
str = "Holberton School"
print(str * 3)
print(str[0:9])

# print 2 strings concatenated
str1 = "Holberton"
str2 = "School"
print(f"Welcome to {str1} {str2}!")

# print specific letters of a string
word = "Chancleta"
first_3 = word[0:3]
last_2 = word[-2:]
middle_word = word[1:-1]

print(word)
print(f"First 3 letters of {word} are: {first_3}")
print(f"Last 2 letters of {word} are: {last_2}")
print(f"Middle letters of {word} are: {middle_word}")