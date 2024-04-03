
if __name__ == '__main__':
    string = input()
    methods = [
        "isalnum", "isalpha", "isdigit", "islower", "isupper"
    ]

    for method in methods:
        validations = [getattr(char, method)() for char in string]
        print(any(validations))
