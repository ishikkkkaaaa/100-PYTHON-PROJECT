def primeNumberChecker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a Prime Number!")
    else:
        print("Not a prime")


n = int(input("Check the number: "))
primeNumberChecker(number=n)
