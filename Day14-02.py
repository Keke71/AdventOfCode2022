from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day14.txt") as f:
        lines = list(filter(None, [line.rstrip() for line in f]))
        
    paths = []
    for line in lines:
        path = [(int(c[0]), int(c[1])) for c in (coord.split(',') for coord in line.split(" -> "))]
        paths.append(path)

    x_coordinates = [c[0] for path in paths for c in path]
    bottom = max([c[1] for path in paths for c in path]) + 2
    # Extend cave to the left and right to the maximum the sand can spread
    left = min(x_coordinates) - bottom
    right = max(x_coordinates) + bottom
    cave = Cave(left, right, bottom, paths)
    cave.start()

    return cave.count


class Cave():
    def __init__(self, left, right, bottom, paths):
        self.start_x = 500 - left
        self.width = right - left + 1
        self.bottom = bottom
        self.fields = [[0] * self.width for _ in range(self.bottom + 1)]
        self.count = 0
        # Add solid floor
        self.fields[self.bottom] = [1] * self.width

        for path in paths:
            for i in range(1, len(path)):
                x_start = min(path[i-1][0], path[i][0]) - left
                y_start = min(path[i-1][1], path[i][1])
                x_stop = max(path[i-1][0], path[i][0]) - left
                y_stop = max(path[i-1][1], path[i][1])
                if y_start == y_stop:
                    self.fields[y_start][x_start:x_stop+1] = [1] * (x_stop - x_start + 1)
                else:
                    for y in range(y_start, y_stop + 1):
                        self.fields[y][x_start] = 1

    def start(self):
        full = False
        while not full:
            full = False
            (x, y) = (self.start_x, 0)
            while True:
                next = self.drop(x, y)
                if next is None:
                    # Sand unit came to rest
                    self.fields[y][x] = 1
                    self.count += 1
                    if y == 0:
                        # Sand is piled up to the top
                        full = True
                    break
                (x, y) = next

    def drop(self, x, y):
        # Straight down
        if y == self.bottom or self.fields[y + 1][x] == 0:
            return (x, y + 1)
        # Left down
        if self.fields[y + 1][x - 1] == 0:
            return (x - 1, y + 1)
        # Right down
        if self.fields[y + 1][x + 1] == 0:
            return (x + 1, y + 1)
        # Nowhere to drop further
        return None
        
            
run()
