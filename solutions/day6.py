from solutions.solution import Solution
from itertools import groupby

class Day6(Solution):
    
    def __init__(self):
        super().__init__(6)
        self.groups = [list(group) for k, group in groupby(self.lines, key=bool) if k]
        
    def part1(self):
        yes_count = 0
        for group in self.groups:
            yes_answers = []
            for form in group:
                for answer in form:
                    if not (answer in yes_answers):
                        yes_answers.append(answer)
        
            yes_count += len(yes_answers)
            
        return yes_count
    def part2(self):
        yes_count = 0
        for group in self.groups:
            yes_answers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for form in group:
                yes_answers = [yes for yes in yes_answers if yes in form]
                            
            yes_count += len(yes_answers)
    
        return yes_count
    