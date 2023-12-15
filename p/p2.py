def f(n1,n2):
    n2 = str(n2)
    n1 = str(n1)
    for i in n2:
        for j in n1:
            if j == i:
                return True
    return False