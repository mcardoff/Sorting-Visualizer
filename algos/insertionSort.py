import time

# Importing colors from colors.py
from color import *

def insertion_sort(data, drawData, timeTick):
    for i in range(1,len(data)):
        j = i - 1
        while j >= 0 and data[j-1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]
            drawData(data, [YELLOW if x == j-1 or x == j else RED for x in range(len(data))] )
            time.sleep(timeTick)
            j -= 1
        

    drawData(data, [RED for x in range(len(data))])
