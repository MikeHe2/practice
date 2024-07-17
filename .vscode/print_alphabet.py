


for i in range(97, 123):
    if i != 101 and i != 113:
        print(f"{chr(i)}", end="")
        print("")
print("----------------------------------------------------")


for i in range(99):
    print(f"{i} = 0x{i:x}")
print("------------------------------------------------")



for i in range(100):
    if i != 99:
        print(f"{i}", end=", ")
    else:
        print(f"{i}")
        print("---------------------------------------------------")




for x in range (10):
    for y in range(10):
        if x != y and x < y:
            if  x == 8 and y == 9:
                print(f"{x}{y}")
            else:
                print(f"{x}{y}" , end=", ")
