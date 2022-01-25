def main():

    set_of_motel_locations = {
        0,
        990,
        1010,
        1970,
        2030,
        2940,
        3060,
        3930,
        4060,
        4970,
        5030,
        5990,
        6010,
        7000,
    }

    minimum_to_travel = int(input())

    maximum_to_Travel = int(input())

    number_of_motels_added = int(input())

    for motel in range(number_of_motels_added):
        set_of_motel_locations.add(int(input()))

    distance_traveled = 0
    route_taken = []

    possible_routes = route_finder(
        distance_traveled,
        minimum_to_travel,
        maximum_to_Travel,
        set_of_motel_locations,
        route_taken,
    )

    print(f"Output: {possible_routes}")


def route_finder(distance, mini, maxi, motels, route_taken):
    possible_routes_found = 0

    while distance < 7000:
        option_found = False

        route_taken_copy = route_taken.copy()

        for motel in motels:
            if motel >= (distance + mini) and motel <= (distance + maxi):

                if option_found == True:
                    #APPEND BEFORE
                    possible_routes_found += route_finder(
                        motel, mini, maxi, motels, route_taken_copy.append(motel)
                    )

                option_found = True

                route_taken.append(motel)
                print(f"{motel}")

                if motel == 7000:
                    possible_routes_found += 1
                    print(f"Route taken: {route_taken}")

                new_distance = motel
        distance = new_distance

        if option_found == False:
            return 0

    return possible_routes_found


main()
