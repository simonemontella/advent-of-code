from solutions.solution import Solution
from math import floor, prod

class Day11(Solution):

    num_rounds = 20

    def __init__(self):
        super().__init__(11, "Monkey in the Middle")
        self.notes = [self.lines[n:n+6] for n in range(0, len(self.lines), 7)]
        self.monkeys = []

        for group in self.notes:
            self.monkeys.append(Monkey(group, self))

    def part1(self):
        for _ in range(self.num_rounds):
            for monkey in self.monkeys:
                monkey.inspect(3)

        elems = sorted([len(monkey.inspected_items) for monkey in self.monkeys], reverse=True)[:2]
        return prod(elems)

    def throw(self, destination, item):
        destination = self.monkeys[destination]

        destination.current_items.append(item)

    def part2(self):
        self.monkeys = []

        for group in self.notes:
            self.monkeys.append(Monkey(group, self))

        for _ in range(10000):
            for monkey in self.monkeys:
                monkey.inspect(1)

        elems = sorted([len(monkey.inspected_items)
                       for monkey in self.monkeys], reverse=True)[:2]
        return prod(elems)

class Monkey():

    def __init__(self, definition, manager) -> None:
        self.inspected_items = []
        self._parse(definition)
        self.manager = manager

    def inspect(self, divider):
        for item in self.current_items:
            self.inspected_items.append(item)
            #result = item
            self.operation = self.operation.replace("*", "/")
            self.operation = self.operation.replace("+", "-")
            try:
                result = eval("{} {}".format(item, self.operation.replace("old", str(item)))) // divider
            except:
                self.operation = self.operation.replace("/", "*")
                self.operation = self.operation.replace("-", "+")
                result = item
            if(result % self.divisor == 0):
                self.manager.throw(self.true_destination, result)
            else:
                self.manager.throw(self.false_destination, result)

        self.current_items.clear()

    def _parse(self, definition):
        for i in range(len(definition)):
            note = definition[i].strip()
            words = note.split()
            if(i == 0):
                self.id = int(words[1].replace(":", ""))
            elif(i == 1):
                self.current_items = [int(item) for item in note.replace("Starting items: ", "").split(",")]
            elif(i == 2):
                self.operation = note.replace("Operation: new = old ", "")
            elif(i == 3):
                self.divisor = int(note.split()[-1])
            elif(i == 4):
                self.true_destination = int(note.split()[-1])
            elif(i == 5):
                self.false_destination = int(note.split()[-1])

    def __repr__(self) -> str:
        return "monkey-id: {}".format(self.id)
