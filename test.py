def gcd_in_two_lines(a: int, b: int) -> int:
    while b: a, b = b, a % b
    return a
