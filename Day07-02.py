from helpers.problemrunner import run_problem


base_directory_name = '/'
parent_directory_name = ".."
total_space = 70000000
needed_space = 30000000

@run_problem
def run():
    with open("Day07.txt") as f:
        terminal_output = list(line.rstrip() for line in f)
    parser = OutputParser()
    parser.parse(terminal_output)

    used_space = parser.base_directory.get_size()
    free_space = total_space - used_space
    additionally_needed_space = needed_space - free_space
    dirs = parser.base_directory.get_all_directories()
    dir_to_be_deleted = next(d for d in sorted(dirs, key=lambda x: x.get_size()) if d.get_size() >= additionally_needed_space)
    
    return dir_to_be_deleted.get_size()


# Start: {Item}+
#
#       / Command
# Item:
#       \ FileSystemItem
#
#            / ' cd ' {.}+
# Command: $ 
#            \ ' ls ' {.}+
#
#                 / Directory
# FileSystemItem:
#                 \ File
#
# Directory: 'dir ' {.}+
#
# File: Size {.}+ 
#
class OutputParser():

    def __init__(self):
        self.base_directory = Directory(base_directory_name, None)
        self.current_directory = self.base_directory


    def parse(self, terminal_output):
        for line in terminal_output:
            self.current_line = line
            self.item()


    def item(self):
        cmd = self.try_read_string("$ ")
        if cmd is not None:
            self.command(cmd)
        else:
            self.file_system_item()


    def command(self, cmd):
        if cmd.startswith("cd"):
            self.change_directory(cmd.split()[1])
        # $ ls can be ignored


    def file_system_item(self):
        dir_name = self.try_read_string("dir ")
        if dir_name is not None:
            new_item = Directory(dir_name, self.current_directory)
        else:
            file = self.current_line.split()
            new_item = File(file[1], int(file[0]))
        self.current_directory.items.append(new_item)


    def change_directory(self, name):
        if name == base_directory_name:
            self.current_directory = self.base_directory
            return
        if name == parent_directory_name:
            self.current_directory = self.current_directory.parent_directory
            return
        
        dir = next((item for item in self.current_directory.items if item.name == name), None)
        if dir is None:
            dir = Directory(name, self.current_directory)
            self.current_directory.items.append(dir)
        self.current_directory = dir        


    def try_read_string(self, s):
        length = len(s)
        if self.current_line[:length] == s:
            return self.current_line[length:]
        return None


class FileSystemItem():

    def __init__(self, name):
        self.name = name


class Directory(FileSystemItem):

    def __init__(self, name, parent_directory):
        super().__init__(name)
        self.items = []
        self.parent_directory = parent_directory


    def get_all_directories(self):
        ret = [self]
        for dir in filter(lambda x: type(x) is Directory, self.items):
            ret.extend(dir.get_all_directories())
        return ret


    def get_size(self):
        ret = 0
        for item in self.items:
            ret += item.get_size()
        return ret


class File(FileSystemItem):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size


    def get_size(self):
        return self.size


run()
