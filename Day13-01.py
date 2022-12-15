from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Day13.txt") as f:
        received_packets = list(filter(None, [line.rstrip() for line in f]))

    packets = [Packet(line[1:-1]) for line in received_packets]

    correct_order = 0
    for i in range(0, len(packets), 2):
        list1 = [packets[i].items]
        list2 = [packets[i+1].items]
        if compare_lists(list1, list2) == -1:
            correct_order += (i + 2) // 2

    return correct_order


def compare_lists(list1, list2):
    for i in range(max(len(list1), len(list2))):
        if i >= len(list1):
            return -1
        if i >= len(list2):
            return 1
        item1 = list1[i]
        item2 = list2[i]
        if type(item1) is int and type(item2) is int:
            if item1 == item2:
                continue
            return -1 if item1 < item2 else 1
        if type(item1) is int:
            comp = compare_value_to_list(item1, item2)
            if comp == 0:
                continue
            return comp
        if type(item2) is int:
            comp = compare_list_to_value(item1, item2)
            if comp == 0:
                continue
            return comp
        
        comp = compare_lists(item1, item2)
        if comp == 0:
            continue
        return comp

    return 0


def compare_value_to_list(value, list):
    if len(list) == 0:
        return 1
    return compare_lists([value], list)


def compare_list_to_value(list, value):
    if len(list) == 0:
        return -1
    return compare_lists(list, [value])


def compare_integers(value1, value2):
    if value1 == value2:
        return 0
    return -1 if value1 < value2 else 1


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
        ret = []
        if len(self.current_line) == 0:
            return ret

        while True:
            if self.try_read_string('['):
                ret.append(self.read_list())
            else:
                value = self.read_integer()
                if value >= 0:
                    ret.append(value)
                else:
                    self.try_read_string(']')
                    break
            if self.try_read_string(',') == False:
                break

        self.try_read_string(']')

        return ret


    def read_integer(self):
        # Empty brackets
        if self.try_read_string(']'):
            return -1

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

            
run()
