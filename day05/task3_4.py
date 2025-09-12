my_dict = {
    " dalmatians ": 101,
    " pi ": 3.14,
    " beast ": 3 * 2 * 111,
    " life ": 42,
    " googol ": 10 ^ 100,
}
max_k = max(my_dict, key=my_dict.get)
print(max_k)
