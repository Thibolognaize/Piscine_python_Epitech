from string import punctuation

special = set(punctuation)


def funA(s, n):
    return len(s) == n


def funB(s, n):
    s_specials = []
    for c in s:
        if c in special:
            s_specials += c
    if len(s_specials) == n:
        return True
    else:
        return False


def funC(s, n):
    return str(n) in s
