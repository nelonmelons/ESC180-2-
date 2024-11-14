def simplify_fraction(n, m):
    largest = max(n, m)
    while m % largest != 0 or n % largest != 0:
        largest -= 1
    k = n / largest
    d = m / largest
    if d == 1:
            print(int(k))
    else:
        print(str(int(k)) + str("/") + str(int(d)))
        
    
m = 10
n = 10
largest = max(n, m)
while m % largest != 0 or n % largest != 0:
    largest -= 1
k = n / largest
d = m / largest
if d == 1:
        print(int(k))
else:
    print(str(int(k)) + str("/") + str(int(d)))


    