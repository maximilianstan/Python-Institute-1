def message(number):
    print("Enter a number:", number)


message(2)


def message(number):
    print("Enter a number:", number)


number = 1234
message(1)
print(number)


def message(what, number):
    print("Enter", what, "number", number)


# invoke the function
message(2, 4)


def message(what, number):
    print("Enter", what, "number", number)


message("telephone", 11)
message("price", 5)
message("number", "number")


def my_function(a, b, c):
    print(a, b, c)


my_function(1, 2, 3)


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
adding(1, 2, 3)
