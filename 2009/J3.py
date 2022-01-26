def main():

    central_time = input()

    pacific = (-3, 0)
    mountain = (-2, 0)
    central = (-1, 0)
    eastern = (0, 0)
    atlantic = (1, 0)
    newfoundland = (1, 30)

    time_processed = process_time(central_time)

    print(f"{timezone_adjustment(time_processed, eastern)} in Ottawa")
    print(f"{timezone_adjustment(time_processed, pacific)} in Victoria")
    print(f"{timezone_adjustment(time_processed, mountain)} in Edmonton")
    print(f"{timezone_adjustment(time_processed, central)} in Winnipeg")
    print(f"{timezone_adjustment(time_processed, eastern)} in Toronto")
    print(f"{timezone_adjustment(time_processed, atlantic)} in Halifax")
    print(f"{timezone_adjustment(time_processed, newfoundland)} in St. John's")


def process_time(time):

    time_digits = list(time)
    time_processed = [0, 0]

    if len(time) < 3:
        time_processed[1] = int(time)

    elif len(time) == 3:
        time_processed[0] = int(time_digits[0])
        time_processed[1] = int(time_digits[1] + time_digits[2])

    else:
        time_processed[0] = int(time_digits[0] + time_digits[1])
        time_processed[1] = int(time_digits[2] + time_digits[3])

    return time_processed


def timezone_adjustment(time, adjustment):

    adjusted_time = [0, 0]

    if time[1] + adjustment[1] < 60:
        adjusted_time[1] = time[1] + adjustment[1]
    else:
        adjusted_time[1] = time[1] + adjustment[1] - 60
        adjusted_time[0] += 1

    if time[0] + adjustment[0] < 24:
        adjusted_time[0] += time[0] + adjustment[0]
    else:
        adjusted_time[0] += time[0] + adjustment[0] - 24

    minutes = str(adjusted_time[1])

    if minutes == "0":
        minutes = minutes + "0"
    if int(minutes) > 0 and int(minutes) < 10:
        minutes = "0" + minutes

    hours = str(adjusted_time[0])

    if hours == "0":
        hours = ""

    str_adjusted_time = hours + minutes

    return str_adjusted_time


main()
