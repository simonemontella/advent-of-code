import os
import re

def days():
    classes = []
    path = "C:\\Users\\siste\\OneDrive\\Desktop\\smont\\advent-of-code\\solutions"

    for file in os.listdir(path):
        if(file.startswith("day")):
            classes.insert(int(re.findall(r'\d+', file)[0])-1, str(file.replace(".py", "")))

    return classes

if __name__ == '__main__':
    for day in days():
        solution = getattr(__import__(str("solutions." + day)), day.replace("d", "D"))
        solution().solve()
