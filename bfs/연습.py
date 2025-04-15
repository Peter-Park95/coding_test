from itertools import product
lst = [1,2,3,4,5,6]
for l in product(lst, repeat=len(lst)):
    print(l)