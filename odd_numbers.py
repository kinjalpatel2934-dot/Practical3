# Find all odd numbers between 1 to 100

odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print("List of Odd Numbers:", odd_numbers)
print("Minimum Odd Number:", min(odd_numbers))
print("Maximum Odd Number:", max(odd_numbers))
print("Sum of Odd Numbers:", sum(odd_numbers))

# Even Numbers between 1 to 50

even_numbers = []

for i in range(1,51):
    
    if i % 2 == 0:
        
        even_numbers.append(i)


print("Even Numbers List:")
print(even_numbers)


print("Three Minimum Even Numbers:")
print(even_numbers[:3])


print("Three Maximum Even Numbers:")
print(even_numbers[-3:])


average = sum(even_numbers) / len(even_numbers)

print("Average:")
print(average)