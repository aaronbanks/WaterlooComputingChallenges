def main():
    character_grid = [
        ["A", "G", "M", "S", "Y"],
        ["B", "H", "N", "T", "Z"],
        ["C", "I", "O", "U", " "],
        ["D", "J", "P", "V", "-"],
        ["E", "K", "Q", "W", "."],
        ["F", "L", "R", "X", "!"],
    ]

    input_text = input() + "!"
    total_moves = 0
    current_location = [0, 0]

    for character in input_text:

        for x_coordinate in range(6):
            for y_coordinate in range(5):

                if character_grid[x_coordinate][y_coordinate] == character:
                    total_moves += max(
                        x_coordinate - current_location[0],
                        current_location[0] - x_coordinate,
                    )
                    total_moves += max(
                        y_coordinate - current_location[1],
                        current_location[1] - y_coordinate,
                    )

                    current_location[0] = x_coordinate
                    current_location[1] = y_coordinate

                    print(total_moves)

    print(total_moves)


main()
