# act_data = ['989', '191', '111']
act_data = ['1112', '1912', '1892', '1234']
mtx_dt = [[int(i) for i in i_str] for i_str in act_data]
# print(mtx_dt)
rln = len(mtx_dt)
cln = len(mtx_dt[0])
res_op = []
for r_idx in range(rln):
    if r_idx in (0, rln-1):
        res_op.append(mtx_dt[r_idx])
        continue
    ch_lst = []
    for c_idx in range(cln):
        if c_idx in (0, cln-1):
            ch_lst.append(mtx_dt[r_idx][c_idx])
            continue
        el = mtx_dt[r_idx][c_idx]
        left    = mtx_dt[r_idx][c_idx-1]
        top     = mtx_dt[r_idx-1][c_idx]
        right   = mtx_dt[r_idx][c_idx+1]
        bottom  = mtx_dt[r_idx+1][c_idx]
        if ((left>el) or (top>el) or (right>el) or (bottom>el)):
            ch_lst.append(str(el))
        else:
            ch_lst.append('X')
    res_op.append(ch_lst)
# print (res_op)
print('\n'.join([''.join([str(i) for i in i_st]) for i_st in res_op]))

            

        



