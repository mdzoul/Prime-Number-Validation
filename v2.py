# Prime Number Checker v2
# Update iteration of another way to check
# Included 1 and 2 to be checked as prime numbers as well
def prime_checker(number):
    if number == 1 or number == 2:
        print("It is a prime number.")

    for i in range(2, number):
        if i + 1 == number:
            print("It's a prime number.")
        elif number % i == 0:
            print("It's not a prime number.")
            break
        elif number % i != 0:
            continue

n = int(input("Check this number: "))
prime_checker(number=n)