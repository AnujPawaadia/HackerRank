sizeM = int(input())
M = set(map(int, input().split()))
sizeN = int(input())
N = set(map(int, input().split()))
A = sorted(list(M^N))
for x in A:
    print (x)
