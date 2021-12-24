import copy

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

    current_coordinates = copy.copy(starting_coordinate)
    set_of_coordinates_visited = set()

    def attempt_to_move_right():

        nonlocal current_coordinates
        nonlocal set_of_coordinates_visited

        move_right = (current_coordinates[0] + 1, current_coordinates[1])

        if (
            move_right
            not in set_of_coordinates_visited
            and move_right
            not in set_of_cutout_coordinates
            and current_coordinates[0] < width_of_outline
        ):
            current_coordinates = move_right
            set_of_coordinates_visited.add(current_coordinates)
            print("R")
            return True

    def attempt_to_move_left():

        nonlocal current_coordinates
        nonlocal set_of_coordinates_visited

        move_left = (current_coordinates[0] - 1, current_coordinates[1])

        if (
            move_left
            not in set_of_coordinates_visited
            and move_left
            not in set_of_cutout_coordinates
            and current_coordinates[0] > 1
        ):
            current_coordinates = move_left
            set_of_coordinates_visited.add(current_coordinates)
            print("L")
            return True

    def attempt_to_move_down():
        nonlocal current_coordinates
        nonlocal set_of_coordinates_visited

        move_down = (current_coordinates[0], current_coordinates[1] + 1)

        if (
            move_down
            not in set_of_coordinates_visited
            and move_down
            not in set_of_cutout_coordinates
            and current_coordinates[1] < height_of_outline
        ):
            current_coordinates = move_down
            set_of_coordinates_visited.add(current_coordinates)
            print("D")
            return True

    def attempt_to_move_up():
        nonlocal current_coordinates
        nonlocal set_of_coordinates_visited

        move_up = (current_coordinates[0], current_coordinates[1] - 1)

        if (
            move_up
            not in set_of_coordinates_visited
            and move_up
            not in set_of_cutout_coordinates
            and current_coordinates[1] > 1
        ):
            current_coordinates = move_up
            set_of_coordinates_visited.add(current_coordinates)
            print("U")
            final_location = current_coordinates
            return True


    for steps in range(steps_to_take):
        print(current_coordinates)
        set_of_coordinates_visited.add(current_coordinates)

        if current_coordinates[0] > width_of_outline / 2 and current_coordinates[1] <= height_of_outline / 2:
            if attempt_to_move_right() == True:
                pass
            else:
                attempt_to_move_down()

        elif current_coordinates[0] > width_of_outline / 2 and current_coordinates[1] > height_of_outline / 2:
            if attempt_to_move_down() == True:
                pass
            else:
                attempt_to_move_left()

        elif current_coordinates[0] <= width_of_outline / 2 and current_coordinates[1] > height_of_outline / 2:
            if attempt_to_move_left() == True:
                pass
            else:
                attempt_to_move_up()

        elif current_coordinates[0] <= width_of_outline / 2 and current_coordinates[1] <= height_of_outline / 2:
            if attempt_to_move_up() == True:
                pass
            else:
                attempt_to_move_right()

    return current_coordinates

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

    print(closed_coordinates)
    return closed_coordinates

main()
