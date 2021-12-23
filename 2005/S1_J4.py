import copy

#THIS PROGRAM PRODUCES THE CORRECT RESULT FOR SAMPLE INPUTS 1,3 AND 4, BUT INCORRECT FOR INPUT 2.

def main():

    top_left_coordinate = (1, 1)

    set_of_cutout_coordinates = set()

    width_of_outline = int(input("Enter the width of the outline:"))
    height_of_outline = int(input("Enter the height of the outline:"))

    width_of_cutout = int(input("Enter the width of the cutouts:"))
    height_of_cutout = int(input("Enter the heigth of the cutouts:"))

    steps_to_take = int(input("How many steps are you going to take?"))

    set_of_cutout_coordinates = set(
        calculate_cutout_coordinates(
            top_left_coordinate,
            width_of_outline,
            height_of_outline,
            width_of_cutout,
            height_of_cutout,
        )
    )

    print(set_of_cutout_coordinates)

    starting_coordinate = (top_left_coordinate[0] + width_of_cutout, 1)

    answer = walk_clockwise(
        starting_coordinate,
        width_of_outline,
        height_of_outline,
        steps_to_take,
        set_of_cutout_coordinates,
    )

    print(answer)


def walk_clockwise(
    starting_coordinate,
    width_of_outline,
    height_of_outline,
    steps_to_take,
    set_of_cutout_coordinates,
):

    current_coordinates = starting_coordinate
    set_of_coordinates_visited = set()
    final_location = ()

    for steps in range(steps_to_take):

        if (
            (current_coordinates[0] + 1, current_coordinates[1])
            not in set_of_coordinates_visited
            and (current_coordinates[0] + 1, current_coordinates[1])
            not in set_of_cutout_coordinates
            and current_coordinates[0] < width_of_outline
        ):
            current_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
            set_of_coordinates_visited.add(current_coordinates)


        elif (
            (current_coordinates[0], current_coordinates[1] + 1)
            not in set_of_coordinates_visited
            and (current_coordinates[0], current_coordinates[1] + 1)
            not in set_of_cutout_coordinates
            and current_coordinates[1] < height_of_outline
        ):
            current_coordinates = (current_coordinates[0], current_coordinates[1] + 1)
            set_of_coordinates_visited.add(current_coordinates)

        elif (
            (current_coordinates[0] - 1, current_coordinates[1])
            not in set_of_coordinates_visited
            and (current_coordinates[0] - 1, current_coordinates[1])
            not in set_of_cutout_coordinates
            and current_coordinates[0] > 1
        ):
            current_coordinates = (current_coordinates[0] - 1, current_coordinates[1])
            set_of_coordinates_visited.add(current_coordinates)

        elif (
            (current_coordinates[0], current_coordinates[1] - 1)
            not in set_of_coordinates_visited
            and (current_coordinates[0], current_coordinates[1] - 1)
            not in set_of_cutout_coordinates
            and current_coordinates[1] > 1
        ):
            current_coordinates = (current_coordinates[0], current_coordinates[1] - 1)
            set_of_coordinates_visited.add(current_coordinates)

        else:
            final_location = current_coordinates
            break

    final_location = current_coordinates
    return final_location

def calculate_cutout_coordinates(
    top_left_coordinate,
    width_of_outline,
    height_of_outline,
    width_of_cutout,
    height_of_cutout,
):

    size_of_cutouts = width_of_cutout * height_of_cutout
    number_of_closed_coordinates = size_of_cutouts * 4
    squares_in_cutout_remaining = copy.copy(size_of_cutouts) + 1
    current_cutout_tracker = 1
    row_number = 1
    row_location = 1

    closed_coordinates = []

    for squares in range(number_of_closed_coordinates):
        squares_in_cutout_remaining -= 1

        if squares_in_cutout_remaining == 0:
            squares_in_cutout_remaining = copy.copy(size_of_cutouts)
            current_cutout_tracker += 1
            row_number = 0

        if current_cutout_tracker == 1:
            if row_location > width_of_cutout:
                row_location = 1
                row_number += 1

            closed_coordinates.append(
                (
                    top_left_coordinate[0] + row_location - 1,
                    top_left_coordinate[1] + row_number - 1,
                )
            )
            row_location += 1

        elif current_cutout_tracker == 2:
            if row_location > width_of_cutout:
                row_location = 1
                row_number += 1

            closed_coordinates.append(
                (
                    width_of_outline - width_of_cutout + row_location,
                    top_left_coordinate[1] + row_number - 1,
                )
            )
            row_location += 1

        elif current_cutout_tracker == 3:
            if row_location > width_of_cutout:
                row_location = 1
                row_number += 1

            closed_coordinates.append(
                (
                    top_left_coordinate[0] + row_location - 1,
                    height_of_outline - height_of_cutout + row_number,
                )
            )
            row_location += 1

        elif current_cutout_tracker == 4:
            if row_location > width_of_cutout:
                row_location = 1
                row_number += 1

            closed_coordinates.append(
                (
                    width_of_outline - width_of_cutout + row_location,
                    height_of_outline - height_of_cutout + row_number,
                )
            )
            row_location += 1

    return closed_coordinates

main()
