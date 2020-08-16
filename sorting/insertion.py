def insertion_sort(lt):
    n = len(lt)
    for i in range(1, len(lt)):
        key  = lt[i]
        j = i-1
        while (j>=0 and key<lt[j]):
            lt[j+1] = lt[j]
            j -= 1
        lt[j+1] = key
    return lt

def i_s(lt):
    n = len(lt)
    for i in range(1, n):
        key = lt[i]
        j = i-1
        while j>=0 and key<=lt[j]:
            lt[j+1] = lt[j]
            j -= 1
        lt[j+1] = key
    return lt

if __name__ == '__main__':
    lt = [23, 4, 7, 1, 5]
    # print(insertion_sort(lt))
    print(i_s(lt))

