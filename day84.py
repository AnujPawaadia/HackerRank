if __name__ == '__main__':
    s = input()
    occ_dict = {}
    for i in s:
        occ_dict[i] = occ_dict.get(i, 0) + 1
    
    sorted_list1 = sorted(occ_dict.items(), key=lambda x: x[0])
    sorted_list2 = sorted(sorted_list1, key=lambda x: x[1], reverse=True)
    
    for i in sorted_list2[:3]:
        print(*i)
