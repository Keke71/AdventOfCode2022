from helpers.problemrunner import run_problem

message_marker_size = 14

@run_problem
def run():
    with open("Day06.txt") as f:
        datastream = f.readline().rstrip()

    for i in range(len(datastream) - message_marker_size):
        package = datastream[i:i + message_marker_size]
        if len(set(package)) == message_marker_size:
            return i + message_marker_size


run()
