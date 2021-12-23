def main():
    lower_limit = int(input("Enter lower limit of range:"))
    upper_limit = int(input("Enter upper limit of range:")) + 1

    rsa_numbers_in_range = 0

    for number in range(lower_limit, upper_limit):
        if rsa_check(number) == True:
            rsa_numbers_in_range += 1

    print(
        f"The number of RSA number between {lower_limit} and {upper_limit - 1} is {rsa_numbers_in_range}"
    )


def rsa_check(number):
    total_even_divisors = 0

    for numbers in range(1, number + 1):
        if number % numbers == 0:
            total_even_divisors += 1

    if total_even_divisors == 4:
        return True

    else:
        return False


main()
