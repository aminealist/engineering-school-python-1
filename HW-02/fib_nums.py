import numpy as np


def fib1(n: int) -> int:
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    prev, cur = 0, 1
    for _ in range(n):
        prev, cur = cur, prev + cur
    return prev


def fib3(n: int) -> int:
    fib_matrix = [[1, 1],
                  [1, 0]]
    fib = [[1, 0],
           [0, 1]]
    while n:
        if n & 1:
            fib = np.matmul(fib, fib_matrix)
        fib_matrix = np.matmul(fib_matrix, fib_matrix)
        n >>= 1
    return fib[0][1]


for i in range(19):
    print(fib1(i), fib2(i), fib3(i))
