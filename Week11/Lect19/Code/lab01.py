

def computeSpeed(kms, minutes):
    #v = km / h
    hours = minutes / 60
    v = kms / hours
    print('Traveling at ', v, 'km/h')
    return v