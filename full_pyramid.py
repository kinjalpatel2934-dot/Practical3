# Star Pyramid (Center)

rows = 5

for i in range(1, rows+1):

    # Print spaces (for center alignment)
    print(" " * (rows - i), end="")

    # Print stars
    for j in range(i):
        print("* ", end="")

    print()


# Alphabet Inverted Pyramid (Center)

letters = ["A","B","C","D","E"]

for i in range(5,0,-1):

    # Print spaces
    print(" " * (5 - i), end="")

    # Print alphabets
    for j in range(i):
        print(letters[j], end=" ")

    print()