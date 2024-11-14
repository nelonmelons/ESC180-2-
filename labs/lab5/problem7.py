#part a
def inst_velocity(x, i):
    if len(x)-2 == i or len(x)-1 == i:
        estimate1, estimate2 = (x[i] - x[i-1])/0.1
    elif i == 0 or i == 1:
        estimate1, estimate2 = (x[i+1] - x[i])/0.1
    else:
        estimate1 = (x[i+1] - x[i - 1])/0.2
        estimate2 = (x[i+2] - x[i - 2])/0.4
        
#part b
import random
