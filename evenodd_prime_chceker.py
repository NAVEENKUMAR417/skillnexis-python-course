number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

if is_prime(number):
    print("Prime")
else:
    print("Not Prime")