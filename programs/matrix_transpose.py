def mt(ll):
    len_row = len(ll[0])
    len_col = len(ll)
    res_lst = []
    for i in range(len_row):
        ch_lst = []
        for j in range(len_col):
            ch_lst.append(ll[j][i])
        res_lst.append(ch_lst)
    print(res_lst)
    return

def matrix_transpose(ll):
    len_row = len(ll[0])
    len_col = len(ll)
    res_lst = []
    for i in range(len_row):
        r_lst = []
        for j in range(len_col):
            r_lst.append(ll[j][i])
        res_lst.append(r_lst)
    return res_lst

if __name__ == '__main__':
    # mt([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
    print(matrix_transpose([[1, 2, 3], [4, 5, 6], [6, 7, 8]]))