def next_houses_number(houses):
    global counter
    counter += 1
    if counter == 1:
        prev = houses[0]
        return houses[0]
    else:
        difference = 9999
        next_house = 0
        for i in range(len(houses)):
            difference = min(difference, abs(houses[i]-prev))
            
            
    

counter = 0
