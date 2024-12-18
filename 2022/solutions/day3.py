from solutions.solution import Solution

class Day3(Solution):

    def __init__(self):
        super().__init__(3, "Rucksack Reorganization")

    def part1(self):
        items = []
        for backpack in self.lines:
            items.extend(set([c for c in backpack[:len(backpack)//2] if c in backpack[len(backpack)//2:]]))

        return self.sum_priorities(items)

    def part2(self):
        badges = []
        for group in [self.lines[n:n+3] for n in range(0, len(self.lines), 3)]:
            badges.extend(set([item for item in group[0] if item in group[1] and item in group[2]]))

        return self.sum_priorities(badges)

    def sum_priorities(self, items):
        return sum([ord(value)-96 if str.islower(value) else ord(value)-38 for value in items])
