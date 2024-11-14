def list_to_str(lis):
    
    list = "["
    for e in lis:
        list += str(e)
        list += ", "
    list += "]"
    return list

if __name__ == '__main__':
    print(list_to_str([5, 6, 9, 0]))