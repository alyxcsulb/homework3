# option 1

# triangle a
print("Triangle A:")
rows = 10
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=" ")
    print("\r")

# triangle b
print("\nTriangle B:")
rows = 10
for i in range(rows+1, 0, -1):
    for j in range(0, i-1):
        print("*", end=" ")
    print(" ")

# triangle c
print("\nTriangle C:")
rows = 10
for i in range(rows, 0, -1):
    for j in range(rows-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# triangle d
print("\nTriangle D:")
rows = 10
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print("")


