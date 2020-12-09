from solutions.solution import Solution
import re

class Day7(Solution):
    
    def __init__(self):
        super().__init__(7)

    def part1(self):
        return self.searchin()
    
    def part2(self):
        pass
    
    def rules(self):
        rules = {}
        for line in self.lines:
            rule = [rule.strip() for rule in line.split("contain")]
            
            key = re.sub(r'bags?', "", rule[0]).strip()
            rules[key] = [re.sub(r'bags?|[.]', "", content).strip() for content in rule[1].split(",")]
        
        return rules
    
    
    blacklist = []

    def searchin(self):
        rules = self.rules()
        def find(key):
            if(key == "shiny gold"):
                return 1
            if(key != "no other"):
                container = [key[1:].strip() if key != "no other" else key for key in rules[key]]
                for bag in container:
                    if find(bag):
                        return 1
            
            return 0
        
        count = 0
        for bag in rules:
            if(bag == "shiny gold"):
                continue
        
            count += find(bag)
        return count   