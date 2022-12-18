from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day15.txt") as f:
        pairs = list(filter(None, [line.rstrip().split(": ") for line in f]))

    row = 2000000
    sensors = [pair[0].lstrip("Sensor at ") for pair in pairs]
    sensors = [(int(x.lstrip("x=")), int(y.lstrip("y="))) for (x, y) in (sensor.split(", ") for sensor in sensors)]
    beacons = [pair[1].lstrip("closest beacon is at ") for pair in pairs]
    beacons = [(int(x.lstrip("x=")), int(y.lstrip("y="))) for (x, y) in (beacon.split(", ") for beacon in beacons)]
    sensor_field = SensorField(sensors, beacons, row)
    sensor_field.mark_excluded_positions()

    return len(list(filter(lambda p: p[1] == row, sensor_field.positions)))


class SensorField():
    def __init__(self, sensors, beacons, row):
        self.sensors = sensors
        self.beacons = beacons
        self.row = row
        self.positions = set()


    def mark_excluded_positions(self):
        for i in range(len(self.sensors)):
            distance = self.manhattan_distance(self.sensors[i], self.beacons[i])
            self.exclude_positions(self.sensors[i], distance)


    def manhattan_distance(self, sensor, beacon):
        return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


    def exclude_positions(self, sensor, distance):
        y_position = sensor[1]
        if y_position + distance < self.row or y_position - distance > self.row:
            return

        x_position = sensor[0]
        y = abs(self.row - y_position)
        for x in range(-(distance - y), distance - y + 1):
            position = (x_position + x, self.row)
            if not position in self.beacons:
                self.positions.add(position)
    
run()
