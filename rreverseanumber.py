x = int(input("Enter a number"))

reverse = 0
for i in range(0, len(str(x))):
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10
print("Reverse of the number is:", reverse)