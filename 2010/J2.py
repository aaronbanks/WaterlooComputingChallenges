def main():

    nikky_forward = int(input())
    nikky_backwards = int(input())

    byron_forward = int(input())
    byron_backwards = int(input())

    steps = int(input())

    nikky = Student(
        "nikky",
        0,
        0,
        True,
        nikky_forward,
        nikky_backwards,
    )
    byron = Student(
        "nikky",
        0,
        0,
        True,
        byron_forward,
        byron_backwards,
    )

    for step in range(steps):
        nikky.take_a_step()
        byron.take_a_step()

    if nikky.location > byron.location:
        print("Nikky")
    elif nikky.location == byron.location:
        print("Tied")
    else:
        print("Byron")


class Student:
    def __init__(
        self,
        name,
        location,
        step_counter,
        direction_forward,
        forward_move,
        backwards_move,
    ):
        self.name = name
        self.location = location
        self.step_counter = step_counter
        self.direction_forward = direction_forward
        self.forward_move = forward_move
        self.backwards_move = backwards_move

    def take_a_step(self):
        if self.direction_forward == True:
            self.location += 1
            self.step_counter += 1

            if self.step_counter >= self.forward_move:
                self.direction_forward = not self.direction_forward
                self.step_counter = 0
        else:
            self.location -= 1
            self.step_counter += 1

            if self.step_counter >= self.backwards_move:
                self.direction_forward = not self.direction_forward
                self.step_counter = 0


main()
