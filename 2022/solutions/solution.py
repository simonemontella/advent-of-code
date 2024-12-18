import fileinput, configparser
from os.path import exists

class Solution():

    base_path = "C:\\Users\\siste\\OneDrive\\Desktop\\smont\\advent-of-code"
    inputs_path = base_path + "\\inputs\\day{}.txt"
    test_path = base_path + "\\tests\\{}"

    def __init__(self, dayNumber: int, name: str, testName=""):
        self.dayNumber = dayNumber
        self.test_path = self.test_path.format(testName)
        self.name = name
        self.lines = [line.replace("\n", "") for line in fileinput.input(self.inputs_path.format(dayNumber))]

        if(not exists("cache.ini")):
            with open("cache.ini", "x"):
                pass

    def part1(self):
        pass

    def part2(self):
        pass

    def solve(self):
        spaces = "\x20" * 3

        cache = configparser.ConfigParser()

        results = cache.read("cache.ini")
        section = f'DAY{self.dayNumber}'

        part1, part2 = None, None
        edited = False
        if(not section in cache):
            part1, part2 = self.part1(), self.part2()
            cache[section] = {}
            cache[section]["part1"] = str(part1)
            cache[section]["part2"] = str(part2)
            edited = True
        else:
            if(not "part1" in cache[section] or cache[section]["part1"] == str(None)):
                part1 = self.part1()
                cache[section]["part1"] = str(part1)
                edited = True
            
            if(not "part2" in cache[section] or cache[section]["part2"] == str(None)):
                part2 = self.part2()
                cache[section]["part2"] = str(part2)
                edited = True

            part1, part2 = cache[section]["part1"], cache[section]["part2"]

        if(edited):
            with open("cache.ini", "w") as file:
                cache.write(file)
        
        print("DAY {} - \"{}\": \n{}PART 1: {}\n{}PART 2: {}"
              .format(self.dayNumber, self.name, spaces, part1, spaces, part2))

    def print_test(self, string):
        if(self.test_path.endswith("\\")):
            raise NotImplementedError()

        with open(self.test_path, "a") as out:
            print(string, file=out)
