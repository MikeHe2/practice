
import random
number = random.randint(-10000, 10000)
mas_facil = str(number)[-1]
if number >= 0:
    result = number % 10
else:
    result = number % -10

print(f"Más facil asi: {mas_facil}")

if result > 5:
    print(f"Last digit of {number} is {result} and is greater than 5")
elif result == 0:
    print(f"Last digit of {number} is {result} and is zero")
elif result <= 5:
    print(f"Last digit of {number} is {result} and is less than 6 and not 0")