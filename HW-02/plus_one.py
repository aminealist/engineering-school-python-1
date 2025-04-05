def plus_one1(x: list[int]) -> list[int]:
    x.reverse()
    x[0] += 1
    for j in range(1, len(x)):
        x[j] = x[j] + x[j - 1] // 10
        x[j - 1] %= 10
    if x[-1] > 9:
        x += [x[-1] // 10]
        x[-2] %= 10
    x[-1] %= 10
    x.reverse()
    return x


def plus_one2(x: list[int]) -> list[int]:
    return list(map(int, list(str(int(''.join(list(map(str, x)))) + 1))))
