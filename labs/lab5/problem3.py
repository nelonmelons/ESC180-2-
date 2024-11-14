def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range (len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    print(lists_are_the_same([3, 5, 7], [3, 5, 7]))
    print(lists_are_the_same([1, 2, 3], [4, 5, 6]))
            
        
        
        