
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
assert(len(arr) == n)

A = set(map(int, input().split()))
assert(len(A) == m)
B = set(map(int, input().split()))
assert(len(B) == m)

happiness = sum(1 for x in arr if x in A)
happiness += sum(-1 for x in arr if x in B)

print(happiness)
