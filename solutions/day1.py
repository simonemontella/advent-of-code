from solutions.solution import Solution

class Day1(Solution):

    def __init__(self):
        super().__init__(1)
        self.calories  = []

    def part1(self):
        maxCalories = 0
        elfCalories = 0
        for calorie in self.lines:
            if(calorie == ""):
                if(elfCalories > maxCalories):
                    maxCalories = elfCalories

                self.calories.append(elfCalories)
                elfCalories = 0
                continue

            elfCalories += int(calorie)

        return maxCalories

    def part2(self):
        self.calories.sort(reverse=True)
        return sum(self.calories[:3])