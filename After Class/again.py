def p1(n):
    coins = 0
    coins += n // 5
    n %= 5
    coins += n // 2
    n %= 2
    n += coins
    return n

def p2(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n3 != n1:
        return True
    else:
        return False

def p3(name):
    result = name[0]
    for i, char in enumerate(name):
        if char == ' ':
            result += name[i+1]
    return result

def p4(card):
    result = ''
    for i, char in enumerate(card):
        if i < 1:
            result += char
        elif 1 < i < 12:
            result += '*'
        else:
            result += char
    return result

def p5(binary):
    verify = set('01')
    bin = set(binary)
    if bin == verify:
        return True
    else:
        return False

def p6(number, even):
    number = str(number)
    n1 = 0
    n2 = 0
    for i, char in enumerate(number):
        char = int(char)
        if char % 2 == 0:
            n1 += char
        else:
            n2 += char
    if even == True:
        return n1
    else:
        return n2
    
def p7(a,b):
    if a > b:
        x = a - b
        result = f'{a}-{b}={x}'
    else:
        x = a + b
        result = f'{a}+{b}={x}'
    return result

def p8(p):
    if len(p) >= 6:
        return True
    else:
        return False
    
def p9(w):
    result = ''
    for i, char in enumerate(w):
        if i % 2 == 0:
            result += char + '+'
        else:
            result += char + '-'
    return result[:-1]

def p10(a, b):
    result = ''
    for i in range(a, b + 1):
        if i % 2 == 0:
            result += str(i) + ','
    return result[:-1]

def p11(t,c,n):
    if t.count(c) == n:
        return True
    else:
        return False

if __name__ == "__main__":
    print(p1(23))
    print(p2(4,8,4))
    print(p3("Internet of Things"))
    print(p4("5290312400019022"))
    print(p5("10101010a1"))
    print(p6(5272,False))
    print(p7(8,12))
    print(p8("ax15asdasd"))
    print(p9("abcdefgh"))
    print(p10(2,3))
    print(p11("ccc","c",3))