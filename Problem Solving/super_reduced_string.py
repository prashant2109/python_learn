st = 'baab'
c_lst = []
for ix, i in enumerate(st):
    if c_lst and c_lst[-1] == i:
        c_lst.pop()
    else:
        c_lst.append(i)
res = ''.join(c_lst)

