import time
import random

start = time.time()
n = 1000000
my_list = random.sample(range(1, n + 1), n)
my_list.sort()  # 1.6669116020202637 | 1.6677026748657227 | 1.6924443244934082
# sorted_list2 = sorted(my_list)
# 1.693662166595459 | 1.693662166595459 | 1.6525518894195557

print(time.time() - start)
