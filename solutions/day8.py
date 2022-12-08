from solutions.solution import Solution
from math import sqrt

class Day8(Solution):

    def __init__(self):
        super().__init__(8, "Treetop Tree House")
        self.map = {(x,y):tree for y,val in enumerate(self.lines) for x,tree in enumerate(val)}

        self.x_lenght = list(self.map.keys())[-1][0]
        self.y_lenght = list(self.map.keys())[-1][1]

        self.center = {pos: val for pos, val in self.map.items() if pos[0] in range(1, self.x_lenght) and pos[1] in range(1, self.y_lenght)}
        
    def part2(self):
        visibles = len(self.map) - len(self.center)
        for pos, tree in self.center.items():
            x, y = pos[0], pos[1]
            if(max([t for p,t in self.map.items() if p[0]==x and p[1]>y]) < tree
                or max([t for p,t in self.map.items() if p[0] > x and p[1] == y]) < tree
                or max([t for p,t in self.map.items() if p[0] < x and p[1] == y]) < tree
                or max([t for p,t in self.map.items() if p[0] == x and p[1] < y]) < tree):
                visibles += 1

        return visibles

    def part1(self):
        highest_score = 0
        for pos, tree in self.center.items():
            x, y = pos[0], pos[1]
            
            left_values = [p for p, v in self.map.items() if p[1] == y and p[0] < x and v >= tree]
            right_values = [p for p, v in self.map.items() if p[1] == y and p[0] > x and v >= tree]
            up_values = [p for p, v in self.map.items() if p[0] == x and p[1] < y and v >= tree]
            down_values = [p for p, v in self.map.items() if p[0] == x and p[1] > y and v >= tree]

            left_dist = x - self.min_distance(pos, left_values)[0] if len(left_values) > 0 else x
            right_dist = self.x_lenght - x if len(right_values) < 1 else self.min_distance(pos, right_values)[0] - x
            up_dist = y - self.min_distance(pos, up_values)[1] if len(up_values) > 0 else y
            down_dist = self.y_lenght - y if len(down_values) < 1 else self.min_distance(pos, down_values)[1] - y

            score = left_dist * right_dist * up_dist * down_dist
            if(score > highest_score):
                highest_score = score

        return highest_score

    def min_distance(self, pos, positions):
        x,y = pos[0], pos[1]
        distances = list(map(lambda t: sqrt(pow(t[0]-x, 2)+pow(t[1]-y, 2)), positions))

        return positions[distances.index(min(distances))]
