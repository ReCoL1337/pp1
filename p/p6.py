def f(b1,b2,b3,b4):
    count = 0
    if b1:
        count += 1
    if b2:
        count += 1
    if b3:
        count += 1
    if b4:
        count += 1
    if count >= 3:
        return True
    else:
        return False