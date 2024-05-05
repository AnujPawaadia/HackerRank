def stack_blocks(blocks):
    prev, i, j = -1, 0, len(blocks) - 1
    while i < j:
        bi, bj = blocks[i], blocks[j]
        if bi > bj:
            b, i = bi, i+1
        else:
            b, j = bj, j-1
        if prev >= b or prev == -1:
            prev = b
        else:
            return "No"
    return "Yes"
 
for i in range(int(input())):
    input()
    blocks = list(map(int, input().split()))
    print(stack_blocks(blocks))
