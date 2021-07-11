import time

# Importing colors from colors.py
from color import *

def cocktail_sort(data, drawData, timeTick):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(data) - 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                drawData(data, [YELLOW if x == i+1 or x == i else RED for x in range(len(data))] )
                time.sleep(timeTick)
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(len(data)-2,0,-1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                drawData(data, [YELLOW if x == i+1 or x == i else RED for x in range(len(data))] )
                time.sleep(timeTick)
                swapped = True
    
    drawData(data, [RED for x in range(len(data))])
