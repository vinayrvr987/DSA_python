"""Given two positive numbers x and y. Find the maximum valued integer a such that: 
 

a divides x i.e. x % a = 0
a and y are co-prime i.e. gcd(a, y) = 1
"""


def gcd(num1, num2):
    ans = 0
    max_num = num1 if num1 > num2 else num2
    for i in range(1, int(max_num) + 1):
        if num1 % i == 0 and num2 % i == 0:
            ans = i
    return ans


def max_val_integer(x, y):
    """Basic approach
    ans = 0
    max_num = x if x > y else y
    for i in range(1, max_num + 1):
        if x % i == 0 and gcd(i, y) == 1:
            ans = i"""

    # Following euclids algorithm
    while gcd(x, y) != 1:
        x = x / gcd(x, y)
    return int(x)


if __name__ == "__main__":
    print(max_val_integer(15, 3))
    print(max_val_integer(14, 28))
    print(gcd(14, 28))
