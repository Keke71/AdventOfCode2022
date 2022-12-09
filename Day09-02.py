from helpers.problemrunner import run_problem
from numpy import sign


@run_problem
def run():
    with open("Day09.txt") as f:
        lines = list(filter(None, (line.rstrip() for line in f)))

    rope = Rope(10)
    for line in lines:
        (direction, steps) = line.split()
        rope.move_head(direction, int(steps))

    return len(rope.tail_positions)


class Position():
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __iadd__(self, offset):
        self.x += offset.x
        self.y += offset.y
        return self

    def __sub__(self, offset):
        return Position(self.x - offset.x, self.y - offset.y)

    def decompose(self):
        return (self.x, self.y)


class Rope:
    step = {
        "U": Position(0, -1),
        "R": Position(1, 0),
        "D": Position(0, 1),
        "L": Position(-1, 0)
    }

    def __init__(self, number_of_knots):
        self.knots = [Position(0, 0) for _ in range(number_of_knots)]
        self.tail_positions = set([(0, 0)])

    def move_head(self, direction, steps):
        for _ in range(steps):
            self.move_head_one_step(direction)

    def move_head_one_step(self, direction):
        self.knots[0] += self.step[direction]
        self.follow_head()

    def follow_head(self):
        for i in range(1, len(self.knots)):
            (x, y) = (self.knots[i-1] - self.knots[i]).decompose()
            if abs(x) < 2 and abs(y) < 2:
                continue
            self.knots[i] += Position(sign(x), sign(y))
        self.tail_positions.add(self.knots[-1].decompose())


run()
