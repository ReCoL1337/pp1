def a(x, y):
    result = x / y
    return result

def b(a, b, c, d):
    x = a + b
    y = c + d
    result = x / y
    return result

def c(x, y):
    result = (int(x / y))
    return result

def d(x, y):
    result = x % y
    return result

def f(x, y):
    result = x ** y
    return result

def g(x):
    result = x * x
    return result

def h(x, y):
    result = (x * y) / 100
    return result

def swap(x, y):
    z = x
    x = y
    y = z
    result = f"Value of x is: {x}\nValue of y is: {y}"
    return result

def cube(a):
    volume = a ** 3
    sa = 6 * a ** 2
    result = f"Side of the cube: {a}\nVolume of the cube: {volume}\nSurface Area of the cube: {sa}"
    return result

def div(x, y):
    d = int(x / y)
    r = x % y
    result = f"Division result: {d}\nRemainder: {r}"
    return result

def asc(x, y):
    if x > y:
        order = f"{y}, {x}"
    else:
        order = f"{x}, {y}"
    result = f"Numbers in ascending order: {order}"
    return result

def pname(name):
    if name[len(name)-1] == "a":
        result = f"{name} - Polish female name"
    else:
        result = "Not a polish female name"
    return result

def dog(x):
    age = 0
    for i in range(x):
        if i <= 1:
            age += 10.5
            i += 1
        else:
            age += 4
            i += 1
    result = f"In dog years: {age}"
    return result

def promo(previous, current):
    p = ((current * 100) / previous)
    percent = 100 - p
    if percent >= 30:
        result = f"Current price: {current}\nPrevious price: {previous}\nBuy the product!!\nPrice reduced by: {percent}%"
    return result

if __name__ == '__main__':
    '''print (a(15, 38))
    print (b(3, 4, 5, 9))
    print (c(7, 2))
    print (d(48, 5))
    print (f(2, 10))
    print (g(49))
    print (h(80, 25))
    print (swap(7, 34))
    print (cube(4))
    print (div(17, 5))'''
    print (asc(14, 27))
    print (pname("Anna"))
    print (dog(15))
    print (promo(200, 140))