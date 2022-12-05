from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Day04.txt") as f:
        lines = [line.rstrip().split(',') for line in f]

    count = len(list(filter(lambda x: SectionRange(x[0]).fully_included(SectionRange(x[1])), lines)))

    return count


class SectionRange:
    def __init__(self, section_definition):
        boundaries = section_definition.split('-')
        self.from_section = int(boundaries[0])
        self.to_section = int(boundaries[1])

    def fully_included(self, other_section):
        return self.from_section <= other_section.from_section and self.to_section >= other_section.to_section\
            or other_section.from_section <= self.from_section and other_section.to_section >= self.to_section


run()
