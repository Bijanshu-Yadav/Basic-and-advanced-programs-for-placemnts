def counter():
    numbers = [1, 2, 2, 3, 1, 4, 2, 3]
    frequency = {}
    for i in numbers:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1
    return frequency
conub = counter()
print(conub)
