from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day01.txt") as f:
        lines = [line.rstrip() for line in f]

    count = len(list(filter(lambda x: len(x) == 0, lines))) + 1
    elfIndex = 0
    elfCalories = [0] * count
    for l in lines:
        if len(l) == 0:
            elfIndex += 1
            continue
        elfCalories[elfIndex] += int(l)
        
    return max(elfCalories)


run()
