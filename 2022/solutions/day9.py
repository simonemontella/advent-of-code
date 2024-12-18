from solutions.solution import Solution

class Day9(Solution):

    def __init__(self):
        super().__init__(9, "Rope Bridge", "rope.txt")
        self.moves = [line.split() for line in self.lines]

    def part1(self):
        '''head_positions = [(0,0)]
        tail_positions = [(0,0)]

        for direction, count in self.moves:
            for _ in range(int(count)):
                head = self.parse_move(direction, 1, head_positions[-1])
                head_positions.append(head)

                tail = tail_positions[-1]
                distance = self.get_distance(head, tail)

                if(distance != 1 and distance != 0 and distance != (2**(1/2))):
                    tail_positions.append([pos for pos in set.intersection(self.get_neighbors(head), self.get_neighbors(tail)) if self.get_distance(pos, head) == 1][0])

        return len(set(tail_positions))'''
        return self.head_tail(2)

    def part2(self):
        #return self.head_tail(9)
        return

    def head_tail(self, elements):
        rows = [[(0, 0)] for i in range(elements)]
        for direction, count in self.moves:
            for _ in range(int(count)):
                for i in range(1, len(rows)):
                    head_positions = rows[i-1]
                    head = head_positions[-1]
                    if(i == 1):
                        head = self.parse_move(direction, 1, head)
                        head_positions.append(head)

                    tail_positions = rows[i]
                    tail = tail_positions[-1]
                    distance = self.get_distance(head, tail)

                    if(distance != 1 and distance != 0 and distance != (2**(1/2))):
                        heads = self.get_neighbors(head)
                        tails = self.get_neighbors(tail)
                        interses = set.intersection(heads, tails)
                        elems = [pos for pos in interses if self.get_distance(pos, head) == 1]
                        elem = elems[0] if len(elems) > 0 else [pos for pos in interses if self.get_distance(pos, head) == (2**(1/2))][0]
                        tail_positions.append(elem)

        return len(set(rows[-1]))

    def get_neighbors(self, pos):
        return set([(pos[0]+1, pos[1]), (pos[0]-1, pos[1]),
                    (pos[0], pos[1]+1), (pos[0], pos[1]-1),
                    (pos[0]+1, pos[1]+1), (pos[0]-1, pos[1]-1),
                    (pos[0]-1, pos[1]+1), (pos[0]+1, pos[1]-1)])

    def get_distance(self, pos1, pos2):
        return (((pos1[0] - pos2[0])**2) + ((pos1[1] - pos2[1])**2)) ** (1/2)

    def parse_move(self, direction, moves, position):
        if(direction == 'L'):
            position = (position[0] - moves, position[1])
        elif(direction == 'R'):
            position = (position[0] + moves, position[1])
        elif(direction == 'U'):
            position = (position[0], position[1] + moves)
        elif(direction == "D"):
            position = (position[0], position[1] - moves)

        return position
