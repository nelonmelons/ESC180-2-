def match_pattern(list1, list2):
    for i in range (0, len(list1) - len(list2)):
        if list2[0] == list1[i]:
            match = True
            for j in range(0, len(list2)):
                if list1[i+j] != list2[j]: # how tf does this work (isnt j out of index for list2)
                    match = False
            if match:
                return True
    return False

if __name__ == '__main__':
    print(match_pattern([1, 2, 3, 7, 4, 5, 6, 7, 8, 9, 10], [7, 8, 9]))