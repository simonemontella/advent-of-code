from solutions.solution import Solution

class Day7(Solution):

    dir_limit = 100000
    disk_size = 70000000
    needed_space = 30000000

    def __init__(self):
        super().__init__(7, "No Space Left On Device", "tree.txt")
        self.cmds = {i: e[2:] for i, e in enumerate(self.lines) if e.startswith("$")}

    def part1(self):
        tree = list()
        cursor = ""
        for ind, val in self.cmds.items():
            cmd = val.split()
            if(len(cmd) == 2): #cmd = cd <dest>
                if(cmd[1] == "/"):
                    folder = Directory(cmd[1], "|")
                    tree.append(folder)
                elif(cmd[1] == ".."):
                    cursor = self.replaceLast(cursor, "|" + cursor.split("|")[-1])
                    continue

                cursor += "|" + cmd[1]
            else: #cmd = ls
                dirName = cursor.split("|")[-1]
                path = self.replaceLast(cursor, dirName)
                if(ind > 1 and path[len(path)-1] == "|"):
                    path = path[:len(path)-1]

                currentDir = [folder for folder in tree if folder.name == dirName and folder.path == path][0]
                for result in self.get_response(ind):
                    if(result.startswith("dir")):
                        subDir = Directory(result.split()[1], cursor)
                        tree.append(subDir)
                        currentDir.add(subDir)
                    else:
                        currentDir.add(File(result))

        self.tree = tree
        tree[0].print(self)
        return sum([folder.get_size() for folder in tree if folder.get_size() < self.dir_limit])

    def part2(self):
        unused_space = self.disk_size - self.tree[0].get_size()
        self.needed_space = self.needed_space - unused_space

        return min([folder.get_size() for folder in self.tree if folder.get_size() > self.needed_space])
    
    def replaceLast(self, string, occurrence):
        return "".join(string.rsplit(occurrence, 1))

    def get_response(self, cmdIndex):
        responses = []
        while(cmdIndex+1 < len(self.lines)):
            cmdIndex += 1
            response = self.lines[cmdIndex]
            if(response.startswith("$")):
                break

            responses.append(response)

        return responses

class File:

    def __init__(self, definition) -> None:
        self.definition = definition
        definition = definition.split()
        self.name = definition[1]
        self.size = int(definition[0])

class Directory():

    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path
        self.files = []

    def calz_size(self, files):
        size = 0
        for file in files:
            if(type(file) == File):
                size += file.size
            elif(type(file) == Directory):
                size += self.calz_size(file.files)

        return size

    def get_size(self):
        return self.calz_size(self.files)

    def add(self, file):
        self.files.append(file)

    space = "\x20"

    def display(self, dir, spaces, solution):
        solution.print_test("{} - {} (dir)".format(self.space if dir.path == "" else self.space * spaces, dir.name))
        for file in dir.files:
            if(type(file) == File):
                solution.print_test("{} - {} (file, size={})".format(self.space * spaces * 2, file.name, file.size))
            elif(type(file) == Directory):
                self.display(file, spaces+1, solution)

    def print(self, solution):
        self.display(self, 1, solution)
