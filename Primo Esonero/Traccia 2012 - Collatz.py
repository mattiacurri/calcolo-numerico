nInput = int(input())

""" Implementare la congettura di Collatz """

def collatz(nInput):
    list = []
    while nInput != 1:
        if nInput % 2 == 0:
            nInput = nInput // 2
        elif nInput % 2 == 1:
            nInput = 3 * nInput + 1        
        list.append(nInput)
    return list
print(collatz(nInput))