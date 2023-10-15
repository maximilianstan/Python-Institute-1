my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

empty_tuple = ()
print(type(empty_tuple))

one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.

my_tuple_1 = 1,
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>

# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)

my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
# my_tuple[2] = "guitar"   The TypeError exception will be raised.

my_tuple = 1, 2, 3,
del my_tuple
# print(my_tuple)    NameError: name 'my_tuple' is not defined

# You can also create a tuple using a Python built-in function called tuple().
# This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list))    # outputs: <class 'list'>
