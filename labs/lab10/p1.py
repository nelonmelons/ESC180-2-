# call itself i.e. use recursion
# base case is n = 0
#recursive step is n=1

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    

#problem 2
#base case is when number is a one digit number
def sumdigits(n):
    if n < 10:
        return n
    else:
        return n%10 + sumdigits(n//10)

