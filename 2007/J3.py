def main():

    cases_opened = int(input())

    list_of_values_eliminated = []

    set_of_briefcase_values = {
        100,
        500,
        1000,
        5000,
        10000,
        25000,
        50000,
        100000,
        500000,
        1000000,
    }

    for cases in range(cases_opened):
        list_of_values_eliminated.append(input())

    bankers_offer = input()

    for value in list_of_values_eliminated:

        if value == "1":
            set_of_briefcase_values.remove(100)
        elif value == "2":
            set_of_briefcase_values.remove(500)
        elif value == "3":
            set_of_briefcase_values.remove(1000)
        elif value == "4":
            set_of_briefcase_values.remove(5000)
        elif value == "5":
            set_of_briefcase_values.remove(10000)
        elif value == "6":
            set_of_briefcase_values.remove(25000)
        elif value == "7":
            set_of_briefcase_values.remove(50000)
        elif value == "8":
            set_of_briefcase_values.remove(100000)
        elif value == "9":
            set_of_briefcase_values.remove(500000)
        elif value == "10":
            set_of_briefcase_values.remove(1000000)

    average_of_remaining = (sum(set_of_briefcase_values)) / (10 - cases_opened)

    if average_of_remaining < float(bankers_offer):
        print("deal")
    else:
        print("no deal")


main()
