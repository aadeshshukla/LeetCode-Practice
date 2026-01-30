# right angle triangle star pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#mirrored right angle triangle star pattern
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# equilateral triangle star pattern
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# diamond star pattern
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

    # square star pattern
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()
# hollow square star pattern
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# right arrow star pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# left arrow star pattern
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# hourglass star pattern
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
    

