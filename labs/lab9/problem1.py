
#part b
def g(L):
    L = L[:]
    return L

def g1(L):
    res = L
    return res

#part c
def part_c():
    d = {"hedons": 5 , "test": 3}
    v = d.copy()
    for i, j in v.items():
        print(i, j)

#part d
import copy
def part_d():
    dic = {"chocolate": [3], "age": [5]}
    shallow_copy = dic.copy()
    dic["chocolate"].append(79)
    print(dic, shallow_copy)

def part_e():
    dic2 = {"chocolate": [3], "age": [5]}
    deep_copy = copy.deepcopy(dic2)
    dic2["chocolate"].append(79)
    print(dic2, deep_copy)
    
    
part_e()
    


    
    