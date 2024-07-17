my_list = [1, 2, 3, 4, 5]
idx = 6
# for  i in range(len(idx)):
    # print(my_list[i])

if idx > len(my_list) -1:
    print("Out of range")
elif idx < 0:
    print("Is a negative number")
else:
    print(my_list[idx])