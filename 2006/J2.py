def main():
    number_of_ways_to_ten = 0

    sides_on_die_m = int(input("Enter m:"))

    sides_on_die_n = int(input("Enter n:"))

    for sides in range(1, sides_on_die_m + 1):
        for sidez in range(1, sides_on_die_n + 1):

            if sides + sidez == 10:
                number_of_ways_to_ten += 1

    print(f"There are {number_of_ways_to_ten} ways too get the sum 10.")


main()
