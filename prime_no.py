import math

x = int(input("Enter a number: "))

if x < 2:
    print("Entered number is not acceptable")
else:
    is_prime = True  # Assume the number is prime
    for i in range(2, int(math.sqrt(x)) + 1):  # Check divisibility from 2 to sqrt(x)
        if x % i == 0:
            is_prime = False  # If divisible, it's not prime
            break  # Exit loop early

    if is_prime:
        print("Entered Number is prime")
    else:
        print("Entered Number is not prime")