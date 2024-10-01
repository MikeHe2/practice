def two_sum(array, k):
    for n in array:
        result = k - n

        if result in array:
            return True
    return False

array = [10, 15, 3, 7]
k = 222
print(two_sum(array, k))
