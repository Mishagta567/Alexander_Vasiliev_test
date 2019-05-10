
def isThereoverlap(a1, a2, b1, b2):
    result = False
#   sort first:
    if a1 < a2:
        vA1 = a1
        vA2 = a2
    else:
        vA1 = a2
        vA2 = a1

    if b1 < b2:
        vB1 = b1
        vB2 = b2
    else:
        vB1 = b2
        vB2 = b1

# just compare first and last values.
    if vA1 < vB1:
        if vA2 >= vB1:
            result = True
    elif vA1 > vB1:
        if vA2 <= vB2:
            result = True
    else:
        result = True
    return result


print(isThereoverlap(1, 6, 5, 10))
print(isThereoverlap(6, 1, 5, 10))
print(isThereoverlap(1, 6, 10, 5))
print(isThereoverlap(1, 5, 5, 10))

print(isThereoverlap(1, 4, 6, 10))
print(isThereoverlap(4, 1, 6, 10))
