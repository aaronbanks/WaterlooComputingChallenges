def main():
    test_cases = int(input())

    for case in range(test_cases):
        input_data = input().split()
        particle_quanities = []
        for quanitiy in input_data:
            particle_quanities.append(int(quanitiy))

        moves_so_far = []
        possible_games = []

        possible_games = find_possible_combinations(
            particle_quanities, moves_so_far, possible_games
        )


# POSSIBLE REACTIONS: AABDD, ABCD, CCD, BBB, AD

# PATRICK ALLWAYS GOES FIRST, RONALD SECOND

# ONE PLAYER WILL ALWAYS HAVE A PERFECT STRATEGY POSSIBLE
# FOR PATRICK TO WIN, THERE NEEDS TO BE AN ODD NUMBER OF MOVES
# FOR RONALD TO WIN, THERE MUST BE AN EVEN NUMBER OF MOVES

# FOR EACH LINE, FIND ALL POSSIBLE COMBINATIONS
# FIND THE INITAL MOVE THAT CAN ONLY RESULT IN ODD OR EVEN AFTERWARDS

# OUTPUT THE PLAYER WITH PERFECT STRATEGY

# total_moves_even = True
# total_moves_even = not total_moves_even


def find_possible_combinations(particle_quanities, moves_so_far, possible_games):
    viable_move_found = False

    assembly_tuple = assemble_aabdd(particle_quanities)
    if assembly_tuple[0] == True:
        viable_move_found = True
        aabdd_move = moves_so_far.copy()
        aabdd_move.append("aabdd")
        possible_games.extend(
            find_possible_combinations(assembly_tuple[1], aabdd_move, possible_games)
        )

    assembly_tuple = assemble_abcd(particle_quanities)
    if assembly_tuple[0] == True:
        viable_move_found = True
        abcd_move = moves_so_far.copy()
        abcd_move.append("abcd")
        possible_games.extend(
            find_possible_combinations(assembly_tuple[1], abcd_move, possible_games)
        )

    assembly_tuple = assemble_ccd(particle_quanities)
    if assembly_tuple[0] == True:
        viable_move_found = True
        ccd_move = moves_so_far.copy()
        ccd_move.append("ccd")
        possible_games.extend(
            find_possible_combinations(assembly_tuple[1], ccd_move, possible_games)
        )

    assembly_tuple = assemble_bbb(particle_quanities)
    if assembly_tuple[0] == True:
        viable_move_found = True
        bbb_move = moves_so_far.copy()
        bbb_move.append("bbb")
        possible_games.extend(
            find_possible_combinations(assembly_tuple[1], bbb_move, possible_games)
        )

    assembly_tuple = assemble_ad(particle_quanities)
    if assembly_tuple[0] == True:
        viable_move_found = True
        ad_move = moves_so_far.copy()
        ad_move.append("ad")
        possible_games.extend(
            find_possible_combinations(assembly_tuple[1], ad_move, possible_games)
        )

    if viable_move_found == False:
        possible_games.append(moves_so_far)

    return possible_games


def assemble_aabdd(particle_quanities):
    if (
        particle_quanities[0] > 1
        and particle_quanities[1] > 0
        and particle_quanities[3] > 1
    ):
        particle_quanities[0] -= 2
        particle_quanities[1] -= 1
        particle_quanities[3] -= 2
        return (True, particle_quanities)

    return (False, particle_quanities)


def assemble_abcd(particle_quanities):
    if (
        particle_quanities[0] > 0
        and particle_quanities[1] > 0
        and particle_quanities[2] > 0
        and particle_quanities[3] > 0
    ):
        particle_quanities[0] -= 1
        particle_quanities[1] -= 1
        particle_quanities[2] -= 1
        particle_quanities[3] -= 1
        return (True, particle_quanities)
    return (False, particle_quanities)


def assemble_ccd(particle_quanities):
    if particle_quanities[2] > 1 and particle_quanities[3] > 0:
        particle_quanities[2] -= 1
        particle_quanities[3] -= 2
        return (True, particle_quanities)
    return (False, particle_quanities)


def assemble_bbb(particle_quanities):
    if particle_quanities[1] > 2:
        particle_quanities[1] -= 3
        return (True, particle_quanities)
    return (False, particle_quanities)


def assemble_ad(particle_quanities):
    if particle_quanities[0] > 0 and particle_quanities[3] > 0:
        particle_quanities[0] -= 1
        particle_quanities[3] -= 1
        return (True, particle_quanities)
    return (False, particle_quanities)


main()
