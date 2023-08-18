secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Enter the magic number:"))
while number != secret_number:
    print("Ha Ha! You're stuck in my loop!")
    number = int(input("Enter the magic number:"))
else:
    print("Well done, muggle! You are free now.")
