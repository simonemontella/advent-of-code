from solutions.solution import Solution

class Day10(Solution):

    def __init__(self):
        super().__init__(10, "Cathode-Ray Tube")

    def part1(self):
        relevant_cycles = [20, 60, 100, 140, 180, 220]
        x = 1
        cycles = 0
        strenght = 0
        for istr in self.lines:
            x_amount = 0

            if(istr.startswith("noop")):
                cycles += 1
            else:
                x_amount = int(istr.split()[1])
                cycles += 2

            if(len(relevant_cycles) > 0 and cycles >= relevant_cycles[0]):
                element = relevant_cycles.pop(0)
                strenght += element*x

            x += x_amount

        return strenght

    def part2(self):
        return super().part2()
