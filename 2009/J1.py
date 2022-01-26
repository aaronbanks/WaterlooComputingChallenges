def main():

    book_number = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
    one_three_sum = 0

    for digit in range(3):
        book_number.append(int(input("Digit 11?")))

    alternator = True

    for digit in book_number:
        alternator = not alternator

        if alternator == True:
            one_three_sum += digit * 3

        else:
            one_three_sum += digit

    print(f"The 1-3 sum is {one_three_sum}")


main()
