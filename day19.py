def mutate_string(string, position, character):
    empty_string = ""
    list1 = list(string)
    list1[position] = character
    result_string = empty_string.join(list1)
    return result_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
