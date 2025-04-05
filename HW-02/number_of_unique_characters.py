def number_of_unique_characters(string: str) -> dict[str, int]:
    s = dict()
    for c in string:
        if c not in s:
            s[c] = 0
        s[c] = 1 + s.get(c, 0)
    return s


print(number_of_unique_characters('abcd'))
