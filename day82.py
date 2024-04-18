from itertools import permutations

inp = input().split(' ')
string, k = inp[0], int(inp[1])

all_perm = [''.join(p) for p in permutations(string,k)]
sorted_perm = sorted(all_perm)
for p in sorted_perm:
    print(p)
