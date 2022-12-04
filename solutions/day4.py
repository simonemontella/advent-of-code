from solutions.solution import Solution

class Day4(Solution):

    def __init__(self):
        super().__init__(4, "Camp Cleanup")
        self.ranges = []

    def part1(self):
        pairs = 0
        for assignment in [line.split(",") for line in self.lines]:
            first = [int(elem) for elem in assignment[0].split("-")]
            second = [int(elem) for elem in assignment[1].split("-")]

            ran1 = range(second[0], second[1]+1)
            ran2 = range(first[0], first[1]+1)

            self.ranges.append([ran1, ran2])

            if((first[0] in ran1 and first[1] in ran1) or (second[0] in ran2 and second[1] in ran2)):
                pairs += 1

        return pairs

    def part2(self):
        overlaps = 0
        for ranges in self.ranges:
            ran1 = set([elem for elem in ranges[0]])
            ran2 = set([elem for elem in ranges[1]])

            if(set.intersection(ran1, ran2)):
                overlaps += 1

        return overlaps
