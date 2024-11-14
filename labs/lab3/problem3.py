#approach 1
def gcd(n, m):
    j = 0
    a = 0
    for i in range(1, m + 1):
        if m % i == 0 and n % i == 0:
            j = i
    
    for k in range(1, n + 1):
        if n % k == 0 and m % k == 0:
            a = k
    if (j > a):
        return j
    else:
        return a
    
#approach 2
def gcd2(n, m):
    largest = max(n, m)
    while m % largest != 0 or n % largest != 0:
        largest -= 1
    return largest

if __name__ == '__main__':
    print(gcd(5, 31))
    print(gcd2(5, 31))
    


    
        
    