from cmath import phase

if __name__ == "__main__":
    number = complex(input())
    r = abs(number)
    phi = phase(number)
    print(r)
    print(phi)
