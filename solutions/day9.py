from solutions.solution import Solution

class Day9(Solution):
    
    def __init__(self):
        super().__init__(9)

    def part1(self):
        lines = self.lines
        error = 0
        for i in range(25, len(lines)):
            line = lines[i]
            
            if not self.findAddends(int(line), lines[i-25:i]):
                error = line
                break
            
        return error
    
    def part2(self):
        error = int(self.part1())
        lines = self.lines
        
        add = []
        for i in range(len(lines)):
            current = int(lines[i])
        
            if(current >= error):
                continue
        
            found = False
            add.append(current)
            while(i + 1 < len(lines)):
                current += int(lines[i + 1])
            
                if(current > error):
                    found = False
                    current = 0
                    add.clear()
                    break
            
                if(current == error):
                    add.append(int(lines[i+1]))
                    found = True
                    break
            
                i += 1
                add.append(int(lines[i]))
        
            if found:
                break
            
        return int(int(min(add)) + int(max(add)))  
                
    def findAddends(self, res, addends):
        found = []
        for i in range(len(addends)):
            current = int(addends[i])
            addend = []
            j = 0
            while(j < len(addends)):
                if(j == i):
                    j += 1                        
                    continue
                
                if(int(current + int(addends[j])) == res):
                    addend.append(addends[j])
                    break
                
                j += 1
            
            if(addend):
                found.append(current)
                found.append(addend[0])
                break
            
        return found