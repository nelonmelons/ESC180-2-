
def count_evens(L):
    n = 0
    for num in L:
        if num%2 == 0:
            n += 1
    return n

if __name__ == '__main__':
    print(count_evens([35, 2, 4, 5, 24224]))

