import urllib.request

def choose_variant(variants):
    for i in variants:
        f = urllib.request.urlopen(f'https://ca.search.yahoo.com/search?p={urllib.parse.quote(i)}')
        lines = f.read().decode("utf-8").split('\n')
        search_results = ''
        for j in lines:
            if 'search results' in j:
                start = j.find('About ')
                end = j.find(' search results')
                search_results = j[start+6:end]
        print(f'{i}: {search_results}')


choose_variant(["top ranked school uoft", "top ranked school waterloo"])