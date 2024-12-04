def sublist(list, e):
    index = list.index(e)
    sublist1 = list[:index]
    sublist2 = list[index + 1: len(list)]
    list = [sublist1, sublist2]
    return list

def split_list(L, E):
    res = []
    for e in E:
        res.extend(sublist(L, e))
    print(res)
    

def split_list2(L, E):
    res = []
    temp = []
    for e in L:
        if e in E:
            res.append(temp)
            temp = []
        else:
            temp.append(e)
    res.append(temp)
    return res

print(split_list2([1, 2, 6, 4, 5, 3, 7] ,[3, 6]))

        
