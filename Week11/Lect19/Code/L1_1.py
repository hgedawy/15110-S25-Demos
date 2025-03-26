
def simple_computation(day, month):
    
    value = 7
    value = value * month
    value = value - 1
    value = 13 * value
    value = value + day
    value = value + 3
    value = value * 11
    value = value - month
    value = value - 26
    value = value / 10
    value = value + 11
    value = value / 100
    return value
    
simple_computation(8, 3)

#print(vv)

#w = vv + 10
#print(w)