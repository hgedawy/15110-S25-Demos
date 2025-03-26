
def exchangingCards(ra, oa, rb, ob):

    a_can_give = 0
    for ca in ra:
        if (ca not in rb) and (ca not in ob):
            a_can_give += 1

    b_can_give = 0
    for cb in rb:
        if (cb not in ra) and (cb not in oa):
            b_can_give += 1

    return min(a_can_give, b_can_give)

def simple_subseq_match(sequence, subseq):
    count = 0
    for i in range(len(sequence)):
        if sequence[i:i+len(subseq)] == subseq:
            count += 1
    return count

def findAndRemove(L, n):
    if n not in L:
        return 0
    positions = []
    start = 0
    L_remove = L[:]
    for i in range( L.count(n) ):
        print(start)
        pos = L[start:].index(n)
        positions.append(start + pos)
        start += pos + 1
    positions.reverse()
    for i in range( L.count(n) ):
        L_remove.remove(n)
    if len(L_remove) == 0:
        diff = 0
    else:
        diff = max(L_remove) - min(L_remove)
    return (positions, L, L_remove, diff)
        
    
        