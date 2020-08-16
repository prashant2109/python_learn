import itertools as it
import operator as opr


###################################################
# for i in it.count(10, 0.5):
#     if i > 13:break
#     print(i)
###################################################
# cycle
# for i in it.cycle('ABC'):
#     print(i)
###################################################
# repeat
# for i in it.repeat('STRING', 3):
#     print(i)
###################################################
# accumulate
# ll = [5, 3, 6, 2, 1, 9, 1]
# res = it.accumulate(ll, opr.add)
# print(list(res))
###################################################
# chain
# ll_chain = [[1, 2, 3, 4], [5, 6]]
# print(list(it.chain(*ll_chain)))
###################################################
# chain.from_iterable
# ll_chain = [[1, 2, 3, 4], [5, 6]]
# print(list(it.chain.from_iterable(ll_chain)))
###################################################
# compress
# ll_compress = [1, 2, 4, 0, 0]
# st = [98, 89, 312, 43, 433.02]
# res = it.compress(st, ll_compress)
# print(list(res))
###################################################
# drop while
# ll_drop = [1, 4, 6, 4, 1]
# res = it.dropwhile(lambda x:x<5, ll_drop)
# print(list(res))
###################################################
# res = it.filterfalse(lambda x:x%3, range(20))
# print(list(res))
###################################################
# li =[(2, 5), (3, 2), (4, 3)]
# n_li = list(map(pow, li))
# n_li = list(it.starmap(pow, li))
# print(n_li)
###################################################