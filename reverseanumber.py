x =int(input("Enter a number:"))

reverse = 0
while x>0:
    y = x % 10
    reverse = reverse * 10 + y
    x = x // 10
print("The reverse of the number is:", reverse)