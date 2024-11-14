L = [4, 1, 6]
L1 = sorted(L) # L1 is [1, 4, 6]
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    Engineering Science, University of Toronto Page 2 of 6
    ESC 180 H1F Lab #8 Fall 2024
    in ascending order."""
    keys = []
    dict = ""
    for key, value in d.items():
        keys.append(key)
    keys = sorted(keys)
    for k in keys:
        dict += f"{k}, {d[k]} \n"
        
    return dict

print(dict_to_str_sorted({1:2, 0:3, 10:5}))