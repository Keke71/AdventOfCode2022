from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day12.txt") as f:
        terrain = list([x for x in textLine.strip()] for textLine in f)

    start = [(start_x, start_y) for start_y, row in enumerate(terrain) for start_x, v in enumerate(row) if v == "S"][0]
    stop = [(start_x, start_y) for start_y, row in enumerate(terrain) for start_x, v in enumerate(row) if v == "E"][0]

    return HeightMap().find_path(terrain, start, stop)

class HeightMap():

    def find_path(self, terrain, start, stop):
        self.width = len(terrain[0])
        self.height = len(terrain)
        self.longest_way = self.width * self.height - 1
        self.terrain = [[Landmark(x, y, terrain[y][x], self.longest_way) for x in range(self.width)] for y in range(self.height)]
        self.terrain[start[1]][start[0]].distance = 0
        self.open_list = set([self.terrain[start[1]][start[0]]])
        self.closed_list = set()

        while len(self.open_list) > 0:
            q = sorted(self.open_list, key=lambda x: x.distance)[0]
            self.open_list.remove(q)
            self.closed_list.add(q)
            self.add_to_open_list(q, q.x + 1, q.y)
            self.add_to_open_list(q, q.x, q.y + 1)
            self.add_to_open_list(q, q.x - 1, q.y)
            self.add_to_open_list(q, q.x, q.y - 1)
            self.update_distance(q, q.x + 1, q.y)
            self.update_distance(q, q.x, q.y + 1)
            self.update_distance(q, q.x - 1, q.y)
            self.update_distance(q, q.x, q.y - 1)
                
        return self.terrain[stop[1]][stop[0]].distance
    
    def add_to_open_list(self, landmark, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            neighbour = self.terrain[y][x]
            if neighbour not in self.open_list and neighbour not in self.closed_list:
                self.open_list.add(neighbour)

    def update_distance(self, landmark, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            neighbour = self.terrain[y][x]
            if neighbour.height - landmark.height <= 1 and neighbour in self.open_list:
                dist = landmark.distance + 1
                if dist < neighbour.distance:
                    neighbour.distance = dist


class Landmark():
    def __init__(self, x, y, height_mark, maximum):
        self.x = x
        self.y = y
        self.height = self.get_height(height_mark)
        self.distance = maximum


    def get_height(self, height_mark):
        if height_mark == "S":
            return self.get_height("a")
        if height_mark == "E":
            return self.get_height("z")

        return ord(height_mark) - ord('a')

run()
