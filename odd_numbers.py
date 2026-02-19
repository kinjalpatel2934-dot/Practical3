# Find all odd numbers between 1 to 100

odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print("List of Odd Numbers:", odd_numbers)
print("Minimum Odd Number:", min(odd_numbers))
print("Maximum Odd Number:", max(odd_numbers))
print("Sum of Odd Numbers:", sum(odd_numbers))
