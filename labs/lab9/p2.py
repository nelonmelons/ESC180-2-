def binary_search(L, e):
    low = 0
    high = len(L) - 1
    counter = 0
    while high - low >= 2:
        counter += 1
        mid = (low + high) // 2  # e.g., 7 // 2 == 3
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid
    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    else:
        return None
    
def binary_search2(L, e):
    low = 0
    high = len(L) - 1
    counter = 0
    while high - low >= 2:
        counter += 1
        mid = (low + high) // 2  # e.g., 7 // 2 == 3
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid, counter
    if L[low] == e:
        return low, counter
    elif L[high] == e:
        return high, counter
    else:
        return None, counter

def part_a():
    L = [1, 5, 7, 4, 3, 35, 342, 15, 5925, 2592, 1323, 434]
    print(binary_search(L, 35))

def part_b():
    L = [1, 5, 7, 4, 3, 35, 342, 15, 5925, 2592, 1323, 434]
    print(binary_search2(L, 2592))
    
    
def part_c():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for e in L:
        print(binary_search2(L, e))
    # making e in the middle element will make binarysearch return early
    
def part_d():
    L = []
    for i in range(10000):
        L.append(i)
    e = L[9998]
    print(binary_search2(L, e))
    
import time
def run_timebinary(L, e):
    start = time.time()
    binary_search(L, e)
    end = time.time()
    print(end-start)
    
def run_timelinear(L, e):
    start = time.time()
    L.index(e)
    end = time.time()
    print(end-start)
    
    
def part_e():
    L = []
    for i in range(9999999):
        L.append(i)
    e = L[9999997]
    run_timebinary(L, e)
    run_timelinear(L, e)
    
part_e()