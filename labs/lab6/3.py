def lookup(L, num):
    for i in range(len(L)):
        if L[i][1] == num:
            return i
        else:
            return None
        
        