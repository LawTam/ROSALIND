import operator
gc_string = None
stats = {'a':1000, 'b':3000, 'c': 100}
items = stats.items()
maximum = max(stats.values())
for key in items:
    if key[1] is maximum:
        print(key[0])
        print(key[1])
