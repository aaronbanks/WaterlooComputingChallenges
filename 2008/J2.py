from collections import deque


def main():
    playlist = ["A", "B", "C", "D", "E"]

    queued_playlist = deque(playlist)

    while True:
        button_number = int(input("Button Number: "))

        number_of_presses = int(input("Number of Presses: "))

        for numbers in range(number_of_presses):

            if button_number == 1:
                queued_playlist.rotate(-1)

            elif button_number == 2:
                queued_playlist.rotate(1)

            elif button_number == 3:
                location_one = queued_playlist[0]
                location_two = queued_playlist[1]

                queued_playlist[0] = location_two
                queued_playlist[1] = location_one

            elif button_number == 4:
                playlist = list(queued_playlist)
                print(playlist)
                return True


main()
