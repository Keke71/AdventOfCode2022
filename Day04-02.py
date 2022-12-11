from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Day04.txt") as f:
        lines = [line.rstrip().split(',') for line in f]

    count = len(list(filter(lambda x: SectionRange(x[0]).overlap(SectionRange(x[1])), lines)))

    return count


class SectionRange:
    def __init__(self, section_definition):
        lower, upper = section_definition.split('-')
        self.range = range(int(lower), int(upper) + 1)

    def overlap(self, other_section):
        return len(set(self.range).intersection(other_section.range)) > 0


run()
