from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day10.txt") as f:
        operations = list(filter(None, (line.rstrip() for line in f)))

        parser = SignalParser()
        parser.perform_operations(operations)

        return '\n' + '\n'.join(''.join(c for c in line) for line in parser.output)


class SignalParser:
    
    width = 40
    height = 6

    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.current_line = 0
        self.output = [[' '] * self.width for _ in range(self.height)]


    def perform_operations(self, operations):
        for operation in operations:
            self.cycle += 1
            self.current_line = self.cycle // self.width
            self.draw_pixel()
            if operation.startswith("addx"):
                self.cycle += 1
                self.draw_pixel()
                self.x += int(operation.split()[1])


    def draw_pixel(self):
        position_in_line = self.cycle % self.width - 1;
        if abs(self.x - position_in_line) <= 1:
            self.output[self.current_line][position_in_line] = "#"
                    

run()
