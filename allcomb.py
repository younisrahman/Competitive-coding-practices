import itertools

stuff = ["jim", 'younis', 'kaka']
arr = []
for L in range(0, len(stuff) + 1):
    str = ''
    for subset in itertools.combinations(stuff, L):
        str += ''.join(subset)
        arr.append(str)

print(arr)
