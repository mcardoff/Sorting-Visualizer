import time

# Importing colors from colors.py
from color import *

def selection_sort(data, drawData, timeTick):
    for i in range(0,len(data)-1):
        jmin = i
        for j in range(i+1, len(data)):
            jmin = j if data[j] < data[jmin] else jmin

        if jmin != i:
            data[i], data[jmin] = data[jmin], data[i]
            drawData(data, [YELLOW if x == i or x == jmin else RED for x in range(len(data))] )
            time.sleep(timeTick)
    drawData(data, [RED for x in range(len(data))] )
