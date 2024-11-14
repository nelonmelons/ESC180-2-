#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    sum = (a + b) * 2
    return sum
  else:
    return (a + b)

def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False

def set_square(x):
    global ret_square
    ret_square = x**2   
    return ret_square