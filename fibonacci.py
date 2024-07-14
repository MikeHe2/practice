#!/usr/bin/python3


def fib(n):
    num1 = 0
    num2 = 1
    for i in range(n):
        sum = num2 + num1
        num1 = num2
        num2 = sum

    return num1


for x in range(10):
    print(fib(x))

