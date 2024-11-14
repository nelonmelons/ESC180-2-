def display_current_value():
    global value, prevalue, prevalue2
    print(value)


def add(to_add):
    global value
    global prevalue, prevalue2
    prevalue2 = prevalue
    prevalue = prevalue2
    value += to_add


def mult(to_mult):
    global value
    global prevalue, prevalue2
    prevalue2 = prevalue
    prevalue = value
    value = value * to_mult

def div(to_div):
    global value
    global prevalue, prevalue2
    prevalue2 = prevalue
    prevalue = value
    value = value / to_div

def memory():
    global memoryvalue, value
    memoryvalue = value

def recall():
    global memoryvalue, value
    global prevalue
    value = memoryvalue

def undo():
    global value
    global prevalue
    prevalue, value = value, prevalue

def undo2():
    global value, prevalue, prevalue2
    prevalue2, value = value, prevalue2
    




if __name__ == "__main__":
    prevalue = 0
    prevalue2 = 0
    print("Welcome to the calculator program.\nCurrent value: 0")
    value = 0
    display_current_value()
    add(1)
    display_current_value()
    mult(2)
    display_current_value()
    undo()
    display_current_value()
    add(5)
    display_current_value()
    undo2()
    display_current_value()
    

