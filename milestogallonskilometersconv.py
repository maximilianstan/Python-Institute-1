def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000 / 1609.344  #or miles = 62.1371
    gallons = liters / 3.785411784
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    kilometers = miles * 1609.344 / 1000
    km100 = kilometers / 100
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
