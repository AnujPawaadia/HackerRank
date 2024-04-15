if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    sorted_records = sorted(records, key = lambda x: x[1])
    min = 0
    first_ele = sorted_records[0]
    key = first_ele[1]
    for element in sorted_records:
        if(element[1] > key):
            second_lowest = element[1]
            break
    names = []
    for element in sorted_records:
        if(element[1] == second_lowest):
            names.append(element[0])
    names = sorted(names)
    for name in names:
        print(name)
