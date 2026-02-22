# Inverted Right Half Pyramid

rows = 6

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
n = 1

for i in range(1,6):
    for j in range(i):
        print(n, end=" ")
        n += 1
        if n > 9:
            n = 1
    print()