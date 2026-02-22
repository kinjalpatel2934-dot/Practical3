# Star Pyramid

rows = 5

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()





# Alphabet Inverted Pyramid

for i in range(rows,0,-1):

    ch='A'

    for j in range(i):

        print(ch,end=" ")

        ch=chr(ord(ch)+1)

    print()