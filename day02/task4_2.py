# Calculate Pi using :
#  f(x) = (2x-1)² /  6 + f(x+1)

# 3.141592


def cal_pi(x, lim):
    if x > lim:
        return 0

    return (2 * x - 1) ** 2 / (6 + cal_pi(x + 1, lim))


print(round(cal_pi(1, 100) + 3, 6))
