from solutions.solution import Solution
from itertools import groupby

class Day4(Solution):
    
    def __init__(self):
        super().__init__(4)
        self.passports = [list(g) for k, g in groupby(self.lines, key=bool) if k]
        self.criteria = criteria = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def part1(self):
        valid_passports = 0
        for passport in self.passports:
            valid_passports += self.validate(passport)
            
        return valid_passports
    
    def part2(self):
        valid_passports = 0
        for passport in self.passports:
            valid_passports += self.complex_validate(passport)
        return valid_passports
    
    def validate(self, passport):
        return self.criteria <= self.extract(passport).keys() 
    
    def complex_validate(self, passport):
        if not self.validate(passport): return 0
        
        passport = self.extract(passport)
        for field in passport:
            value = passport[field]
            if(field == "ecl"):
                if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']): 
                    return 0
            elif(field == "hcl"):
                if not (len(value) == 7): 
                    return 0
                if not (value.startswith("#")): 
                    return 0
                
            elif(field == "hgt"):
                if(value.endswith("cm")):
                    if not (int(value[:-2]) in range(150, 193 + 1)):
                        return 0
                elif(value.endswith("in")): 
                    if not (int(value[:-2]) in range(59, 76 + 1)):
                        return 0
            elif(field == "pid"):
                if not (len(value) == 9):
                    return 0
                if not (value.isdigit()):
                    return 0
            elif(field == "byr"):
                if not (int(value) in range(1920, 2020 + 1)):
                    return 0
            elif(field == "iyr"):
                if not (int(value) in range(2010, 2020 + 1)):
                    return 0
            elif(field == "eyr"):
                if not (int(value) in range(2020, 2030 + 1)):
                    return 0
            else: continue
        return 1
                
    def extract(self, passport):
        final_passport = " ".join([item for item in passport])
        
        content = {}
        for value in final_passport.split():
            pair = value.split(":")
            if(len(pair) != 2):
                continue
            
            content[pair[0]] = pair[1]
        
        return content
        