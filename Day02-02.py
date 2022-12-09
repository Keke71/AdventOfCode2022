from helpers.problemrunner import run_problem

values = {"A": 1, "B": 2, "C": 3}
moves = list(values.keys())


@run_problem
def run():
    with open("Day02.txt") as f:
        scores = [get_score(line.rstrip()) for line in f]

    return sum(scores)

def get_score(move):
    if move[2] == "Y":
        return values[move[0]] + 3

    my_result = get_my_result(move)
    return values[my_result] + (0 if move[2] == "X" else 6)

def get_my_result(move):
    index_of_opponent = moves.index(move[0])
    return moves[(index_of_opponent + 1 if move[2] == "Z" else index_of_opponent + 2) % 3]

run()
