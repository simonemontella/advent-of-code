import fileinput
path = "C:\\Users\\siste\\j-workspace\\adventofcode2020\\inputs\\day{}.txt"

class Solution:
    
    def __init__(self, dayNumber):
        self.dayNumber = dayNumber
        self.lines = list(fileinput.input(path.format(self.dayNumber)))
    
    def part1(self):
        pass
    
    def part2(self):
        pass
        
    def solve(self):
        print ("Day {} Solutions: \n\tPart1: {}\n\tPart2: {}"
              .format(self.dayNumber, self.part1(), self.part2()))