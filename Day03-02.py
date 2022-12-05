from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Day03.txt") as f:
        lines = [line.rstrip() for line in f]

    groups_of_three = [lines[i: i + 3] for i in range(0, len(lines), 3)]

    sum = 0
    for group in groups_of_three:
        duplicate_item = list(set.intersection(*map(set, group)))[0]
        sum += get_priority(duplicate_item)


    return sum


def get_priority(item):
    return ord(item) - (ord('A') - 27 if item.isupper() else ord('a') - 1)


run()
