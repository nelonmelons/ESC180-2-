


text = open("ccc_results.txt", encoding="latin-1").read().split("\n")
dummy = ""
d = {}
for i in text:
    dummy = ""
    lines = i.split()
    for j in lines:
        if j != j.upper():
            dummy += j
    if dummy in d:
        d[dummy] += 1
    else:
        d[dummy] = 1
        
for key, value in d.items():
    print(key, value)
    

            
                
    
    
    