from solutions.solution import Solution

class Day6(Solution):

    def __init__(self):
        super().__init__(6, "Tuning Trouble")
        self.signal = self.lines[0]

    def part1(self):
        return self.find_marker(4)

    def part2(self):
        return self.find_marker(14)

    def find_marker(self, lenght):
        current = 0
        while(current <= len(self.signal)-lenght):
            sequence = set(self.signal[current:current+lenght])
            if(len(sequence) == lenght):  #no duplicates
                break

            current += 1

        return current+lenght

'''
n0 n1 n2 n3
n1 n2 n3 n4
n2 n3 n4 n5
n3 n4 n5 n6
n4 n5 n6 n7
n5 n6 n7 n8
n6 n7 n8 n9 -> 6 <= 10 - 4
0123456789 - len = 10
'''
        
