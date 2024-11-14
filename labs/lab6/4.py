def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    
    return -(term1 + term2 + term3)

def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w01, w02, w12))


#part A:
    '''if both x1 and x2 are positive, or they are both negative, multiplying by a larger weight will make |term1| larger 
    since E = -term1 - term2 - term3
    will make energy state lower'''

#Part B
def store_memory(x0, x1, x2, w01, w02, w12):
    for i in range(4):
        if x0*x1 > 0:
            w01 += 0.1
        elif x0*x1 < 0:
            w01 -= 0.1
        if x0*x2 > 0:
            w02 += 0.1
        elif x0*x2 < 0:
            w02 -= 0.1
        if x1*x2 > 0:
            w12 += 0.1
        elif x1*x2 < 0:
            w12 -= 0.1
    
    return w01, w02, w12

if __name__ == "__main__":
    w01 = 2
    w02 = -1
    w12 = 1
    x0 = -1
    x1 = 1
    x2 = 1
    print_all_energies(w01, w02, w12)
    w01,w02,w12 = store_memory(x0, x1, x2, w01, w02, w12)
    print('==================')
    print_all_energies(w01, w02, w12)

    
