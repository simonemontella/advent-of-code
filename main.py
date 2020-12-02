import os

def days():
    classes = []
    path = "C:\\Users\\siste\\j-workspace\\adventofcode2020\\solutions"
    
    for file in os.listdir(path):
        if(file.startswith("day")) :
            classes.append(str(file.replace(".py", "")))
    
    return classes 
    
if __name__ == '__main__':
    for day in days() :
        solution = getattr(__import__(str("solutions." + day)), day.replace("d", "D"))
        solution().solve()