from solutions.solution import Solution

class Day2(Solution):
    
    def __init__(self):
        super().__init__(2)

    def part1(self):
        occurrences = 0
        for string in self.lines:
            char = string.split()[1].replace(":", "")
            range_min = int(string.split()[0].split("-")[0])
            range_max = int(string.split()[0].split("-")[1])
            password = string.split()[2]
            
            count = self.count_occurrences(password, char)
            
            if(count in range(range_min, range_max+1)):
                occurrences +=1
            
        return occurrences
        
    def part2(self):
        occurrences = 0
        for string in self.lines:
            char = string.split()[1].replace(":", "")
            pos1 = int(string.split()[0].split("-")[0])-1
            pos2 = int(string.split()[0].split("-")[1])-1
            password = string.split()[2]
            
            if(password[pos1] == char):
                if(password[pos2] != char):
                    occurrences += 1
                    continue
            elif(password[pos2] == char):
                occurrences += 1
                continue
        
        return occurrences
    
    def count_occurrences(self, string, char):
        return len([counted for counted in string if counted == char])