# Print all integers, decreasingly from 10 000 to 1, that are divisible by 7.
# count = 10000
# while count != 0:
#     if count % 7 == 0:
#         print(count)
#     count -= 1

[print(i) for i in range(1000, 0, -1) if i % 7 == 0]
