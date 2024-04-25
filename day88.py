if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        _, A = input(), set(map(int, input().split(" ")))
        _, B = input(), set(map(int, input().split(" ")))
        print(A.issubset(B))
