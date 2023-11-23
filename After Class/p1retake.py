def p1(a, b):
    if a > b:
        x = a - b
        result = f"{a} - {b} = {x}"
    else:
        x = a + b
        result = f"{a} + {b} = {x}"
    return result

def p2(n):
    prime = 0
    return result

def p3(p):
    if len(p) >= 6:
        return True
    else:
        return False
    
def p4(w):
    result = ""
    for i, char in enumerate(w):
        if i % 2 == 0:
            result += char + '+'
        else:
            result += char + '-'
    return result[:-1]

def p5(a, b):
    if a < b:
        result = ""
        x = range(a, b + 1)
        for i in x:
            if i % 2 == 0:
                result += str(i) + ","
    return result[:-1]

def p1result():
    print (p1(20,8))
    print (p1(8,12))
    print (p1(7,7))

if __name__ == '__main__':
    print (p1result())
    print (p3("asd"))
    print (p3("asdasd"))
    print (p4("ajksdbfojasdhbf"))
    print (p5(4,6))