from solutions.solution import Solution

class Day2(Solution):

    win = 6
    draw = 3
    loss = 0

    def __init__(self):
        super().__init__(2, "Rock Paper Scissors")

    def part1(self):
        score = 0
        for moves in [move.split(" ") for move in self.lines]:
            score += self.play(moves[0], moves[1])
        
        return score

    def part2(self):
        score = 0
        for moves in [move.split(" ") for move in self.lines]:
            score += self.play(moves[0], self.calc_move(moves[0], moves[1]))

        return score
            
    def calc_move(self, opponent, strategy):
        if(strategy == "X"): #LOSS
            return globals()[self.get_move(opponent).wins]
        elif(strategy == "Y"): #DRAW
            return self.get_move(opponent)
        elif(strategy == "Z"): #WIN
            return globals()[self.get_move(opponent).loses]
        else: return None

    def play(self, opponent, own):
        opponent = self.get_move(opponent)
        if(type(own) == str):
            own = self.get_move(own)

        score = own.score
        if(opponent.__name__ == own.__name__):
            score += self.draw
        elif(opponent.__name__ == own.wins):
            score += self.win
        else:
            score += self.loss

        return score

    def get_move(self, move: str):
        if(move in Rock.aliases):
            return Rock
        elif(move in Paper.aliases):
            return Paper
        elif(move in Scissors.aliases):
            return Scissors
        else: return None

class Rock:

    aliases = ['A', 'X']
    score = 1
    wins = 'Scissors'
    loses = 'Paper'

class Paper:

    aliases = ['B', 'Y']
    score = 2
    wins = 'Rock'
    loses = 'Scissors'

class Scissors:

    aliases = ['C', 'Z']
    score = 3
    wins = 'Paper'
    loses = 'Rock'
