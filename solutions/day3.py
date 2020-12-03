from solutions.solution import Solution

class Day3(Solution):
    
    def __init__(self):
        super().__init__(3)

    def part1(self):
        return self.count_trees(3,1)
        
    def part2(self):
        return (self.count_trees(1,1) 
                        * self.part1() 
                        * self.count_trees(5,1)
                        * self.count_trees(7,1)
                        * self.count_trees(1,2))
       
    def count_trees(self, x, y):
        trees = 0
        pos = 0
        for line in self.lines[::y]:
            trees += line[pos % len(line)] == "#"
            pos += x
            
        return trees