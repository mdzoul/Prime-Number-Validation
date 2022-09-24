# This script finds if a number is prime or not
user_input = int(input("What number are you checking?: "))

for number in range(2, user_input):
    if number == user_input - 1:
        print(f"\nYes. {user_input} is a prime number.")
    elif user_input % number != 0:
        continue
    else:
        print(f"\nNo. {user_input} is not a prime number.")
        break