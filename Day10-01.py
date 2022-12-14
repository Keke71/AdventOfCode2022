from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day10.txt") as f:
        operations = list(filter(None, (line.rstrip() for line in f)))

        parser = SignalParser()
        parser.perform_operations(operations)

        return parser.signal_strength


class SignalParser:
    cycles_of_interest = [20 + i * 40 for i in range(6)]

    def __init__(self):
        self.signal_strength = 0
        self.x = 1
        self.cycle = 0

    def perform_operations(self, operations):
        for operation in operations:
            self.cycle += 1
            self.check_cycle()
            if operation.startswith("addx"):
                self.cycle += 1
                self.check_cycle()
                self.x += int(operation.split()[1])
            if len(self.cycles_of_interest) == 0:
                break
        return sum


    def check_cycle(self):
        if self.cycle == self.cycles_of_interest[0]:
            self.signal_strength += self.x * self.cycle
            self.cycles_of_interest = self.cycles_of_interest[1:]
                    

run()
