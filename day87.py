def build_pair(signs, level):
    if level == 0:
       return ['']
    result = []
    for i, sign in enumerate(signs):
        from_below_level = build_pair(signs[i:], level - 1)
        result += [sign + below for below in from_below_level]
    return result


if __name__ == '__main__':
    _in = input().split()
    S = sorted(str(_in[0]))
    k = int(_in[1])
    
    for pair in build_pair(S, k):
        print(pair)
