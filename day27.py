def minion_game(string):
    import string as st
    vouels = 'AEIOU'
    consonants = ''.join([letter for letter in st.ascii_uppercase if letter not in vouels])
    kevin_score = 0
    stuart_score = 0
    string_numerated = enumerate(string)
    for i, l in string_numerated:
        if l in vouels:
            kevin_score += len(string[i:])
        elif l in consonants:
            stuart_score += len(string[i:])
    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    if stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')
    if stuart_score == kevin_score:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
