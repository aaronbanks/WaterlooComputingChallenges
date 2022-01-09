def main():

    calories_in_meal = burger() + side() + drink() + dessert()

    print(f"Your total Calorie count is {calories_in_meal}.")


def burger():
    while True:
        user_input = int(input("Please enter a burger choice:"))

        if user_input == 1:
            return 451

        elif user_input == 2:
            return 431

        elif user_input == 3:
            return 421

        elif user_input == 4:
            return 0

        else:
            print(
                "Invalid entry, please enter a number between 1-4 to indicate your order"
            )


def side():
    while True:
        user_input = int(input("Please enter a side order choice:"))

        if user_input == 1:
            return 100

        elif user_input == 2:
            return 57

        elif user_input == 3:
            return 70

        elif user_input == 4:
            return 0

        else:
            print(
                "Invalid entry, please enter a number between 1-4 to indicate your order"
            )


def drink():
    while True:
        user_input = int(input("Please enter a drink choice:"))

        if user_input == 1:
            return 130

        elif user_input == 2:
            return 160

        elif user_input == 3:
            return 118

        elif user_input == 4:
            return 0

        else:
            print(
                "Invalid entry, please enter a number between 1-4 to indicate your order"
            )


def dessert():
    while True:
        user_input = int(input("Please enter a desert choice:"))

        if user_input == 1:
            return 167

        elif user_input == 2:
            return 266

        elif user_input == 3:
            return 75

        elif user_input == 4:
            return 0

        else:
            print(
                "Invalid entry, please enter a number between 1-4 to indicate your order"
            )


main()
