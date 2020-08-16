from collections import Counter
def count_occurence_character(ip_str):
    dct = Counter(ip_str)
    sum_vals = sum(dct.values())
    st_opt = ', '.join([f'{k}={v}' for k, v in dct.items()])
    print (f'string output is {st_opt}')
    print (f'sum is {sum_vals}')
count_occurence_character('erwweewewewtt')