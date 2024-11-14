import math
#print(round(math.pi*(10**5)))
#print(round(5.65))
i = 0
n = 0
sf = 3
while True:
    j = ((-1) ** i) / (2*i + 1)
    n += j
    i += 1
    if (round((n * 4)*(10**sf))) == round(math.pi*(10**sf)):
        break
    
print(i)
print(n * 4)

