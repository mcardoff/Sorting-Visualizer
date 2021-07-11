import time
import math

# Importing colors from colors.py
from color import *

# bubble sort
def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [YELLOW if x == j or x == j+1 else RED for x in range(len(data))] )
                time.sleep(timeTick)
                
    drawData(data, [RED for x in range(len(data))])

# Cocktail shaker sort
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

# insertion sort
def insertion_sort(data, drawData, timeTick):
    for i in range(1,len(data)):
        j = i - 1
        while j >= 0 and data[j-1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]
            drawData(data, [YELLOW if x == j-1 or x == j else RED for x in range(len(data))] )
            time.sleep(timeTick)
            j -= 1
        

    drawData(data, [RED for x in range(len(data))])

# library sort
def library_sort(data, drawData, timeTick):
    pass

# merge sort
def merge_sort(data, drawData, timeTick):
    def merge(start, mid, end):
        p = start
        q = mid + 1
        temp = []

        for i in range(start, end+1):
            if p > mid:
                temp.append(data[q])
                q += 1
            elif q > end:
                temp.append(data[p])
                p += 1
            elif data[p] < data[q]:
                temp.append(data[p])
                p += 1
            else:
                temp.append(data[q])
                q += 1

        for p in range(len(temp)):
            data[start] = temp[p]
            start += 1
    
    def merge_sort_rec(start, end):
        if(start < end):
            mid = math.floor((start+end)/2)
            merge_sort_rec(start,mid)
            merge_sort_rec(mid+1,end)

            # two lists, now merge them
            merge(start, mid, end)
            drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                            else DARK_BLUE if x > mid and x <=end else RED for x in range(len(data))])
            time.sleep(timeTick)

    merge_sort_rec(0, len(data)-1)
    drawData(data, [RED for x in range(len(data))])
    
# quick sort
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

# radix sort
def radix_sort(data, drawData, timeTick):
    pass

    
# selection sort
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

# stooge sort
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

# timsort
def tim_sort(data, drawData, timeTick):
    pass
