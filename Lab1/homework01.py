from operator import add, sub

# --------------------------------

def a_plus_abs_b(a, b):
    """输入两个数 a、b, 实现 a + abs(b), 不允许调用 abs 函数, abs是计算绝对值
    
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# --------------------------------

def two_of_three(a, b, c):
    """从3个正数中挑选2个最大的, 求出这两个数的平方和, x*x + y*y
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a*a + b*b + c*c - min(a, b, c) - min(a, b, c)

# --------------------------------

def largest_factor(n):
    """给一个整数n, 翻出除n外最大的因数
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    import math
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return n // i
    return 1

# --------------------------------

def if_function(condition, true_result, false_result):
    """如果 if 条件满足,就返回第一个结果;不满足条件,就返回第二个结果
    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
    
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False

def t():
    print("it's running")

def f():
    return 1

# --------------------------------

def hailstone(n):
    """给1整数n,反复执行以下过程
       1.如果n是偶数,则除以2
       2.如果n是奇数,则乘3再加1
       3.如果n等于1,退出
    打印n变化过程,并返回一共变化的次数
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    step = 1
    while True:
        print(n)
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        step += 1
    return step

