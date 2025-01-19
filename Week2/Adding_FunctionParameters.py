

def function_name(day, month): #header
    value = 7
    value = value * month
    value = value - 1
    value = 13 * value
    value = value + day
    value = value + 3
    value = value * 11
    value = value - month
    value = value - day
    value = value / 10
    value = value + 11
    value = value / 100
    return value



output = function_name(29, 8)
print('Ouput is:', output)