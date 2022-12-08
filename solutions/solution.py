import fileinput

class Solution():

    base_path = "C:\\Users\\siste\\OneDrive\\Desktop\\smont\\advent-of-code"
    inputs_path = base_path + "\\inputs\\day{}.txt"
    test_path = base_path + "\\tests\\{}"

    def __init__(self, dayNumber: int, name: str, testName=""):
        self.dayNumber = dayNumber
        self.test_path = self.test_path.format(testName)
        self.name = name
        self.lines = [line.replace("\n", "") for line in fileinput.input(self.inputs_path.format(dayNumber))]

    def part1(self):
        pass

    def part2(self):
        pass

    def solve(self):
        spaces = "\x20" * 3
        
        print("DAY {} - \"{}\": \n{}PART 1: {}\n{}PART 2: {}"
              .format(self.dayNumber, self.name, spaces, self.part1(), spaces, self.part2()))

    def print_test(self, string):
        if(self.test_path.endswith("\\")):
            raise NotImplementedError()

        with open(self.test_path, "a") as out:
            print(string, file=out)
