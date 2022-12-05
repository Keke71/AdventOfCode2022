from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Day03.txt") as f:
        lines = [line.rstrip() for line in f]

    sum = 0
    for line in lines:
        half_size = len(line) // 2
        compartment1 = set(line[:half_size])
        compartment2 = line[half_size:]
        duplicate_item = list(compartment1.intersection(compartment2))[0]
        sum += get_priority(duplicate_item)

    return sum

def get_priority(item):
    return ord(item) - (ord('A') - 27 if item.isupper() else ord('a') - 1)


run()
