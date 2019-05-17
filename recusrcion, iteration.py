#fibonaci by using generators
"""def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a+b

for item in fib(12):
    print(item)"""

#generators for listing dictionarz items
"""myDict = {"throne": "iron", "ass": "huge", "number": "infinite"}
for key,val in myDict.items:
    print("item {} is {}".format(key,val))"""

#recursive multiplication
"""def rec_mult(m, n):
    #base case for recursive multiplication
    if n == 0:
        return 0
    elif n >= 1:
        return m + rec_mult(m, n-1)
    elif n <= -1:
        return -m + rec_mult(m, n+1)"""

#iterative multiplication - same case
"""def iter_mult(m, n):
    if n == 0 or m  == 0:
        return 0

    result = m * n
    if n >= 1:
        while n > 0:
            result += m
            n -= 1
    elif n <= -1:
        while n < 0:
            result += -m
            n += 1
    return result

print("iterative multiplication: ")
print(iter_mult(3, 4))
print(iter_mult(-1, 4))
print(iter_mult(-2, 4))
print(iter_mult(2, -4))
print(iter_mult(0, 0))"""

#recursion of fibonachi
"""def rec_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return rec_fib(n -1) + rec_fib(n - 2)

print("recursive fibonachi is: ")
print(rec_fib(0))
print(rec_fib(1))
print(rec_fib(2))
print(rec_fib(3))
print(rec_fib(10))"""

#iterative of fibonachi
"""def iter_fib(n):
    if n == 0 or n ==1:
        return n
    else:
        previous_fib = 0
        current_fib = 1
        for iteration in range(1, n):
            next_fib = current_fib + previous_fib
            previous_fib = current_fib
            current_fib = next_fib
        return  current_fib

print(iter_fib(10))"""

#faktorial
"""def f(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

def fact(n):
    assert n >= 0
    if n <= 1:
        return n
    else:
        return n*fact(n - 1)

def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

def h(x):
    assert type(x) == int and x >= 0
    answer = 0
    s = str(x)
    for c in s:
        answer += int(c)
    return answer"""

