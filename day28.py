def merge_the_tools(string, k):
    # st_str=""
    global st_dct
    st_dct={}
    st_lst=[]
    count=0
    for ch in string:
        if count<k:
            st_dct[ch]=1
            count+=1
        else:
            count=1
            st_lst.append("".join(st_dct.keys()))
            st_dct={}
            st_dct[ch]=1
    else:
        st_lst.append("".join(st_dct.keys()))
    for ch in st_lst:
        print(ch)
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
