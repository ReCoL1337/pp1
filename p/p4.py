def f(n):
    result = ""
    if n % 2 == 0:
        if n < 0:
            n = str(n)
            result = n[1:]
            result = int(result)
        else:
            result = '-' + str(n)
            result = int(result)
    else:
        if n < 0:
            n = str(n)
            result = n[1:]
            result = int(result)
        else:
            result = str(n)
            result = int(result)
    return result