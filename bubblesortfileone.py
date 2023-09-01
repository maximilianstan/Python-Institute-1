my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)



my_list = [1, 78, 645, 2, 53, 8, 71, 996, 995, 4, 750, 993, 10743, 95]
my_list.sort()
print(my_list)

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)
# output [1, 2, 3]
