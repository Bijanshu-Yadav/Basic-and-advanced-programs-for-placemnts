def sorting():
    numbers = [23,56,34,67,12,0,56,45,34,45,-99,-101]
    di = {
        "name": "Sorting",
        "Work": "to sort the list",
        "and": "to print the sorted list"
    }
    print("Original list:", numbers)
    print("Original list:", di)
    
    sorteded = sorted(numbers, key = abs)
    dic =sorted(di)
    print("Sorted " ,sorteded,di)
sort = sorting()
print(sort)