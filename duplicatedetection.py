def duplicate():
    ids = [101, 205, 101, 309, 205, 410, 512, 309]
    seen = {}
    for i in ids:
        if i in seen:
            seen[i] +=1
        else:
            seen[i] = 1
    return seen
duplicated = duplicate()
print(duplicated)