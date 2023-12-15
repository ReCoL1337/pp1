def p1(p1,p2):
    cards = {'A':10, 'K':10, 'Q':10, 'J':10, 'T':10}
    hands = [p1, p2]
    result = []
    for i in hands:
        value = 0
        for j in i:
            if j.isdigit():
                value += int(j)
            else:
                value += cards.get(j)
        result.append(value)
    if result[0] >= result[1]:
        return True
    else:
        return False

def p2(arr: list):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]

def p3(array2d):
    rowcount = 0
    for i in array2d:
        row = 0
        col = 0
        col = sum(i)
        for r in array2d:
            row += r[rowcount]
        rowcount += 1
        if col == row:
            continue
        else:
            return False
    return True

def p4(sub: dict):
    for key, value in sub.items():
        x = sum(value)
        x /= len(value)
        sub.update({key: x})
    return sorted(sub.items(), key=lambda n: n[1])[-1][0]

def p5(fl: str, ll: str):
    import re
    count = 0
    with open('09-Test2\mock\data.txt', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if word.isalpha() is False:
                    print(word)
                    word = re.sub(r'[+*|()$}{,;:]*', '', word)
                    word = re.sub(r'\.*$', '', word)
                    print(word)
                if word.startswith(fl) and word.endswith(ll):
                    count += 1
    return count


def p6(y, c):
    import json
    count = 0
    with open('09-Test2\mock\data.json') as file:
        details = json.loads(file.read())
        for i in details:
            if i.get('age') >= y:
                studies = i.get('studies')
                courses = studies.get('courses')
                for j in courses:
                    if j.get('name') == c:
                        grades = j.get('grades')
                        summ = sum(grades)
                        summ /= len(grades)
                        if summ >= 4:
                            count += 1
    return count                    




if __name__ == '__main__':
    #print(p1("AJ972","K8"))
    #print(p2([5,5,5,5,5,5,5,7]))
    #print(p3([[3,7,2],[4,2,5],[5,2,1]]))
    #print(p3([[3,7,2],[4,2,5],[9,2,1]]))
    #print(p4({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
    print(p5('w','d'))
    #print(p6(21,'statistics'))