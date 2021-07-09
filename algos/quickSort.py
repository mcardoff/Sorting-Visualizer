import time

# Importing colors from colors.py
from color import *

def quick_sort(data, drawData, timeTick):

    def quick_sort_rec(data, lo, hi, drawData, timeTick):
        if lo < hi:
            p = partition(data, lo, hi, drawData, timeTick)
            quick_sort_rec(data, lo, p-1, drawData,timeTick)
            quick_sort_rec(data, p+1, hi, drawData,timeTick)

    def partition(data, lo, hi, drawData, timeTick):
        pivot = data[hi]
        i = lo
        for j in range(lo,hi):
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                drawData(data, [YELLOW if x == j or x == i else RED for x in range(len(data))])
                i += 1
                time.sleep(timeTick)
        data[i], data[hi] = data[hi], data[i]
        drawData(data, [YELLOW if x == i or x == hi else RED for x in range(len(data))])
        time.sleep(timeTick)
        return i

    quick_sort_rec(data, 0, len(data)-1,drawData,timeTick)
    drawData(data, [RED for x in range(len(data))])
