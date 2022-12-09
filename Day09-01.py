from helpers.problemrunner import run_problem
from numpy import sign, array


@run_problem
def run():
    with open("Day09.txt") as f:
        lines = list(filter(None, (line.rstrip() for line in f)))

    rope = Rope()
    for line in lines:
        (direction, steps) = line.split()
        rope.move_head(direction, int(steps))

    return len(rope.tail_positions)


class Rope:
    step = {
        "U": array([0, -1]),
        "R": array([1, 0]),
        "D": array([0, 1]),
        "L": array([-1, 0])
    }

    def __init__(self):
        self.head = array([0, 0])
        self.tail = array([0, 0])
        self.tail_positions = set([(0, 0)])

    def move_head(self, direction, steps):
        for _ in range(steps):
            self.move_head_one_step(direction)

    def move_head_one_step(self, direction):
        self.head += self.step[direction]
        self.follow_head()

    def follow_head(self):
        distance = self.head - self.tail
        x, y = distance[0], distance[1]
        if abs(x) < 2 and abs(y) < 2:
            return
        self.tail += array([sign(x), sign(y)])
        self.tail_positions.add((self.tail[0], self.tail[1]))


run()
