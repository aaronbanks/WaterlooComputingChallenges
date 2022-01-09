def main():

    input_lines = []

    while True:
        current_line_input = input()

        if current_line_input == "halt":
            break

        input_lines.append(current_line_input)

    for line in input_lines:
        current_key = 1

        total_seconds_used = 0

        for character in line:

#KEYPAD 2
            if character == "a":
                if current_key == 2:
                    total_seconds_used += 2
                current_key = 2
                total_seconds_used += 1

            if character == "b":
                if current_key == 2:
                    total_seconds_used += 2
                current_key = 2
                total_seconds_used += 2

            if character == "c":
                if current_key == 2:
                    total_seconds_used += 2
                current_key = 2
                total_seconds_used += 3

#KEYPAD 3
            if character == "d":
                if current_key == 3:
                    total_seconds_used += 2
                current_key = 3
                total_seconds_used += 1

            if character == "e":
                if current_key == 3:
                    total_seconds_used += 2
                current_key = 3
                total_seconds_used += 2

            if character == "f":
                if current_key == 3:
                    total_seconds_used += 2
                current_key = 3
                total_seconds_used += 3

#KEYPAD 4
            if character == "g":
                if current_key == 4:
                    total_seconds_used += 2
                current_key = 4
                total_seconds_used += 1

            if character == "h":
                if current_key == 4:
                    total_seconds_used += 2
                current_key = 4
                total_seconds_used += 2

            if character == "l":
                if current_key == 4:
                    total_seconds_used += 2
                current_key = 4
                total_seconds_used += 3

#KEYPAD 5
            if character == "j":
                if current_key == 5:
                    total_seconds_used += 2
                current_key = 5
                total_seconds_used += 1

            if character == "k":
                if current_key == 5:
                    total_seconds_used += 2
                current_key = 5
                total_seconds_used += 2

            if character == "i":
                if current_key == 5:
                    total_seconds_used += 2
                current_key = 5
                total_seconds_used += 3

#KEYPAD 6
            if character == "m":
                if current_key == 6:
                    total_seconds_used += 2
                current_key = 6
                total_seconds_used += 1

            if character == "n":
                if current_key == 6:
                    total_seconds_used += 2
                current_key = 6
                total_seconds_used += 2

            if character == "o":
                if current_key == 6:
                    total_seconds_used += 2
                current_key = 6
                total_seconds_used += 3

#KEYPAD 7
            if character == "p":
                if current_key == 7:
                    total_seconds_used += 2
                current_key = 7
                total_seconds_used += 1

            if character == "q":
                if current_key == 7:
                    total_seconds_used += 2
                current_key = 7
                total_seconds_used += 2

            if character == "r":
                if current_key == 7:
                    total_seconds_used += 2
                current_key = 7
                total_seconds_used += 3

            if character == "s":
                if current_key == 7:
                    total_seconds_used += 2
                current_key = 7
                total_seconds_used += 4

#KEYPAD 8
            if character == "t":
                if current_key == 8:
                    total_seconds_used += 2
                current_key = 8
                total_seconds_used += 1

            if character == "u":
                if current_key == 8:
                    total_seconds_used += 2
                current_key = 8
                total_seconds_used += 2

            if character == "v":
                if current_key == 8:
                    total_seconds_used += 2
                current_key = 8
                total_seconds_used += 3                              

#KEYPAD 9
            if character == "w":
                if current_key == 9:
                    total_seconds_used += 2
                current_key = 9
                total_seconds_used += 1

            if character == "x":
                if current_key == 9:
                    total_seconds_used += 2
                current_key = 9
                total_seconds_used += 2

            if character == "y":
                if current_key == 9:
                    total_seconds_used += 2
                current_key = 9
                total_seconds_used += 3

            if character == "z":
                if current_key == 9:
                    total_seconds_used += 2
                current_key = 9
                total_seconds_used += 4                                          

        print(f"{total_seconds_used}")
main()