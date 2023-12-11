def f(n):
    num1 = 0
    num2 = 1
    next_num = num2
    count = 0
    result = [0, 1, 1]
    while count <= n:
        count += 1
        num1 = num2
        num2 = next_num
        next_num = num1 + num2
        result.append(next_num)
    print(result)
    return result[n - 1]


print(f(9))