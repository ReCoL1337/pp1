def p1(l):
    result = 0
    for i in l :
        result += i
    return result

def p2(l):
    result = 1
    if 0 not in l:
        for i in l :
            result *= i
        return result
    else:
        return 'Nuh uh'
    
def p3 (l: list) -> int:
    l.sort(reverse=True)
    return l[0]

def p4 (l: list) -> int:
    l.sort()
    return l[0]

def p5(l: list) -> int:
    result = 0
    for i in l:
        if i[0] == i[-1]:
            result += 1
    return result

def p6(l: list):
    return sorted(l, key=lambda n: n[-1])

def p7(l: list):
    for i in l:
        x = l.count(i)
        if x != 1:
            l.remove(i)
    return l

def p8(l: list):
    if l == []:
        return True
    else:
        return False
    
def p9(l: list):
    clone = []
    for i in l:
        clone.append(i)
    return clone

def p10(l: list, n: int):
    result = []
    for i in l:
        if len(i) > n:
            result.append(i)
    return result

def p11(n: str):
    listt = n.split(" ")
    return listt
        
def p12(n,m):
    listt = []
    slowo = ''
    for i, l in enumerate(n):
        if l == ' ':
            listt.append(slowo)
            slowo = ''
        elif i == len(n)-1:
            slowo += n[i]
            listt.append(slowo)
        else:
            slowo += l
    return listt


if __name__ == '__main__':
    print(p1([0,2,6,4,7,8,12,7,8,134]))
    print(p2([1,5,2,6,7]))
    print(p3([3,6,8,21,6,7,1,48,2]))
    print(p4([3,6,8,21,6,7,1,48,2]))
    print(f"Result: {p5(['abc', 'xyz', 'aba', '1221'])}")
    print(p6([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
    print(p7([8,4,8,2,7]))
    print(p8([]))
    print(p9([5,7,2,7,2136]))
    print(p10(['asddaasd','aeryhery','asd','a'], 3))
    print(p11("Lucyferaaf asdasd asdasdas"))
    print(p12('dasdsa asdasd dsadasd dasd', 1))