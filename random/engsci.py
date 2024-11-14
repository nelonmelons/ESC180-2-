def drink_coffee():
    global current_time, coffee, too_much_coffee, coffee_time, coffee_time2, coffee_counter
    coffee = True
    if (current_time - coffee_time2) < 120:
        too_much_coffee = True
    
    coffee_time2 = coffee_time
    coffee_time = current_time

    

    

def study(minutes):
    global current_time, coffee, knols, too_much_coffee
    current_time += minutes
    if too_much_coffee == True:
        return
    elif coffee == True:
        knols += 10 * minutes
    else:
        knols += 5 * minutes
    coffee = False
    
#The following initialize function is given
def initialize():
    global too_much_coffee
    global current_time
    global coffee_time
    global coffee_time2
    global knols, coffee, coffee_counter
    too_much_coffee = False
    current_time = 0
    knols = 0
    coffee_time = -100
    coffee_time2 = -100
    coffee = False
    coffee_counter = 0


if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    print(knols)
    study(20) # knols = 400
    print(knols)
    drink_coffee() # knols = 400
    study(10) # knols = 500
    print(knols)
    drink_coffee() # knols = 500
    study(10) # knols = 600
    print(knols)
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600
    print(knols)
