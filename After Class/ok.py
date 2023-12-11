def f(a,b):
    x = 10
    result = f'wartosc x = {x}'
    return result

def p2(n):
    
    return "ok"

def p3(p):
    count = 0
    for i in p:
        count += 1
    if count >= 6:
        return True
    else:
        return False

def p4(w):
    result = ''
    for index, literka in enumerate(w):
        print(f'index: {index}, literka: {literka}')
        if index % 2 == 0:
            result += literka + '+'
        else:
            result += literka + '-'
    return result[:-1]

def bin(n):
    verify = set("01")
    if set(n) == verify:
        return True
    else:
        return False


def p6(n, even):
    num1 = 0
    num2 = 0
    for i in str(n):
        i = int(i)
        if i % 2 == 0:
            num1 += i
        else:
            num2 += i
    if even:
        return num1
    else:
        return num2


if __name__ == '__main__':
    x = [[123,123,321],[123,321456,7865]]
    print()
    print(x[0])