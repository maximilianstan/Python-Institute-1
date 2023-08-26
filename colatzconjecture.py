c0 = int(input("Insert a number here: "))
if c0 > 1:
    print("Use a non-negative non-zero number.")


steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    print(c0)
    steps = steps + 1

print("Total number of steps: ", steps)
