n,m = list(map(int, input().split()))

char1='|'
char2='.'

cnt = 1
pat = 1
for i in range(1,n+1):
    if i <= (n//2):
        print((pat*(char2+char1+char2)).center(m,'-'))
        pat += 2
    elif i > ((n//2)+1):
        print((pat*(char2+char1+char2)).center(m,'-'))
        pat -=2
    elif i == ((n//2)+1):
        print('WELCOME'.center(m,'-'))
        pat -=2
    cnt += 1
