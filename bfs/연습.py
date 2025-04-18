from itertools import combinations
c = ((1, 2), (3, 4),(5,6))
for idx, zc in enumerate(combinations(c,2)):
    print(idx, zc)