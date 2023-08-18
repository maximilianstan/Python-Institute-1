income = float(input("Enter the annual income: "))

#
# Write your code here.
#

if income <= 85528:
    tax = income * .18 - 556.02
else:
    tax = 14839.02
    surplus = income - 85528
    surplusTax = surplus * .32
    tax = tax + surplusTax

if tax <= 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
