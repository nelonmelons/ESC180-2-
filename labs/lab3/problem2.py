i = 0
n = 0
while (i < 1001):
    j = ((-1) ** i) / (2*i + 1)
    n += j
    i += 1
    
print(4 * n)