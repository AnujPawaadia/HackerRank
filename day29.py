
def print_rangoli(size):
    import string
    letters_in_rangoli = ('-'.join(sorted(string.ascii_lowercase[0:size], reverse=True)
                        + sorted(string.ascii_lowercase[1:size]))
                        )
    rangoli_with = len(letters_in_rangoli)
    r1, r2 = 2, rangoli_with -3
    if rangoli_with == 1:
        print('{0:-^{1}}'.format(letters_in_rangoli[0], rangoli_with))
    else:
        print('{0:-^{1}}'.format(letters_in_rangoli[0], rangoli_with))
        for i in range(0, rangoli_with//2 - 1):
            while i < rangoli_with//4 - 1:
                letters_this_line = letters_in_rangoli[:r1] + letters_in_rangoli[r2:]
                print('{0:-^{1}}'.format(letters_this_line, rangoli_with))
                r1, r2 = r1 + 2, r2 - 2
                break
            while i > rangoli_with//4 - 2:
                letters_this_line = letters_in_rangoli[:r1] + letters_in_rangoli[r2:]
                print('{0:-^{1}}'.format(letters_this_line, rangoli_with))
                r1, r2 = r1 - 2, r2 + 2
                break
        print('{0:-^{1}}'.format(letters_in_rangoli[0], rangoli_with))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
