def main():

starting_coordinate = ()

starting_coordinate = (1, 1)

set_of_coordinates_visited = set()
set_of_closed_coordinates = set()

width_of_outline = input("Enter the width of the outline:")
height_of_outline = input("Enter the height of the outline:")

width_of_cutout = input("Enter the width of the cutouts:")
height_of_cutout = input("Enter the heigth of the cutouts:")

size_of_cutouts = width_of_cutout * height_of_cutout
number_of_closed_coordinates = size_of_cutouts * 4

cutout_tracker = 1
cutout_remaining = 6

for squares in number_of_closed_coordinates:
    cutout_remaining -= 1
    if cutout_remaining == 0:
        cutout_remaining = 5
        cutout_tracker +1

    if cutout_tracker = 1:

    if cutout_tracker = 2:

    if cutout_tracker = 3:

    if cutout_tracker = 4:




main()
