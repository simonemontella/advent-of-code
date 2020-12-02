from solutions.solution import Solution

class Day1(Solution):
    
    def __init__(self):
        super().__init__(1)
    
    def part1(self):
        for current_line in self.lines:
            first = int(current_line)
            
            for line in self.lines:
                second = int(line)
                if(first + second == 2020):
                    return first * second

    def part2(self):
        for current_line in self.lines:
            first = int(current_line)
            
            for next_line in self.lines:
                second = int(next_line)
                if(first + second < 2020):
                    for last_line in self.lines:
                        third = int(last_line)
                        if(first + second + third == 2020):
                            return first * second * third