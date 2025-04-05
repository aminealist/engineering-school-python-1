def is_correct_brackets_seq1(s: str) -> bool:
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            return False
    return False if stack else True


def is_correct_brackets_seq2(s: str) -> bool:
    delta = 0
    for c in s:
        delta += 1 if c == '(' else -1
        if delta < 0:
            return False
    return delta == 0
