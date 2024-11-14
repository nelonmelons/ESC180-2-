#f = open(<filename>)
# e.g., f = open("data2.txt")
#text = f.read()
# text is a string that contains the contents of the entire file

def get_word_counts(path: str) -> dict:
    with open(path) as f:
        text = f.read()
    words = text.split()
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def top10(L):
    top10 = []
    L = sorted(L, reverse=True)
    top10 = L[0:10]
    return top10


def top10_freq_words(path: str) -> list:
    d = get_word_counts(path)
    inv = dict()
    for i, j in d.items():
        inv[j] = i
    s = sorted(list(inv.keys()), reverse = True)
    returnlist = []
    for i in range(10):
        returnlist.append(inv[s[i]])
    return returnlist

print(get_word_counts("sample.txt"))

