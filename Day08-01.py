from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day08.txt") as f:
        matrix = list([int(x) for x in textLine.strip()] for textLine in f)
    height = len(matrix)
    width = len(matrix[0])
    columns = [[row[i] for row in matrix] for i in range(height)]
    count = 2 * (height + width) - 4 
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            value = matrix[y][x]
            if value > max(matrix[y][:x]) or value > max(matrix[y][x + 1:])\
                or value > max(columns[x][:y]) or value > max(columns[x][y + 1:]):
                count += 1

    return count


run()
