# Practical 3 - Even Numbers Between 1 to 100

even_numbers = []

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)

print("Even Numbers between 1 to 100:")
print(even_numbers)

print("Minimum Even Number:", min(even_numbers))
print("Maximum Even Number:", max(even_numbers))
print("Sum of Even Numbers:", sum(even_numbers))
