def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number.
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's nor, increment the factor by one
            factor += 1
    return "Done"

print("Welcome to ZED's Prime Factor Generator\n\n")
number = int(input("Enter the number: "))
print_prime_factors(number)
