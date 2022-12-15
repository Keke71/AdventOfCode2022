from helpers.problemrunner import run_problem


base_directory_name = '/'
parent_directory_name = ".."
maximum_size = 100000

@run_problem
def run():
    with open("Day13.txt") as f:
        received_packets = list(filter(None, [line.rstrip() for line in f]))

    packets = [Packet(line[1:-1]) for line in received_packets]

    right_order = 0
    for i in range(0, len(packets), 2):
        list1 = List(packets[i].items)
        list2 = List(packets[i+1].items)
        if list1.is_smaller_than(list2):
            right_order += (i + 2) // 2

    return 0


#
# Start: Packet
#
# Packet: [List]
#
#                   / End
#         / Integer  
#        /          \ ,List
#       /
# List:         / ,List
#       \ [List 
#               \ ]
#
class Packet():

    def __init__(self, packet_line):
        self.current_line = packet_line
        self.items = self.read_list()


    def read_list(self):
        ret = List()
        if len(self.current_line) == 0:
            return ret

        while True:
            if self.try_read_string('['):
                ret.append(self.read_list())
            else:
                value = self.read_integer()
                ret.append(value)
            if self.try_read_string(',') == False:
                break

        self.try_read_string(']')

        return ret


    def read_integer(self):
        ret = 0
        while len(self.current_line) > 0:
            try:
                ret = ret * 10 + int(self.current_line[0])
                self.current_line = self.current_line[1:]
            except ValueError:
                break

        return ret


    def try_read_string(self, s):
        length = len(s)
        if self.current_line[:length] == s:
            self.current_line = self.current_line[length:]
            return True
        return False


class List(list):

    def is_smaller_than(self, other):
        for i, item in enumerate(self):
            if not type(item) is int and i >= len(self):
                return True
            elif not type(other) is int and i >= len(other):
                return False
            if type(item) is int and type(other) is int:
                return item < other
            if type(item) is int:
                return other.is_greater_than(item)
            if type(other) is int:
                return item.is_smaller_than(other)
            
            return item.is_smaller_than(other[i])


    def is_greater_than(self, other):
        for i, item in enumerate(self):
            if type(item) is int:
                if item > other:
                    return True
            else:
                return item.is_greater_than(other)

        return False

            
run()
