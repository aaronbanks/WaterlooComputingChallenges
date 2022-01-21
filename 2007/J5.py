def main():

    set_of_motel_locations = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000}

    minimum_to_travel = int(input())

    maximum_to_Travel = int(input())

    number_of_motels_added = int(input())

    for motel in range(number_of_motels_added):
        set_of_motel_locations.add(int(input()))

    distance_traveled = 0

    possible_routes = route_finder(distance_traveled, minimum_to_travel, maximum_to_Travel, set_of_motel_locations)

    print(f"Output: {possible_routes}")

def route_finder(distance, mini, maxi, motels):
    possible_routes_found = 0

    while distance < 7000:
        option_found = False

        for motel in motels:
            if motel >= (distance + mini) and motel <= (distance + maxi):

                if option_found == True:
                    possible_routes_found += route_finder(motel, mini, maxi, motels)

                option_found = True

                if motel == 7000:
                    possible_routes_found += 1
                distance = motel

        if option_found == False:
            return 0

    return possible_routes_found
main()