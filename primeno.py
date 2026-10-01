n = int(input("Enter the number:"))

if n <2:
    print("Notprime")
else:
    is_prime = True

    for i in range(2,n):
        if n % i ==0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Notprime")