from solutions.solution import Solution

class Day8(Solution):
    
    def __init__(self):
        super().__init__(8)

    def part1(self):
        lines = [line for line in self.lines]
        return self.run(lines, True)[1]
    
    def part2(self):
        '''accumulator = 0
        i = 0
        lines = [line for line in self.lines]
        while i < len(lines):
            line = lines[i]
            
            if(line.startswith("jmp")):
                lines[i] = line.replace("jmp", "nop")
                
                try:
                    modded = self.run(lines, False)
                    if(modded[0] == len(lines)):
                        accumulator = modded[1]
                        break
                except AssertionError: 
                    lines[i] = line
            elif(line.startswith("nop")):
                lines[i] = line.replace("nop", "jmp")
                
                try:
                    modded = self.run(lines, False)
                    if(modded[0] == len(lines)):
                        accumulator = modded[1]
                        break
                except AssertionError: 
                    lines[i] = line
            
            i += 1
        return accumulator'''
        pass
    
    def run(self, lines, interrupt):
        accumulator = 0
        i = 0
        while(i < len(lines)):
            line = lines[i]
            parts = line.split()
            
            if(i == len(lines)):
                break
            if(interrupt):
                if(len(parts) == 3):
                    break
                else: lines[i] += " ok"
                
            #assert(i < len(lines))
                
            cmd = parts[0]
            if(cmd == "nop"):
                i += 1
            else:
                val = int(parts[1])
                if(cmd == "acc"):
                    accumulator += val
                    i += 1
                elif(cmd == "jmp"):
                    i += val
                
        #assert(False)
        return accumulator if not interrupt else i, accumulator