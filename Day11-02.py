from functools import reduce
from helpers.problemrunner import run_problem


@run_problem
def run():
    monkey_length = 6
    rounds = 10000

    with open("Day11.txt") as f:
        lines = list(filter(None, (line.rstrip() for line in f)))

    monkey_lines = [lines[i: i + monkey_length] for i in range(0, len(lines), monkey_length)]
    monkeys = []
    for monkey_number, lines_per_monkey in enumerate(monkey_lines):
        monkey = create_monkey(monkey_number, lines_per_monkey)
        monkeys.append(monkey)

    divisor = reduce(lambda a, b: a * b, [d.test_func.divisible_by for d in monkeys])
    for i in range(rounds):
        print(i)
        for monkey in monkeys:
            while len(monkey.items) > 0:
                (thrown_item, target) = monkey.throw_first_item()
                monkeys[target].items.append(thrown_item % divisor)

    inspection_counts = sorted([x.inspection_count for x in monkeys], reverse=True)

    return inspection_counts[0] * inspection_counts[1]


def create_monkey(monkey_number, lines_per_monkey):
        stripped = list(map(lambda x: x.strip(), lines_per_monkey))
        line_index = 1
        _, items = stripped[line_index].split("Starting items: ")
        line_index += 1
        _, operation = stripped[line_index].split("Operation: new = old ")
        line_index += 1
        _, divisible_by = stripped[line_index].split("Test: divisible by ")
        line_index += 1
        _, true_target = stripped[line_index].split("If true: throw to monkey ")
        line_index += 1
        _, false_target = stripped[line_index].split("If false: throw to monkey ")
        test_condition = TestCondition(int(divisible_by), int(true_target), int(false_target))

        return Monkey(monkey_number, [int(item) for item in items.split(", ")], operation, test_condition)


class TestCondition:

    def __init__(self, divisible_by, true_target, false_target):
        self.divisible_by = divisible_by
        self.true_target = true_target
        self.false_target = false_target

    def get_target(self, item):
        return self.true_target if item % self.divisible_by == 0 else self.false_target


class Monkey:

    def __init__(self, number, items, operation, test_func):
        self.number = number
        self.items = items
        self.test_func = test_func
        self.operation = self.create_operation(operation)
        self.inspection_count = 0

    def throw_first_item(self):
        self.inspection_count += 1
        item = self.operation(self.items[0])
        target = self.test_func.get_target(item)
        del self.items[0]

        return (item, target)

    def create_operation(self, operation):
        operator, argument = operation.split()
        if argument == "old":
            return lambda x: int(x * x)
        if operator == "*":
            return lambda x: x * int(argument)

        return lambda x: x + int(argument)

run()
