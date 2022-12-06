from solutions.solution import Solution
from copy import deepcopy

class Day5(Solution):

    def __init__(self):
        super().__init__(5, "Supply Stacks")
        self.setup()

    def part1(self):
        stacks = deepcopy(self.stacks)
        for move in self.moves:
            words = move.split()
            qty = int(words[1])
            origin = int(words[3])-1
            to = int(words[5])-1

            for i in range(qty):
                stacks[to].insert(0, stacks[origin].pop(0))

        return "".join([stack[0] for stack in stacks])

    def part2(self):
        for move in self.moves:
            words = move.split()
            qty = int(words[1])
            origin = int(words[3])-1
            to = int(words[5])-1

            items = self.stacks[origin][:qty]
            self.stacks[origin] = self.stacks[origin][qty:]
            self.stacks[to] = items + self.stacks[to]

        return "".join([stack[0] for stack in self.stacks if len(stack)>0])

    def setup(self):
        rowsCount = (list.index(self.lines, "")+1)-2
        colsCount = int(len(self.lines[rowsCount])/4)+1
        self.stacks = [[] for x in range(colsCount)]
        for cols in range(rowsCount):
            line = self.lines[cols]
            for row in range(0, colsCount):
                value = line[(row*4)+1]
                if(value != ' '):
                    self.stacks[row].insert(cols, value)
        
        self.moves = self.lines[rowsCount+2:]

'''
lin0    stacks[0][0] = lin0[1]
        stacks[1][0] = lin0[5]
        stacks[2][0] = lin0[9]
            ...
        stacks[8][0] = lin0[33]

lin1    stacks[0][1] = lin1[1]
        stacks[1][1] = lin1[5]

        ...

lin7    stacks[0][7] = lin[1]
        ...
'''
