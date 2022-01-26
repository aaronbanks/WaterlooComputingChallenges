def main():

    finger_count = int(input())

    possible_combinations = set()

    for left_fingers in range(6):
        for right_fingers in range(6):
            if right_fingers + left_fingers == finger_count:
                combination = [right_fingers, left_fingers]
                combination.sort()
                ordered_combination = (combination[1], combination[0])
                possible_combinations.add(ordered_combination)

    print(len(possible_combinations))


main()
