'''
(p1.py) The vending machine accepts
1, 2 and 5 PLN coins. Define the function
f(amount_to_pay) that returns the minimum number
of coins that can be used to pay
for the purchased product.
'''
def f(n):
    coins = 0
    coins += n//5
    print(coins)
    n %= 5
    print(n)
    coins += n//2
    print(coins)
    n %= 2
    print(n)
    coins += n
    print(coins)
    return coins

print(f(9))
