def main():

    trout_points = int(input())
    pike_points = int(input())
    pickerel_points = int(input())
    total_point_allowance = int(input())

    set_of_possible_catches = set()

    for trout in range(0, int(total_point_allowance / trout_points) + 1):
        for pike in range(int(total_point_allowance / pike_points) + 1):
            for pickerel in range(int(total_point_allowance / pickerel_points) + 1):

                if trout + pike + pickerel == 0:
                    continue
                if (trout * trout_points) + (pike * pike_points) + (
                    pickerel * pickerel_points
                ) <= total_point_allowance:
                    set_of_possible_catches.add((trout, pike, pickerel))

    for catch in set_of_possible_catches:
        print(
            f"{catch[0]} Brown Trout, {catch[1]} Northern Pike, {catch[2]} Yellow Pickerel"
        )

    print(f"Number of ways to catch fish: {len(set_of_possible_catches)}")


main()
