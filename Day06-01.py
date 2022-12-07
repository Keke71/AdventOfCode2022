from helpers.problemrunner import run_problem

package_marker_size = 4

@run_problem
def run():
    with open("Day06.txt") as f:
        datastream = f.readline().rstrip()

    for i in range(len(datastream) - package_marker_size):
        package = datastream[i:i + package_marker_size]
        if len(set(package)) == package_marker_size:
            return i + package_marker_size


run()
