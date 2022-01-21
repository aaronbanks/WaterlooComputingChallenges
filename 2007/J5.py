def main():

    set_of_motel_locations = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000}

    minimum_to_travel = int(input())

    maximum_to_Travel = int(input())

    number_of_motels_added = int(input())

    for motel in range(number_of_motels_added):
        set_of_motel_locations.add(input())

    number_of_possible_routes = 0

    distance_traveled = 0
    possible_routes = 0
    set_of_routes = {}

    current_trip = []


    def route_finder(distance, mini, maxi, motels, trip_so_far):
        while distance < 7000:
            option_found = False
            for motel in motels:
                if motel >= (distance + mini) and motel <= (distance + maxi):
                    if option_found == True:
                        route_finder(motel, mini, maxi, motels, trip_so_far.append(motel))

                    distance = motel
                    option_found = True
                    trip_so_far.append(motel)






main()