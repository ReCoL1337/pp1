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
            result += name[i + 1]
    return result

def p4(card):
    result = ''
    for i, char in enumerate(card):
        if i <=1:
            result += char
        elif 1 < i < 12:
            result += '*'
        else:
            result += char
    return result

def p5(binary):
    verify = set('01')
    binary_set = set(binary)
    if binary_set == verify:
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

if __name__ == "__main__":
    print(p1(23))
    print(p2(4,8,4))
    print(p3("Internet of Things"))
    print(p4("5290312400019022"))
    print(p5("101010101"))
    print(p6(3124,True))