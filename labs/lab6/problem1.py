L = [["CIV", 92],
    ["180", 98],
    ["103", 99],
    ["194", 95]]

print(L[2][1])

def get_nums(L):
    num = []
    for i in range(len(L)):
        num.append(L[i][1])
    return num
