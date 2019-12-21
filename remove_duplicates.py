numbers = [4,7,9,8,6,4,2,4,6,5]
numbers.sort()
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)