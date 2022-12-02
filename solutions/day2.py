from solutions.solution import Solution

class Day2(Solution):

    win = 6
    draw = 3
    loss = 0

    def __init__(self):
        super().__init__(2)

    def part1(self):
        score = 0
        for move in self.lines:
            moves = move.split(" ")
            score += self.play(moves[0], moves[1])
        
        return score

    def part2(self):
        score = 0
        for move in self.lines:
            moves = move.split(" ")
            score += self.play(moves[0], self.calc_move(moves[0], moves[1]))

        return score
            
    def calc_move(self, opponent, strategy):
        if(strategy == "X"): #LOSS
            return globals()[self.move(opponent).wins]
        elif(strategy == "Y"): #DRAW
            return self.move(opponent)
        elif(strategy == "Z"): #WIN
            return globals()[self.move(opponent).loss]
        else: return None

    def play(self, opponent, own):
        opponent = self.move(opponent)
        if(type(own) == str):
            own = self.move(own)

        score = own.score
        if(opponent.__name__ == own.__name__):
            score += self.draw
        elif(opponent.__name__ == own.wins):
            score += self.win
        else:
            score += self.loss

        return score

    def move(self, move: str):
        if(move in Rock.aliases):
            return Rock
        elif(move in Paper.aliases):
            return Paper
        elif(move in Scissors.aliases):
            return Scissors
        else:
            return None

class Rock:

    aliases = ['A', 'X']
    score = 1
    wins = 'Scissors'
    loss = 'Paper'

class Paper:

    aliases = ['B', 'Y']
    score = 2
    wins = 'Rock'
    loss = 'Scissors'

class Scissors:

    aliases = ['C', 'Z']
    score = 3
    wins = 'Paper'
    loss = 'Rock'
