def f(t):
    result = ''
    for i, char in enumerate(t):
        result += char * (i+1)
    return result

print(f("ok"))