def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """
    dict = ""
    for key, value in d.items():
        dict += str(key) + "," + str(value) + "\n"
    return dict
        
        
    pass # replace this with your code
print(dict_to_str({1:2, 5:6}))

