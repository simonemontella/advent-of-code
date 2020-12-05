from solutions.solution import Solution

class Day5(Solution):
    
    seats = {}
    
    def __init__(self):
        super().__init__(5)

    def part1(self):
        max_id = 0
        for seat in self.lines:
            row = int(seat[:7].replace("B", "1").replace("F", "0"), 2)
            column = int(seat[7::].replace("R", "1").replace("L", "0"), 2)
            
            self.save_seat(row, column)
            
            id = (row*8) + column
            if(max_id < id):
                max_id = id
                
        return max_id
        
    def part2(self):
        missing = {}
        for seat in self.seats.keys():
            for i in range(0, 8):
                if not (i in self.seats[seat]):
                    missing[seat] = i
        
        return (min(missing.keys()) * 8 + missing[min(missing.keys())])
    
    def save_seat(self, row, column):
        if(self.seats.__contains__(row)):
            self.seats[row].append(column)
        else:
            self.seats[row] = []
            self.seats[row].append(column)