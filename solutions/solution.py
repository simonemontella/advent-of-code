import fileinput
from abc import ABC, abstractmethod

class Solution(ABC):

    path = "C:\\Users\\siste\\OneDrive\\Desktop\\smont\\advent-of-code\\inputs\\day{}.txt"

    def __init__(self, dayNumber: int):
        self.dayNumber = dayNumber
        self.lines = [line.replace("\n", "") for line
                      in fileinput.input(self.path.format(dayNumber))]

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

    def solve(self):
        spaces = "\x20" * 3
        print("DAY {}: \n{}PART 1: {}\n{}PART 2: {}"
              .format(self.dayNumber, spaces, self.part1(), spaces, self.part2()))
