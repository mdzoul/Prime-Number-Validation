# Prime Number Checker v3
# Apparently, this is the simplest way to check for prime numbers (just one line less than v2)
def prime_checker(number):
    if number == 1 or number == 2:
        print("It is a prime number.")
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It;s not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)