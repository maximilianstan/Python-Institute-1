greutate = int(input("Weight: "))
tipologie = input("(K)g or (L)bs: ")

if tipologie == "k":
    print("Your weight in kg is", greutate)
elif tipologie == "K":
    print("Your weight in kg is", greutate)
elif tipologie == "L":
    print("Your weight in kg is", greutate * 0.45)
elif tipologie == "l":
    print("Your weight in kg is", greutate * 0.45)
else:
    print("Esti prost sau nu ai inteles ce am intrebat.")
