beatles = []
# step 1
print("Step 1:", beatles)

# step 2
print("Step 2:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 3
for member in range(2):
    beatlename = input("New Beatle Name :")
    beatles.append(beatlename)

print("Step 3:", beatles)

# step 4
del beatles[3:5]

print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))
