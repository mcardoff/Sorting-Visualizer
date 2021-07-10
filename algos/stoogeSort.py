import time
import math

# Importing colors from colors.py
from color import *

def stooge_sort(data, drawData, timeTick):
    def stooge_rec(data, i, j):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
            drawData(data, [YELLOW if x == j or x == i else RED for x in range(len(data))] )
            time.sleep(timeTick)
        if (j - i + 1) > 2:
            t = math.floor((j - i + 1) / 3)
            stooge_rec(data, i, j-t)
            stooge_rec(data, i+t, j)
            stooge_rec(data, i, j-t)

    stooge_rec(data, 0, len(data)-1)
    drawData(data, [RED for x in range(len(data))])
