def two_sum(a: list[int], x: int) -> list[int]:
    mem = dict()
    for i, val in enumerate(a):
        if x - val in mem:
            return [mem[x - val], i]
        if val not in mem:
            mem[val] = i
    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([4, 5, 9, 5], 10))
print(two_sum([-4, 3, 10, 0], -1))