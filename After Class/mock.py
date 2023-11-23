def p1(a):
    coins = 0
    coins += a // 5
    a %= 5
    coins += a // 2
    a %= 2
    a += coins
    return a

def p2(n1,n2,n3):
    if n1 != n2 & n2 != n3 & n3 != n1:
        return True
    else:
        return False
    
def p3(name):
    out = name[0]
    for i in range(1, len(name)):
        if name[i] == ' ':
            out += name[i+1]
    return out

def p4(card):
    mask = ''
    for i, char in enumerate(card):
        if i <= 1:
            mask += char
        elif 2 < i < 11:
            mask += '*'
        elif i > 11:
            mask += char
    return mask

def p5(binary):
    bin = set('01')
    val = set(binary)
    if val.issubset(bin):
        return True
    else:
        return False
    
def p6(number, even):
    sum = 0
    for i in str(number):
        i = int(i)
        if even and i % 2 == 0:
            sum += i
        elif not even and i % 2 != 0:
            sum =+ i
    return sum

if __name__ == "__main__":
    print(p1(23))
    print(p2(2,9,2))
    print(p3("Internet of Things"))
    print(p4("5290312400019022"))
    print(p5("101a01"))
    print(p6(3124,True))