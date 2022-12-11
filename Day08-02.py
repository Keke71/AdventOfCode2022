from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day08.txt") as f:
        matrix = list([int(x) for x in textLine.strip()] for textLine in f)
    height = len(matrix)
    width = len(matrix[0])
    columns = [[row[i] for row in matrix] for i in range(height)]
    max_score = 0
    # Iterate through all but the edge trees 
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            value = matrix[y][x]
            left = looking_distance(value, matrix[y][x-1::-1])
            right = looking_distance(value, matrix[y][x+1:])
            up = looking_distance(value, columns[x][y-1::-1])
            down = looking_distance(value, columns[x][y+1:])
            max_score = max(max_score, left * right * up * down)

    return max_score


def looking_distance(value, neighbours):
    count = 0
    for neighbour in neighbours:
        count += 1
        if neighbour >= value:
            break

    return count


run()
