from helpers.problemrunner import run_problem
from helpers.dicthelpers import create_or_append


@run_problem
def run():
    with open("Day15.txt") as f:
        pairs = list(filter(None, [line.rstrip().split(": ") for line in f]))

    max_coordinates = 4000000
    sensors = [pair[0].lstrip("Sensor at ") for pair in pairs]
    sensors = [(int(x.lstrip("x=")), int(y.lstrip("y="))) for (x, y) in (sensor.split(", ") for sensor in sensors)]
    beacons = [pair[1].lstrip("closest beacon is at ") for pair in pairs]
    beacons = [(int(x.lstrip("x=")), int(y.lstrip("y="))) for (x, y) in (beacon.split(", ") for beacon in beacons)]
    pairs = [(sensors[i], beacons[i]) for i in range(len(sensors))]
    sensor_field = SensorField(pairs, max_coordinates)
    sensor_field.mark_excluded_positions()

    for row_number, ranges in sensor_field.rows.items():
        sorted_ranges = sorted(ranges, key=lambda r: r[0])
        current_max = 0
        for sorted_range in sorted_ranges:
            if sorted_range[0] > current_max + 1:
                return tuning_frequency(current_max + 1, row_number)
            current_max = max(current_max, sorted_range[1])


def tuning_frequency(x, y):
    return x * 4000000 + y;


class SensorField():
    def __init__(self, pairs, max_coordinates):
        self.pairs = pairs
        self.max_coordinates = max_coordinates
        self.rows = {}


    def mark_excluded_positions(self):
        for pair in self.pairs:
            sensor = pair[0]
            beacon = pair[1]
            distance = self.manhattan_distance(sensor, beacon)
            self.exclude_positions(sensor, distance)


    def manhattan_distance(self, sensor, beacon):
        return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


    def exclude_positions(self, sensor, distance):
        y_position = sensor[1]
        if y_position + distance < 0 or y_position - distance > self.max_coordinates:
            return

        x_position = sensor[0]
        for y in range(-distance, distance + 1):
            if 0 <= y_position + y <= self.max_coordinates:
                create_or_append(self.rows, y_position + y, (max(0, (x_position - (distance - abs(y)))), min(x_position + distance - abs(y), self.max_coordinates)))
    
run()
