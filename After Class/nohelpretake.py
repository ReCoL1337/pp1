def p1(a, b):
    if a > b:
        x = a - b
        result = f"{a}-{b}={x}"
    else:
        x = a + b
        result = f"{a}+{b}={x}"
    return result

def p3(p):
    if len(p) < 6:
        return False
    else:
        return True

def p4(w):
    result = ''
    for i, char in enumerate(w):
        if i % 2 == 0:
            result += char + '+'
        else:
            result += char + '-'
    return result[:-1]

def p5(a, b):
    result = ''
    for n in range(a, b + 1):
        if n % 2 == 0:
            result += str(n) + ','
    return result[:-1]

if __name__ == '__main__':
    print(p1(8,12))
    print(p3("fdg12"))
    print(p4("abcdefgh"))
    print(p5(3,11))