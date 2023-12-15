def p1(p1: str,p2: str):
    s1 = 0
    s2 = 0
    karty = {'A': 10, 'K': 10, 'Q': 10, 'J': 10, 'T': 10}
    for i in p1:
        if i.isdigit():
            i = int(i)
            s1 += i
        else:
            s1 += karty.get(i)
    for i in p2:
        if i.isdigit():
            i = int(i)
            s2 += i
        else:
            s2 += karty.get(i)
    if s1 >= s2:
        return True
    else:
        return False

def p2(arr: list):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]
    
def p3(tab2d: list):
    for i in tab2d:
        row = 0
        col = 0
        col = sum(i)
        print(f'column: {i}, sum:{col}')
        for j in i:
            row += j
            print(f'num: {j}')
        print(f'sum of row: {row}')
        if col == row:
            continue
        else:
            
            return False
    return True

def p4(sub: dict):
    for x, y in sub.items():
        count = 0
        for ocena in y:
            count += ocena
        sub.update({x:count/len(y)})
    return sorted(sub.items(), key=lambda n: n[-1])[-1][0]

def p7(arr: list):
    count = 0 
    for i in arr:
        low = 0
        nums = 0
        if  4 <= len(i) <= 12:
            if '_' in i:
                for j in i:
                    if j.isdigit():
                        nums += 1
                    elif j.lower():
                        low += 1
                if nums != 0 and low != 0:
                    count += 1
    return count


if __name__ == '__main__':
#    print(p1("AJ972","AQT72"))
#    print(p1("9532","K8"))
#    print(p2([7,7,7,7,7,5]))
#    print(p3([[3,7,2],[4,2,5],[9,2,1]]))
#    print(p4({"math":[3,4,4], "geo":[5,4,4,4],"comp":[5,4]}))
    print(p7(["uek","water_7_x","anna2_.may","a_b_c_2_e_f"]))