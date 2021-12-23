def main():

    with open("S1_J3_INPUT.txt") as input_file:
        input_lines = input_file.readlines()

        inverted_line = ""
        location = ""
        print_line = False

        for line in reversed(input_lines):

            clean_line = line.strip("\n")

            if clean_line == "SCHOOL":
                continue

            if clean_line != "L" and clean_line != "R":
                location = clean_line

            if print_line == True:
                print(f"Turn {inverted_line} onto {location} street.")
                print_line = False

            if clean_line == "R":
                inverted_line = "LEFT"
                print_line = True

            elif clean_line == "L":
                inverted_line = "RIGHT"
                print_line = True

        print(f"Turn {inverted_line} into your HOME.")


main()
