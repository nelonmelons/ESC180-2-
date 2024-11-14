def list1_start_with_list2(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range (len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    print(list1_start_with_list2([3, 5, 7, 9], [3, 5, 7]))
    print(list1_start_with_list2([1, 2, 3], [4, 5, 6]))