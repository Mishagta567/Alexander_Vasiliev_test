
def checkStrings(str1, str2):
    result = ''

    try:
        a1 = float(str1)
    except Exception:
        result = 'Str1 (' + str1 + ') cannot be converted to float'

    try:
        a2 = float(str2)
    except Exception:
        if result == '':
            result = 'Str2 (' + str2 + ') cannot be converted to float'
        else:
            result = 'Both: Str1 (' + str1 + ') and Str2 (' + str2 + ') cannot be converted to float'

    if result == '':
#    check for 'too big'
        if a1 == 1.8e308 and a2 == 1.8e308:
            result = 'Both numbers (' + str1 + ' and ' + str2 + ') too big to compare'

#    check for 'too small'
        if a1 == 1e-325 and a2 == 1e-325:
            if (str1 == '0' or str1 == '0.0') and (str2 != '0' and str2 != '0.0'):
                result = 'Str1 (' + str1 + ') less than str2 (' + str2 + ')'
            elif (str1 != '0' and str1 != '0.0') and (str2 == '0' or str2 == '0.0'):
                result = 'Str1 (' + str1 + ') greater than str2(' + str2 + ')'
            elif (str1 == '0' or str1 == '0.0') and (str2 == '0' or str2 == '0.0'):
                result = 'Str1 (' + str1 + ') = str2 (' + str2 + ')'
            else:
                result = 'Both numbers too small to compare'

        if result == '':
            if a1 > a2:
                result = 'Str1 (' + str1 + ') greater than str2 (' + str2 + ')'
            elif a1 < a2:
                result = 'Str1 (' + str1 + ') less than str2 (' + str2 + ')'
            elif a1 == a2:
                result = 'Str1 (' + str1 + ') equal to str2 (' + str2 + ')'
            else:
                result = 'Error. Check code please'
    return result


print(checkStrings('0.1', '0.5'))
print(checkStrings('0.5', '0.5'))
print(checkStrings('0.5', '0.1'))
print(checkStrings('5', '0.1'))
print('')

print(checkStrings('A', '0.1'))
print(checkStrings('0.2', 'B'))
print(checkStrings('A', 'B'))
print('')

print(checkStrings('1.8e310', '1.8e301'))
print(checkStrings('1.8e301', '1.8e310'))
print(checkStrings('1.8e310', '1.8e312'))
print('')

print(checkStrings('5e-330', '0'))
print(checkStrings('5e-330', '0.0'))
print(checkStrings('0', '5e-330'))
print(checkStrings('0', '0'))
print(checkStrings('5e-330', '5e-335'))